---
order: 195
---

# Hlasovanie

Základná myšlienka hlasovania spočíva vo validácii prichádzajúceho zoznamu hlasov z [gateway-a](../../gateway/synchronization_service.md), ktorá musí prejsť niekoľkými krokmi. Samotný zoznam prichádzajúcich hlasov je zašifrovaný pomocou vlastnej knižnice *electiersa*, ktorého štruktúra je následovná:

```python
class VoteEncrypted(BaseModel):
    encrypted_message: str
    encrypted_object: str

class VotesEncrypted(BaseModel):
    polling_place_id: int
    votes: List[VoteEncrypted] = []
```

Ak je validácia úspešná, spomínaný zoznam prichádzajúcich hlasov sa uloží do kolekcie *votes* a informuje používateľa. V opačnom prípade, server vráti špecifickú hlášku, vďaka ktorej používateľ bude vedieť, v akom kroku bola validácia neúspešná.

## Validácia
- *ID* volebnej miestnosti sa musí nachádzať v kolekcii *key_pair*
- počet zvolených kandidátov nesmie byť väčší ako 5
- každý kandidát sa v prichádzajúcom hlase môže vyskytovať iba raz
- nezadaná politická strana nesmie obsahovať žiadneho kandidáta
- kandidát musí patriť do správnej politickej strany
- v kolekcii *votes* sa nesmie nachádzať duplitcitná kombinácia tokenu a *ID* volebnej miestnosti
- v príchádzajúcom zozname hlasov sa nesmie nachádzať duplicitný token
- *ID* volieb musí byť totožné s tým, ktoré sa nachádza v konfiguračnom súbore *config.py*

## Popis API

### vote_elections_vote_post

<a id="opIdvote_elections_vote_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/elections/vote', headers = headers)

print(r.json())

```

`POST /elections/vote`

*Vote*

Process candidate's vote

> Body parameter

```json
{
  "polling_place_id": 0,
  "votes": [
    {
      "encrypted_message": "36AMNvcpAWdHAXKCSWexgyjxrt7xeWwhOf+oUMBqip/C051...",
      "encrypted_object": "lb5B/LAg2/38mot9jYzRpa9O6YwrXDilpspPrGrnTKKYUXS8..."
    }
  ]
}
```

<h3 id="vote_elections_vote_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[VotesEncrypted](#schemavotesencrypted)|true|none|

> Example responses

> 200 Response

```json
{
  "status": "string",
  "message": "string"
}
```

<h3 id="vote_elections_vote_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Message](#schemamessage)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Message](#schemamessage)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

### get_voting_data_elections_voting_data_get

<a id="opIdget_voting_data_elections_voting_data_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/elections/voting-data', headers = headers)

print(r.json())

```

`GET /elections/voting-data`

*Get Voting Data*

Downlaod voting data json using command curl http://localhost:8222/elections/voting-data > config.json

> Example responses

> 200 Response

```json
{
  "polling_places": [],
  "parties": [],
  "key_pairs": [],
  "texts": {
    "elections_name_short": {
      "sk": "string",
      "en": "string"
    },
    "elections_name_long": {
      "sk": "string",
      "en": "string"
    },
    "election_date": {
      "sk": "string",
      "en": "string"
    }
  }
}
```

<h3 id="get_voting_data_elections_voting_data_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[VotingData](#schemavotingdata)|

<aside class="success">
This operation does not require authentication
</aside>

### get_zapisnica_elections_zapisnica_get

<a id="opIdget_zapisnica_elections_zapisnica_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/elections/zapisnica', headers = headers)

print(r.json())

```

`GET /elections/zapisnica`

*Get Zapisnica*

> Example responses

> 200 Response

```json
null
```

<h3 id="get_zapisnica_elections_zapisnica_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="get_zapisnica_elections_zapisnica_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

