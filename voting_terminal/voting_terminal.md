---
order: 101
---
# Volebný terminál
Volebný terminál je zariadenie, s ktorým požívateľ bezprostredne interaguje. Pozostáva z frontendu, s ktorým interaguje používateľ a backendu, ktorý obsluhuje požiadavky frontendu a komunikuje s periférnymi zariadeniami a gateway-om.

## Architektúra

Hardwérové zapojenie volebného terminálu možno vidieť na nasledujúcom obrázku, pričom na obrázku je zobrazená aj architektúra gatewaya s ktorým volebný terminál komunikuje, čo je jednou z hlavných funkcionalít backendu volebného terminálu.

![](/assets/images/vt/vt_devices.png)

Z obrázku vidíme, že dotyková obrazovka, s ktorou interaguje používateľ je prepojená s RPi, ktorá predstavuje základné výpočtové zariadenie celého backendu. Spojenie je vytvorené cez rozhranie HDMI. Ďalej ku backendovému RPi je napojená tlačiareň pomocou sieťového kábla a čítačka NFC tagov, ktorá komunikuje s backendom cez USB rozhranie. RPi je napojené do routra volebnej miestnosti pomocou sieťového ethernetového kábla, s ktorým rovnakým spôsobom komunikuje aj gateway.

## Mikroslužba

Ako už bolo spomenuté volebný terminál pozostáva z frontendu a backendu, pričom je každá z týchto služieb kontajnerizovaná pomocou dockeru a spolu sú cez docker compose orchestrované do jednej mikroslužby.

## Frontend

Frontend volebného terminálu je implementovaný v jazyku Typescript pomocou frameworku Svetle, pričom sme pri návrhu GUI používali zaužívaný štandard ID-SK, ktorý je používaný vo všetkých štátnych aplikáciách.

## Backend

