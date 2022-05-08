# Voting service

Služba zodpovedná za overovanie tokenu prichdádzajúceho a za prijímanie hlasu z voliebného terminálu.

## Popis API

### Prijatie hlasu

Prijme hlas z votebného terminálu, skontroluje platnosť tokenu, zaregistruje hlas v databáze a deaktivuje token, aby sa znemožnilo jeho použitie znovupoužitie.

```http
POST /api/vote
```

```json
{
    "vote": {},
    "token": "string"
}
```

## Overenie platnosti tokenu
Prijme token z volebného terminálu, skontroluje platnosť tokenu a vráti, či je token platný alebo nie.

```http
POST /api/token-validity
```
```json
{
    "token": "string"
}
```