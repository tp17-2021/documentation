# Token manager

Služba je zodpovedná za generovanie, overovanie a deaktivovanie tokenov nahrávaných na NFC tagy. Služba rovnako ovláda a interaguje Token writter-om, ktorý sa stará o samostné nahranie tokenu na NFC tag.

Token je generovaný pomocou `uuid` bez znakov `-`, napríklad `858c0eb798a8475dbcf67e29ddb4966e`.

Deaktivovaný token je označený ako `{"active": false}`.

Aktivovaný a zapísaný token je označený ako `{"active": true}` a `{"written": true}`.

Token je považovaný ako platný iba ak je aktívny (`{"active": true}`).

## Komunikácia s frontendom
Token manager komunikuje s frontendovou aplikáciou pomocou websocketov. Používateľa informuje o stave zapisovačky o úspešnom alebo neúspešnom zapísaní tokenu alebo o možnosti nahrávania ďalšieho tokenu. Vo websockete sa posiela udalosť `writer_status`, ktorý nadobúda hodnoty  `off`, `idle`, `success`, `error`.

## Popis API

### Generovanie tokenu
Vygeneruje nový token a vráti ho v JSON formáte.

#### Požiadavka
```http
POST /tokens/create
```

#### Odpoveď
```json
{
    "status": "success",
    "token": "token"
}
```


### Validovanie tokenu
Skontroluje, či je zadaný token platný.
#### Požiadavka
```http
POST /tokens/validate
```
```json
{
    "token": "token"
}
```
#### Odpoveď
Vráti `403` ak token nie je platný, inak vráti `200`.

### Deaktivácia tokenu
Deaktivuje zadaný token.
#### Požiadavka
```http
POST /tokens/deactivate
```
```json
{
    "token": "token"
}
```
#### Odpoveď
Vráti `403` ak token nie je platný, inak vráti `200`.


### Vymazanie tokenu
Vymaže zadaný token.

#### Požiadavka
```http
DELETE /tokens/delete
```
```json
{
    "token": "token"
}
```
#### Odpoveď
Vráti `403` ak token nie je platný, inak vráti `200`.

### Aktivovanie NFC zapisovačky
Aktivuje NFC zapisovačku. Po zapnutí sa na zapisovačke zapne LED dióda.

```http
POST /tokens/writer/activate
```

### Deaktivovanie NFC zapisovačky
Deaktivuje NFC zapisovačku. LED dióda sa vypne.

```http
POST /tokens/writer/deactivate
```

### Vymazanie nezapísaných tokenov
Vymaže všetky nezapísané tokeny z databázy.

```http
POST /tokens/writer/delete
```

### Aktualizovanie zapísaného tokenu
Aktualizuje NFC tokene v databáze na `{"written": true}`.

```http
POST /tokens/writer/update
```
```json
{
    "token": "token"
}