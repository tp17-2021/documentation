---
order: 140
---

# Gateway

Gataway je zariadenie nachádzajúce sa vo velebnej miestnosti. V miestnosti sa nachádza vždy len jeden gateway. Zabezpečuje komunikáciu medzi volebnými terminálmi a serverom. Gateway obsahuje lokálnu databázu pre hlasy aj tokeny, takže dokáže fungovať aj bez pripojenia k internetu a vie urobiť synchronizáciu na inom mieste, kde je internet dostupný.

Gataway sa má nachádzať na chránenom mieste a pristupovať k nemu smú iba členovia volebnej komisie napríklad pri spustení alebo zastavení volieb alebo nahrávaní tokenov na NFC tagy.

## Architektúra
popis architektury
![](/assets/images/gateway/architecture.png)

## Mikroslužby a ich smerovanie

V nasledujúcej tabuľke uvádzame zoznam mikroslužieb a statických súborv na gateway-i a ich smerovanie.

| Service | Path |
| --- | --- |
| Voting service | `/voting-service-api/` |
| Synchronization service | `/synchronization-service-api/` |
| Voting process manager | `/voting-process-manager-api/` |
| Token manager | `/token-manager-api/` |
| State vector | `/statevector/` |
| _config.json_ | `/statevector/config/config.json` |
| _datamodels.yaml_ | `/statevector/config/datamodels.yaml` |
