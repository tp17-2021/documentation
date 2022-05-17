# Výsledky a štatistiky

Výsledky volieb sa rátajú na serveri pomocou dát získaných z Elastic Searchu a funkcie `calcualte_winning_parties_and_seats`.

Na zobrazenie výsledkov ponákame viaceré koncové body ktoré výsledky vrátia s inou agregáciou alebo vráti len ich časť aby odpoveď nebola príliš veľká.

## Distupné koncové body:
- /elastic/get-parties-results 
    - získanie výsledkov politických strán bez kandidátov
- /elastic/get-party-candidate-results
    - získanie výsledkov všetkých strán a kandidátov
- /elastic/get-candidates-results
    - získanie výsledkov všetkých kandidátov
- /elastic/get-results-by-locality
    - získanie výsledkov všetkých strán a kandidátov pre určitú lokalitu

## Počítanie percent a parlamentných kresiel
Výpočet získaných kresiel sa vykonáva vo funkcii `calcualte_winning_parties_and_seats`.

```python
def calcualte_winning_parties_and_seats(transformed_data):
    """
    Find parties having more than 5% (threshold) and count all votes for these parties.
    In case parties have less then threshold value, take all parties
    Calculate relative vote percentage from this set of parties and calculate result seats for each party
    """
```

Algoritmus výpočtu:
1. Prepočítať poečt získaných hlasov pre všetky strany a získať tie ktoré majú nad 5%.
2. Počet republikové číslo (počet hlasov, potrebných pre získanie jedného mandátu, ráta s pomocou čísla 151)
3. Pomocou republikového čísla určiť na koľko kresiel má strana nárok a uchovať si počet po celočíselnom delení.
4. Ak neboli rozdané všetky kreslá, tak sa doplnia postupne stranám v poradí podľa zostatku po celočíselonom delení republikovým číslom.


<h1 id="fastapi-elastic-search">Elastic search</h1>

## setup_elastic_votes_index_elastic_setup_elastic_vote_index_post

<a id="opIdsetup_elastic_votes_index_elastic_setup_elastic_vote_index_post"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/elastic/setup-elastic-vote-index', headers = headers)

print(r.json())

```

`POST /elastic/setup-elastic-vote-index`

*Setup Elastic Votes Index*

Setup elastic search. Drop index if previously used. Create new index and variables mapping.

> Example responses

> 200 Response

```json
{
  "status": "string",
  "message": "string"
}
```

<h3 id="setup_elastic_votes_index_elastic_setup_elastic_vote_index_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Message](#schemamessage)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Message](#schemamessage)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[Message](#schemamessage)|

<aside class="success">
This operation does not require authentication
</aside>

## synchronize_votes_ES_elastic_synchronize_votes_es_post

<a id="opIdsynchronize_votes_ES_elastic_synchronize_votes_es_post"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/elastic/synchronize-votes-es', headers = headers)

print(r.json())

```

`POST /elastic/synchronize-votes-es`

*Synchronize Votes Es*

Batch synchronization of votes from Mongo DB to Elastic search 3 Node cluster. Shuld be called in specific intervals during election period.

<h3 id="synchronize_votes_es_elastic_synchronize_votes_es_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|number|query|any|false|none|

> Example responses

> 200 Response

```json
{
  "status": "string",
  "message": "string"
}
```

<h3 id="synchronize_votes_es_elastic_synchronize_votes_es_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Message](#schemamessage)|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Message](#schemamessage)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[Message](#schemamessage)|

<aside class="success">
This operation does not require authentication
</aside>

## get_parties_results_elastic_get_parties_results_post

<a id="opIdget_parties_results_elastic_get_parties_results_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/elastic/get-parties-results', headers = headers)

print(r.json())

```

`POST /elastic/get-parties-results`

*Get Parties Results*

> Body parameter

```json
{
  "party": "SME RODINA"
}
```

<h3 id="get_parties_results_elastic_get_parties_results_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[StatisticsPerPartyRequest](#schemastatisticsperpartyrequest)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_parties_results_elastic_get_parties_results_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Message](#schemamessage)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[Message](#schemamessage)|

<h3 id="get_parties_results_elastic_get_parties_results_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_parties_with_candidates_results_elastic_get_party_candidate_results_post

<a id="opIdget_parties_with_candidates_results_elastic_get_party_candidate_results_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/elastic/get-party-candidate-results', headers = headers)

print(r.json())

```

`POST /elastic/get-party-candidate-results`

*Get Parties With Candidates Results*

> Body parameter

```json
{
  "party": "SME RODINA"
}
```

<h3 id="get_parties_with_candidates_results_elastic_get_party_candidate_results_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[StatisticsPerPartyRequest](#schemastatisticsperpartyrequest)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_parties_with_candidates_results_elastic_get_party_candidate_results_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Message](#schemamessage)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[Message](#schemamessage)|

<h3 id="get_parties_with_candidates_results_elastic_get_party_candidate_results_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_candidates_results_elastic_get_candidates_results_post

<a id="opIdget_candidates_results_elastic_get_candidates_results_post"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/elastic/get-candidates-results', headers = headers)

print(r.json())

```

`POST /elastic/get-candidates-results`

*Get Candidates Results*

> Example responses

> 200 Response

```json
null
```

<h3 id="get_candidates_results_elastic_get_candidates_results_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Message](#schemamessage)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[Message](#schemamessage)|

<h3 id="get_candidates_results_elastic_get_candidates_results_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_resilts_by_locality_mongo_elastic_get_results_by_locality_mongo_get

<a id="opIdget_resilts_by_locality_mongo_elastic_get_results_by_locality_mongo_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/elastic/get-results-by-locality-mongo', headers = headers)

print(r.json())

```

`GET /elastic/get-results-by-locality-mongo`

*Get Resilts By Locality Mongo*

Used to provide benchmark for ES vs Mongo aggregation queries

> Example responses

> 200 Response

```json
null
```

<h3 id="get_resilts_by_locality_mongo_elastic_get_results_by_locality_mongo_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="get_resilts_by_locality_mongo_elastic_get_results_by_locality_mongo_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_results_by_locality_elastic_get_results_by_locality_post

<a id="opIdget_results_by_locality_elastic_get_results_by_locality_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/elastic/get-results-by-locality', headers = headers)

print(r.json())

```

`POST /elastic/get-results-by-locality`

*Get Results By Locality*

> Body parameter

```json
{
  "filter_by": "region_name",
  "filter_value": "Prešovský kraj"
}
```

<h3 id="get_results_by_locality_elastic_get_results_by_locality_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[StatisticsPerLocalityRequest](#schemastatisticsperlocalityrequest)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="get_results_by_locality_elastic_get_results_by_locality_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Message](#schemamessage)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[Message](#schemamessage)|

<h3 id="get_results_by_locality_elastic_get_results_by_locality_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

## get_elections_status_elastic_elections_status_get

<a id="opIdget_elections_status_elastic_elections_status_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/elastic/elections-status', headers = headers)

print(r.json())

```

`GET /elastic/elections-status`

*Get Elections Status*

> Example responses

> 200 Response

```json
null
```

<h3 id="get_elections_status_elastic_elections_status_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|400|[Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)|Bad Request|[Message](#schemamessage)|
|500|[Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1)|Internal Server Error|[Message](#schemamessage)|

<h3 id="get_elections_status_elastic_elections_status_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>    

