
## hello__get

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

## vote_api_vote_generated_post

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

## token_token_post

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

## receive_current_election_state_from_gateway_api_election_state_post

<a id="opIdreceive_current_election_state_from_gateway_api_election_state_post"></a>

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

<h3 id="receive_current_election_state_from_gateway_api_election_state_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|object|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="receive_current_election_state_from_gateway_api_election_state_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="receive_current_election_state_from_gateway_api_election_state_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

# Schemas

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

