# Voting process manager

Hlavná služba na gateway-i zodpovedná za spustenie a zastavenie volieb, registráciu volebných terminálov, poskytuje informáciu o stave pripojených terminálov a udalosti o spustení a zastavení volieb. Rovnako zabezpečuje generovanie zápisnice a odoslanie zápisnice na server.

## Registrácia volebného terminálu
Pri spustení volebného terminálu sa terminál dopytuje na endpoint `/register-vt` kedy sa pri spustenej registrácii vymení verejný kľúč gataway-a, aby mohla priebehať šifrovaná komunikácia medzi volebným terminálom a gateway-om. Ak registrácia nie je spustená vráti sa status `400`.


## Komunikácia medzi volebným terminálom
Táto služba komunikuje so všetkými registrovanými volebnými terminálmi pomocou websocketov. Vo websockete sa posiela udalosť `actual_state`, ktorý obsahuje aktuálny stav volieb volebným terminálom. Rovnako aj volebné terminály notifikujú gateway o ich aktuálnom stave udalosťou `vt_status`.

## Popis API

### root__get

<a id="opIdroot__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/gateway/voting-process-manager-api/', headers = headers)

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

<h3 id="root__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="root__get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

### election_config_election_config_get

<a id="opIdelection_config_election_config_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/gateway/voting-process-manager-api/election-config', headers = headers)

print(r.json())

```

`GET /election-config`

*Election Config*

Returns necessary config fields for gateway from config. 

> Example responses

> 200 Response

```json
null
```

<h3 id="election_config_election_config_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="election_config_election_config_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

### terminals_status_terminals_status_get

<a id="opIdterminals_status_terminals_status_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/gateway/voting-process-manager-api/terminals-status', headers = headers)

print(r.json())

```

`GET /terminals-status`

*Terminals Status*

Returns necessary staus information of connected voting terminals.

> Example responses

> 200 Response

```json
null
```

<h3 id="terminals_status_terminals_status_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="terminals_status_terminals_status_get-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

### login_for_access_token_token_post

<a id="opIdlogin_for_access_token_token_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/x-www-form-urlencoded',
  'Accept': 'application/json'
}

r = requests.post('/gateway/voting-process-manager-api/token', headers = headers)

print(r.json())

```

`POST /token`

*Login For Access Token*

Log in user using username and password. 

> Body parameter

```yaml
grant_type: string
username: string
password: string
scope: ""
client_id: string
client_secret: string

```

<h3 id="login_for_access_token_token_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_login_for_access_token_token_post](#schemabody_login_for_access_token_token_post)|true|none|

> Example responses

> 200 Response

```json
{
  "access_token": "string",
  "token_type": "string"
}
```

<h3 id="login_for_access_token_token_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[Token](#schematoken)|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<aside class="success">
This operation does not require authentication
</aside>

### current_user_current_user__get

<a id="opIdcurrent_user_current_user__get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/gateway/voting-process-manager-api/current-user/', headers = headers)

print(r.json())

```

`GET /current-user/`

*Current User*

> Example responses

> 200 Response

```json
{
  "username": "string",
  "disabled": true
}
```

<h3 id="current_user_current_user__get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|[User](#schemauser)|

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

### start_voting_process_start_post

<a id="opIdstart_voting_process_start_post"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/gateway/voting-process-manager-api/start', headers = headers)

print(r.json())

```

`POST /start`

*Start Voting Process*

Starts elections and notify all voting terminals.

> Example responses

> 200 Response

```json
null
```

<h3 id="start_voting_process_start_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="start_voting_process_start_post-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

### end_voting_process_end_post

<a id="opIdend_voting_process_end_post"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.post('/gateway/voting-process-manager-api/end', headers = headers)

print(r.json())

```

`POST /end`

*End Voting Process*

Stops elections and notify all voting terminals.

> Example responses

> 200 Response

```json
null
```

<h3 id="end_voting_process_end_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="end_voting_process_end_post-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

### register_vt_register_vt_post

<a id="opIdregister_vt_register_vt_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/gateway/voting-process-manager-api/register-vt', headers = headers)

print(r.json())

