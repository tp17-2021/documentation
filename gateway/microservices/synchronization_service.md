# Synchronization service

Služba je zodpovedná za sychronizáciu hlasov medzi gateway-om a serverom. Služba je implementovaná ako REST API v knižnici
[Fast API](https://fastapi.tiangolo.com/).

Služba pracuje z hlasmi v lokálnej Mongo databáze, ktoré boli vložené pomocou [Voting service](voting_service.md). Hlasy sa synchronizujú po dávkach (prednastavená hodnota je 10) a po zaširovaní sa posielajú pomocou HTTP požiadavky na endpoint [servera](/server/server.md), ktorý ich zvaliduje. Synchronizácia prebehne úspešne iba ak sú všetky hlasy v poriadku prijaté. Úspešne synchronizované hlasy označí ako `{"synchronized": true}`.

Synchronizácia prebieha na pozadí v intervale každú minútu (implementované pomocou [Fast API Utils Repeated Tasks](https://fastapi-utils.davidmontague.xyz/user-guide/repeated-tasks/)). Dá sa však spustiť aj manuálne pomocou endpointu `POST /api/synchronize`, ktorý je popísaný nižšie.



## Popis API

### Spustenie synchronizácie

```http
POST /api/synchronize
```

Požiadavka spustí na pozadí proces synchronizácie. Synchronizácia sa vykonáva pokým nie sú zosynchronizované všetky hlasy.
Ak je odpoveď iná ako `200` zrejme je chyba na strane servera a odpoveď má kód `500`.

### Stav synchronizácie

```http
POST /api/statistics
```
Požiadavka poskytuje štatistiky o aktuálnom stave synchronizácie na gateway-i. Konkrétne počet synchronizovaných a nesynchronizovaných hlasov, čas poslednej synchronizácie a čas poslednej úspešnej synchronizácie.