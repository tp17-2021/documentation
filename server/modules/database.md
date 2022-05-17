---
order: 199
---
# Databáza
Server používa na ukladanie dát dokumentovú databázu [MongoDB](https://www.mongodb.com/). Aj keď je do MongoDB vkladať dáta s rôznymi atribútmi, používame modely jednoitlivých dátových entít, ktoré špecifikujú štruktúru objektu a definujú typy jeho atribútov. Pracujeme s nasledujúcimi kolekciami:
- votes
- parties
- candidates
- polling_places
- key_pairs

Štruktúra uloženého hlasu:
```python
class Vote(BaseModel):
    token: str
    party_id: Optional[int] = None
    election_id: str
    candidate_ids: List[int] = []
```
Dátová štruktúra hlasu obsahuje referenciu na . Ďalej sa počas spracovania hlasov dynamicky pridajú dva atribúty a to:

```python
polling_place_id: int
synchronized: bool
```
Atribút polling_place_id slúži na spojenie hlasu s miestnosťou, v ktorej bol zvolený a atribút synchronized, ktorý indikuje, či bol daný hlas už zandexovaný do Elastic Searchu.



Štruktúra politickej strany:
```python
class Party(BaseModel):
    id: int = Field(..., alias="_id")
    party_number: int
    name: str
    official_abbr: str
    abbr: str
    image: str
    image_bytes: str
    color: str
    candidates: List[Candidate] = []
```
Dátová štruktúra politickej strany obsahuje základné údaje ako názov, skratka a číslo a doplnkové údaje ako farba a logo, ktoré sa používajú v štatistickej aplikácii. Ďalej strana obsahuje zoznam kadidátov, ktorý sú reprezentovaný vlastným modelom.

Štruktúra volebnej miestnosti:
```python
class PollingPlace(BaseModel):
    id: int = Field(..., alias="_id")
    region_code: int
    region_name: str
    administrative_area_code: int
    administrative_area_name: str
    county_code: int
    county_name: str
    municipality_code: int
    municipality_name: str
    polling_place_number: int
    registered_voters_count: int
```
Dátová štruktúra volebnej miestnosti obsahuje ifnormácie o územných celkoch, v ktorých sa daná miestnosť nachádza. Tieto údaje budú následne použité na prepočítavanie výslekov pre rôzne lokality (obce, okresy a kraje).

Štruktúra kandidáta:
```python
class Candidate(BaseModel):
    id: int = Field(..., alias="_id")
    party_number: int
    order: int
    first_name: str
    last_name: str
    degrees_before: str
    age: int
    occupation: str
    residence: str
```
Dátová štruktúra kandidáta obsahuje základné údaje o kandidátovy, ktoré sú použité na zobrazovanie výsledkov a obsahuje taktiež prepojenie na politickú stranu, ktorej je súčasťou.

Štruktúra kľúčového páru:
```python
class KeyPair(BaseModel):
    id: int = Field(..., alias="_id")
    polling_place_id: int
    private_key_pem: str
    public_key_pem: str
    g_private_key_pem: str
    g_public_key_pem: str
```
Kľúčový pár je špecifický pre každú volebnú meistnosť a jeho privátnym kľúčom je dešifrovaná iba kominikácia, ktorá prichádza z tejto volebnej miestnosti. Tento krok zvyšuje bezpečnosť komunikácie.


## Popis API

### schema_database_schema_get

<a id="opIdschema_database_schema_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/database/schema', headers = headers)

print(r.json())

```

`GET /database/schema`

*Schema*

Get all collections from database

> Example responses

> 200 Response

```json
{
  "collections": []
}
```

<h3 id="schema_database_schema_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Collections](#schemacollections)|

<aside class="success">
This operation does not require authentication
</aside>

### import_data_database_import_data_post

<a id="opIdimport_data_database_import_data_post"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/database/import-data', headers = headers)

print(r.json())

```

`POST /database/import-data`

*Import Data*

> Example responses

> 200 Response

```json
{
  "status": "string",
  "message": "string"
}
```

<h3 id="import_data_database_import_data_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Message](#schemamessage)|

<aside class="success">
This operation does not require authentication
</aside>

### seed_data_database_seed_data_post

<a id="opIdseed_data_database_seed_data_post"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/database/seed-data', params={
  'number_of_votes': '0'
}, headers = headers)

print(r.json())

```

`POST /database/seed-data`

*Seed Data*

<h3 id="seed_data_database_seed_data_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|number_of_votes|query|integer|true|none|

> Example responses

> 200 Response

```json
{
  "status": "string",
  "message": "string"
}
```

<h3 id="seed_data_database_seed_data_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Message](#schemamessage)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

### seed_votes_database_seed_votes_post

<a id="opIdseed_votes_database_seed_votes_post"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/database/seed-votes', params={
  'number_of_votes': '0'
}, headers = headers)

print(r.json())

```

`POST /database/seed-votes`

*Seed Votes*

<h3 id="seed_votes_database_seed_votes_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|number_of_votes|query|integer|true|none|

> Example responses

> 200 Response

```json
{
  "status": "string",
  "message": "string"
}
```

<h3 id="seed_votes_database_seed_votes_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Message](#schemamessage)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>