```

`POST /register-vt`

*Register Vt*

Register a voting terminal.
Returns status 400 if registration is disabled else return status 200 with id and public key.

> Body parameter

```json
{
  "public_key": "string"
}
```

<h3 id="register_vt_register_vt_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[Body_register_vt_register_vt_post](#schemabody_register_vt_register_vt_post)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="register_vt_register_vt_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="register_vt_register_vt_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

### gateway_events_gateway_elections_events_get

<a id="opIdgateway_events_gateway_elections_events_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/gateway/voting-process-manager-api/gateway-elections-events', headers = headers)

print(r.json())

```

`GET /gateway-elections-events`

*Gateway Events*

Get all elections events of start and end of elections.

> Example responses

> 200 Response

```json
null
```

<h3 id="gateway_events_gateway_elections_events_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="gateway_events_gateway_elections_events_get-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

### get_first_start_gateway_elections_events_first_start_get

<a id="opIdget_first_start_gateway_elections_events_first_start_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/gateway/voting-process-manager-api/gateway-elections-events/first-start', headers = headers)

print(r.json())

```

`GET /gateway-elections-events/first-start`

*Get First Start*

Get first start of elections.

> Example responses

> 200 Response

```json
null
```

<h3 id="get_first_start_gateway_elections_events_first_start_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="get_first_start_gateway_elections_events_first_start_get-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

### get_last_end_gateway_elections_events_last_end_get

<a id="opIdget_last_end_gateway_elections_events_last_end_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer {access-token}'
}

r = requests.get('/gateway/voting-process-manager-api/gateway-elections-events/last-end', headers = headers)

print(r.json())

```

`GET /gateway-elections-events/last-end`

*Get Last End*

Get last end of elections.

> Example responses

> 200 Response

```json
null
```

<h3 id="get_last_end_gateway_elections_events_last_end_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="get_last_end_gateway_elections_events_last_end_get-responseschema">Response Schema</h3>

<aside class="warning">
To perform this operation, you must be authenticated by means of one of the following methods:
OAuth2PasswordBearer
</aside>

### generate_commission_paper_commission_paper_generate_post

<a id="opIdgenerate_commission_paper_commission_paper_generate_post"></a>

> Code samples

```python
import requests
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json'
}

r = requests.post('/gateway/voting-process-manager-api/commission-paper/generate', headers = headers)

print(r.json())

```

`POST /commission-paper/generate`

*Generate Commission Paper*

Generate commission paper in pdf format encoded in base64 and store it into database.

> Body parameter

```json
{
  "polling_place_id": 0,
  "participated_members": [
    {
      "name": "Jo�ko Mrkvi�ka",
      "agree": true
    },
    {
      "name": "Ferko Mrkvi�ka",
      "agree": false
    },
    {
      "name": "J�n Mrkvi�ka",
      "agree": true
    }
  ],
  "president": {
    "name": "Jo�ko Hlavn�",
    "agree": true
  }
}
```

<h3 id="generate_commission_paper_commission_paper_generate_post-parameters">Parameters</h3>

