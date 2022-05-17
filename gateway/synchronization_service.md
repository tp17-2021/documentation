# Synchronization service

Služba je zodpovedná za sychronizáciu hlasov medzi gateway-om a serverom. Služba je implementovaná ako REST API v knižnici
[Fast API](https://fastapi.tiangolo.com/).

Služba pracuje z hlasmi v lokálnej Mongo databáze, ktoré boli vložené pomocou [Voting service](voting_service.md). Hlasy sa synchronizujú po dávkach (prednastavená hodnota je 10) a po zaširovaní sa posielajú pomocou HTTP požiadavky na endpoint [servera](../server/modules/voting.md), ktorý ich zvaliduje. Synchronizácia prebehne úspešne iba ak sú všetky hlasy v poriadku prijaté. Úspešne synchronizované hlasy označí ako `{"synchronized": true}`.

Synchronizácia prebieha na pozadí v intervale každú minútu (implementované pomocou [Fast API Utils Repeated Tasks](https://fastapi-utils.davidmontague.xyz/user-guide/repeated-tasks/)). Dá sa však spustiť aj manuálne pomocou endpointu `POST /api/synchronize`, ktorý je popísaný nižšie.

## Štruktúra posielaných hlasov

Hlasy sú posielané v HTTP požiadavke, ktorú tvorí json s id volebnej miestnosti a hlasmi, ktoré sú zašifrované ako pole zašifrovaných hlasov pomocou knižnice [*rsaelectie*](../communication_encryption), funkcie `encrypt_vote`.

``` json
  {
    "polling_place_id": 0,
    "votes": [
      {
        "encrypted_message": "string",
        "encrypted_object": "string"
      }
    ]
  }
```



## Popis API

### root__get

<a id="opIdroot__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/gateway/synchronization-service-api/', headers = headers)

print(r.json())

```

`GET /`

*Root*

Simple hello message. 

> Example responses

> 200 Response

```json
null
```

<h4 id="root__get-responses">Responses</h4>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h4 id="root__get-responseschema">Response Schema</h4>

<aside class="success">
This operation does not require authentication
</aside>

### synchronize_synchronize_post

<a id="opIdsynchronize_synchronize_post"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/gateway/synchronization-service-api/synchronize', headers = headers)

print(r.json())

```

`POST /synchronize`

*Synchronize*

Try to send local votes to server and updates local status.
If server response is different than 200, response has status 500 with error from server.

> Example responses

> 200 Response

```json
null
```

<h4 id="synchronize_synchronize_post-responses">Responses</h4>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h4 id="synchronize_synchronize_post-responseschema">Response Schema</h4>

<aside class="success">
This operation does not require authentication
</aside>

### statistics_statistics_post

<a id="opIdstatistics_statistics_post"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/gateway/synchronization-service-api/statistics', headers = headers)

print(r.json())

```

`POST /statistics`

*Statistics*

Provide statistics of votes in gateway database. Count of synchronized and unsynchronized votes.

> Example responses

> 200 Response

```json
null
```

<h4 id="statistics_statistics_post-responses">Responses</h4>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h4 id="statistics_statistics_post-responseschema">Response Schema</h4>

<aside class="success">
This operation does not require authentication
</aside>

### seed_seed_post

<a id="opIdseed_seed_post"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/gateway/synchronization-service-api/seed', headers = headers)

print(r.json())

```

`POST /seed`

*Seed*

Insert 10 unsynced dummy votes into gataway local gatabase. 

> Example responses

> 200 Response

```json
null
```

<h4 id="seed_seed_post-responses">Responses</h4>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h4 id="seed_seed_post-responseschema">Response Schema</h4>

<aside class="success">
This operation does not require authentication
</aside>

### test_encrypt_test_encrypt_get

<a id="opIdtest_encrypt_test_encrypt_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/gateway/synchronization-service-api/test-encrypt', headers = headers)

print(r.json())

```

`GET /test-encrypt`

*Test Encrypt*

Get a batch of encrypted votes. 

> Example responses

> 200 Response

```json
null
```

<h4 id="test_encrypt_test_encrypt_get-responses">Responses</h4>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h4 id="test_encrypt_test_encrypt_get-responseschema">Response Schema</h4>

<aside class="success">
This operation does not require authentication
</aside>