---
order: 101
---
# Server
Server je centrálna jednotka na spracovanie hlasov z volebných miestností. Server po prijatí požiadavky na uloženie hlasov zabezpečí ich validáciu, následné spracovanie a uloženie. Po úspešnom vykonaní vráti odpoveď v ktorej špeifikuje koľko hlascov bolo spracovaným. Uložené hlasy sa priebežne indexujú do technlógie Elastic Search, z ktorej sú následne získavené pri volaní koncových bodov na získanie výsledkov a štatistík.
## Architektúra
popis architektury
![](/assets/images/server/architecture.png)