|Name|In|Type|Required|Description|
|---|---|---|---|---|
|body|body|[CommissionPaper](#schemacommissionpaper)|true|none|

> Example responses

> 200 Response

```json
null
```

<h3 id="generate_commission_paper_commission_paper_generate_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|
|422|[Unprocessable Entity](https://tools.ietf.org/html/rfc2518#section-10.3)|Validation Error|[HTTPValidationError](#schemahttpvalidationerror)|

<h3 id="generate_commission_paper_commission_paper_generate_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

### get_commission_paper_commission_paper_get

<a id="opIdget_commission_paper_commission_paper_get"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.get('/gateway/voting-process-manager-api/commission-paper', headers = headers)

print(r.json())

```

`GET /commission-paper`

*Get Commission Paper*

Get commission paper from database encoded in base64.

> Example responses

> 200 Response

```json
null
```

<h3 id="get_commission_paper_commission_paper_get-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="get_commission_paper_commission_paper_get-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

### send_commission_paper_commission_paper_send_post

<a id="opIdsend_commission_paper_commission_paper_send_post"></a>

> Code samples

```python
import requests
headers = {
  'Accept': 'application/json'
}

r = requests.post('/gateway/voting-process-manager-api/commission-paper/send', headers = headers)

print(r.json())

```

`POST /commission-paper/send`

*Send Commission Paper*

Send commission paper to server.

> Example responses

> 200 Response

```json
null
```

<h3 id="send_commission_paper_commission_paper_send_post-responses">Responses</h3>

|Status|Meaning|Description|Schema|
|---|---|---|---|
|200|[OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)|Successful Response|Inline|

<h3 id="send_commission_paper_commission_paper_send_post-responseschema">Response Schema</h3>

<aside class="success">
This operation does not require authentication
</aside>

### Schemas

#### Body_login_for_access_token_token_post
<!-- backwards compatibility -->
<a id="schemabody_login_for_access_token_token_post"></a>
<a id="schema_Body_login_for_access_token_token_post"></a>
<a id="tocSbody_login_for_access_token_token_post"></a>
<a id="tocsbody_login_for_access_token_token_post"></a>

```json
{
  "grant_type": "string",
  "username": "string",
  "password": "string",
  "scope": "",
  "client_id": "string",
  "client_secret": "string"
}

```

Body_login_for_access_token_token_post

##### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|grant_type|string|false|none|none|
|username|string|true|none|none|
|password|string|true|none|none|
|scope|string|false|none|none|
|client_id|string|false|none|none|
|client_secret|string|false|none|none|

#### Body_register_vt_register_vt_post
<!-- backwards compatibility -->
<a id="schemabody_register_vt_register_vt_post"></a>
<a id="schema_Body_register_vt_register_vt_post"></a>
<a id="tocSbody_register_vt_register_vt_post"></a>
<a id="tocsbody_register_vt_register_vt_post"></a>

```json
{
  "public_key": "string"
}

```

Body_register_vt_register_vt_post

##### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|public_key|string|true|none|none|

#### CommissionPaper
<!-- backwards compatibility -->
<a id="schemacommissionpaper"></a>
<a id="schema_CommissionPaper"></a>
<a id="tocScommissionpaper"></a>
<a id="tocscommissionpaper"></a>

```json
{
  "polling_place_id": 0,
  "participated_members": [
    {
      "name": "Jožko Mrkvička",
      "agree": true
    },
    {
      "name": "Ferko Mrkvička",
      "agree": false
    },
    {
      "name": "Ján Mrkvička",
      "agree": true
    }
  ],
  "president": {
    "name": "Jožko Hlavný",
    "agree": true
  }
}

```

CommissionPaper

##### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|polling_place_id|integer|true|none|none|
|participated_members|[[Member](#schemamember)]|false|none|none|
|president|[Member](#schemamember)|true|none|none|

#### HTTPValidationError
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

##### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|detail|[[ValidationError](#schemavalidationerror)]|false|none|none|

#### Member
<!-- backwards compatibility -->
<a id="schemamember"></a>
<a id="schema_Member"></a>
<a id="tocSmember"></a>
<a id="tocsmember"></a>

```json
{
  "name": "string",
  "agree": true
}

```

Member

##### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|name|string|true|none|none|
|agree|boolean|true|none|none|

#### Token
<!-- backwards compatibility -->
<a id="schematoken"></a>
<a id="schema_Token"></a>
<a id="tocStoken"></a>
<a id="tocstoken"></a>

```json
{
  "access_token": "string",
  "token_type": "string"
}

```

Token

##### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|access_token|string|true|none|none|
|token_type|string|true|none|none|

#### User
<!-- backwards compatibility -->
<a id="schemauser"></a>
<a id="schema_User"></a>
<a id="tocSuser"></a>
<a id="tocsuser"></a>

```json
{
  "username": "string",
  "disabled": true
}

```

User

##### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|username|string|true|none|none|
|disabled|boolean|false|none|none|

#### ValidationError
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

##### Properties

|Name|Type|Required|Restrictions|Description|
|---|---|---|---|---|
|loc|[string]|true|none|none|
|msg|string|true|none|none|
|type|string|true|none|none|