Backend volebného terminálu je implentovaný v jazyku python, pričom sme použili framework [Fast API](https://fastapi.tiangolo.com/) na implementáciu API rozhrania. Úlohou backendu je práve cez toto API obsluhovať požiadavky gateway-a a frontendu. V kontajneri backendu volebného terminálu je ako operačný systém použitý Linux - Alpine.

### Komunikácia backendu

Backend komunikuje dvoma spôsobmi a to pomocou websocketov a klasických HTTP requestov.

#### Komunikácia cez websockety

Komunikácia cez websockety je použítá na obojsmernú komunikáciu, ktorá sa nedala implementovať API rozhraním. Na implementáciu socketov sme použili knižnicu [socketio](https://python-socketio.readthedocs.io/en/latest/client.htm) . Prakticky všetky informácie ktoré posiela backend na frontend sú prenesené cez websockety. Takýmto spôsobom sa posiela na frontend stav volieb, vďaka čomu sa potom na obrazovke môžu meniť scény.

Websockety sa taktiež používajú pri odosielaní volebného stavu a ID volebného terminálu na gateway. Websocketami naopak prijíma backend informáciu o zmene stavu volieb z gateway-u.

#### Komunikácia cez API rozhranie

Komunikácia cez API rozhranie je využitá primárne na odosielanie a príjmanie hlasu. Stručne špecifikované endpointy back-endu:
*   Základný hello world enpoint na adrese - `/`
*   Endpoint na prijatie hlasu od front-endu na adrese - `/api/vote_generated`
*   Endpoint na prijatie tokenu na adrese - `/token`
*   Endpoint na prijatie stavu volieb na drese - `/api/election/state`

Využivame aj metódu, ktorá sa spustí na začiatku životného cyklu FAST API clienta, pričom táto metóda vykoná úvodné nastavenia volebného terminálu ako natiahne privátne a verejné kľúče, zaregistruje volebný terminál na gateway tým, že odošle gateway-u svoj verejný kľúč a taktiež sa vytvorí websocketové pripojenie.

#### Komunikácia s tlačiarňou

Komunikácia s tlačiarňou je implementovaná cez knižnicu *CUPS*, ktorá bola do kontajneru doinštalovaná. Pri prvom odvolení sa tlačiareň zaregistruje na backende štandartným príkazom *lpadmin*. Pred samotnou registráciou tlačiarne je potrebné nainštalovať inštalačné skripty fungujúce ako driver od výrobcu tlačiarne. Z dôvodu, že použivame termotlačiareň EPSON TM-T20III sú drivre verejne dostupné na adrese https://download.epson-biz.com/modules/pos/index.php?page=single_soft&cid=6918&pcat=3&pid=6146 . Samotné vytlačenie hlasovacieho lístka sa potom vykoná odoslaním pdf súboru na tlač cez príkaz *lpr*.

#### Komunikácia s NFC čítačkou

TODO

### Definované metódy

Niektoré funkcionality, ktoré sú obsiahnuté v API špecifikácií sme už načrtli, okrem týchto API funkcií sú definované aj rôzne pomocné metódy, ich špecifikáciu uvádzame v tejto sekcií. Zdrojový kód je koncipovaný do piatich pythonovských súborov.


#### Súbor utils.py

**encrypt_message(data: dict)** je metóda ktorá pomocou knižnice na šifrovanie komunácie zašifruje dáta ktoré dostane ako vstup

**get_config()** je metóda, ktorá načíta súbor v JSON formáte, v ktorom sú uložené základné údaje o konfigurácií volieb

**reg_printer()** je metóda, ktorá cez CUPS zaregistruje tlačiareň pripojenú na IP adrese definovanej v systémovej premennej.

**print_ticket_out()** je metóda, ktorá vytlačí hlasovací lístok od používateľa uložený v súbore NewTicket.pdf

**prepare_printing_vote(vote: dict)** je metóda, ktorá vytvorí z hlasu od používateľa, ktorý je v JSON formáte PDF s obsahom hlasu

**transform_vote_to_print(vote: dict)** je metóda, ktorá vytvorí z prijatého hlasu od používateľa slovník, kde sú namiesto čísel poslancov a strán už reálne mená a názvy.

#### Súbor gateway_communication.py

**recieve_config_from_gateway()** je metóda, ktorá cez get request natiahne a načíta configuračný súbor z gateway

**send_current_election_state_to_gateway()** je metóda, ktorá odošle cez websocket volebný stav a ID volebného terminálu na gateway

**send_token_to_gateway(token: str)** je metóda, ktorá príme v argumente token s surovom stringovom formáte a odošle ho na gateway, pričom v závislosti od platnosti tokenou zmení scénu na obrazovke volebného terminálu. Ak bol token odoslaný na gateway validný tak je možné ďalej pokračovať vo volení a stav volieb sa nastaví ako pripravený na načítanie NFC tagu.

**send_vote_to_gateway()** je metóda, ktorá v argumente dostane hlas od používateľa vo formáte slovníka a v prípade, že ešte nie je zaregistrovaná tlačiareň tak ju zaregistruje. Po prípadnej registrácií sa hlas zašifruje a odošle na gateway. Ak bol hlas úspešne zvalidovaný tak sa následne vytlačí hlasovací lístok.

#### Súbor main.py

V tomto súbore je uložená špecifikácia API. Okrem tejto funkcionality obsahuje tento súbor aj dve funkcie na komunikáciu s front-endom

**send_current_election_state_to_frontend()** je metóda, ktorá odošle pomocou websocketu stav volieb

**change_state_and_send_to_frontend()** je metóda, ktorá aktualizuje stav volieb a informuje o tom aj front-end

#### Súbor imports.py

V tomto súbore sú uložené používané dátové štruktúry ako ID volebného terminálu, stav volieb, informácia o registrácií tlačiarne a taktiež tento súbor obsahuje uložený prípadný zvalidovaný token s getterom a setterom.

#### Súbor NationalTicket.py

Tento súbor obsahuje triedu, ktorá predstavuje špecifikáciu volebného lístka na tlačenie. Trieda NationalTicket je odvodená od BaseTicket a implementuje preťažené metódy na tvorbu PDF súboru z hlasu.

**create_pdf()** je metóda, ktorá vytvorí z hlasu PDF súbor a uloží ho do súboru NewTicket.pdf. PDF súbor sa vytvára pomocou knižnice FDPF pre Python. Funkcia na konci vytvorí z hlasu aj QR kód a vloží ho do PDF.

**preprocessText(candidates: list, max_line_len: int)** je metóda, ktorá upraví hlas aby bol lepšie tlačiteľný na volebnom hlase. Úlohou metódy je dlhé mená a názvy strán vhodne rozdeliť a usporiadať.

**__init__(data: dict)** je metóda, ktorá uloži zvolený hlas do triedy. Táto metóda je konštruktorom triedy.

## API

### hello__get

<a id="opIdhello__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/backend/', headers = headers)

print(r.json())

```

`GET /`

*Hello*

Sample testing endpoint 

> Example responses

> 200 Response

```json
null
```

<h3 id="hello__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="hello__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

### vote_api_vote_generated_post

<a id="opIdvote_api_vote_generated_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/backend/api/vote_generated', headers = headers)

print(r.json())

```

`POST /api/vote_generated`

*Vote*

Api method for recieving vote from fronend

Keyword arguments:
vote -- vote object that user created in his action

> Body parameter

```json
{
  "party_id": 0,
  "candidate_ids": [
    0
  ]
}
```

<h3 id="vote_api_vote_generated_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[VotePartial](#schemavotepartial)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="vote_api_vote_generated_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="vote_api_vote_generated_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

### token_post

<a id="opIdtoken_token_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/backend/token', headers = headers)

print(r.json())

```

`POST /token`

*Token*

Api method for recieving token from client

Keyword arguments:
token -- token that voter user

> Body parameter

```json
"string"
```

<h3 id="token_token_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|string|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="token_token_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="token_token_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

### receive_current_election_state_from_gateway_post

<a id="opIdreceive_current_election_state_from_gateway_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/backend/api/election/state', headers = headers)

print(r.json())

```

`POST /api/election/state`

*Receive Current Election State From Gateway*

Method for receiving current election state from gateway

Keyword arguments:
state -- current election state

> Body parameter

```json
{}
```

<h3 id="receive_current_election_state_from_gateway-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="receive_current_election_state_from_gateway-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="receive_current_election_state_from_gateway-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## API Schemas

<h2 id="tocS_HTTPValidationError">HTTPValidationError</h2>
<!-- backwards compatibility -->
<a id="schemahttpvalidationerror"></a>
<a id="schema_HTTPValidationError"></a>
<a id="tocShttpvalidationerror"></a>
<a id="tocshttpvalidationerror"></a>

```json
{
  "detail": [
    {
      "loc": [
        "string"
      ],
      "msg": "string",
      "type": "string"
    }
  ]
}

```

HTTPValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

<h2 id="tocS_ValidationError">ValidationError</h2>
<!-- backwards compatibility -->
<a id="schemavalidationerror"></a>
<a id="schema_ValidationError"></a>
<a id="tocSvalidationerror"></a>
<a id="tocsvalidationerror"></a>

```json
{
  "loc": [
    "string"
  ],
  "msg": "string",
  "type": "string"
}

```

ValidationError

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[string]|true|none|none|
|msg|string|true|none|none|
|type|string|true|none|none|

<h2 id="tocS_VotePartial">VotePartial</h2>
<!-- backwards compatibility -->
<a id="schemavotepartial"></a>
<a id="schema_VotePartial"></a>
<a id="tocSvotepartial"></a>
<a id="tocsvotepartial"></a>

```json
{
  "party_id": 0,
  "candidate_ids": [
    0
  ]
}

```

VotePartial

### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|party_id|integer|false|none|none|
|candidate_ids|[integer]|false|none|none|



# Dátová štruktúra

## Štruktúra hlasu odoslaného z frontendu

Po odvolení sa odošle z frontendu hlas na backend v tejto forme:

```yaml
VotePartial:
      type: object
      properties:
        party_id:
          type: integer
        candidate_ids:
          type: array
          items:
            type: integer
          maxItems: 5
```

## Štruktúra hlasu spracovaného pred tlačou
Na backende sa spracuje daný hlas vo forme slovníka. Pred tlačou je hlas transformovaný do inej podoby vďaka configuračnému súboru pre celé voľby, pričom sa *party_id* z hlasu páruje ku *_id* pre stranu v konfiguračnom súbore. Vďaka tomuto napárovaniu sa vytiahne z kofiguračného súboru meno volenej strany. Rovnakým spôsobom sa vytiahne pre každý prvok z poľa *candidate_ids* meno kandidáta. Výsledná dátová štruktúra ktorá sa posiela do funkcie na tvorbu PDFka pred tlačou vyzerá nasledovne:

```json
{
    "token": "valid",
    "vote": {
        "title": "Voľby do národnej rady",
        "candidates": ["2. Andrej Trnovec"],
        "party": "Slovenská ľudová strana Andreja Hlinku"
    }
}
```

## Štruktúra hlasu odoslaného na uloženie na gateway
Súčasťou životného cyklu hlasu je aj odoslanie a uloženie na gatewayi. Formát finálneho hlasu odoslaného a uloženého na gateway je nasledovný:

```yaml
Vote:
    allOf:
    - $ref: '#/components/schemas/VotePartial'
    - type: object  
        required:
        - election_id
        - token
        properties:
        token:
            type: string
        election_id:
            type: string
```

Pričom *election_id* je idečko volieb ktoré sa práve odohrávajú.


