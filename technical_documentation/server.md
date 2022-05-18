---
order: 120
---

# Server
Server je centrálna jednotka na spracovanie hlasov z volebných miestností. Server po prijatí požiadavky na uloženie hlasov zabezpečí ich validáciu, následné spracovanie a uloženie. Po úspešnom vykonaní vráti odpoveď v ktorej špecifikuje koľko hlascov bolo spracovaných. Uložené hlasy sa priebežne indexujú do technlógie ElasticSearch, z ktorej sú následne získavené pri volaní endpointov na získanie výsledkov a štatistík.

## Architektúra
![](/assets/images/server/server_architecture.png)
