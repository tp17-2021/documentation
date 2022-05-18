---
order: 140
---

# Gateway

Gataway je zariadenie nachádzajúce sa vo velebnej miestnosti. V miestnosti sa nachádza vždy len jeden gateway. Zabezpečuje komunikáciu medzi volebnými terminálmi a serverom. Gateway obsahuje lokálnu databázu pre hlasy aj tokeny, takže dokáže fungovať aj bez pripojenia k internetu a vie urobiť synchronizáciu na inom mieste, kde je internet dostupný.

Gataway sa má nachádzať na chránenom mieste a pristupovať k nemu smú iba členovia volebnej komisie napríklad pri spustení alebo zastavení volieb alebo nahrávaní autorizačných tokenov na NFC tagy.

## Architektúra

![](/assets/images/gateway/architecture.png)

Systém je rozdelený na niekoľko mikroslužieb. Konkrétne sú všetky realizované ako Docker kontajnery a orchestrované pomocou Docker Compose. Každá služba by mala mať na starosti jeden logický celok vo volebnom procese. Na obrázku je znázornená softvérová architektúra gateway-u s prepojeniami medzi mikroslužbami a popisom ich hlavných funkcií.

Nad tým všetkým je nasadený jeden __NGINX reverse proxy__, cez ktorý prichádza všetka komunikácia na gateway. Iba 3 služby sú volané mimo gateway-u a to __voting service__ pre prijímanie hlasov z volebných terminálov, __voting process manager__ pre obslužnú komunikáciu s volebnými terminálmi a __admin frontend__ bežiaci priamo na dotykovom displeji gateway-u. Cez internet so serverom komunikujú iba __synchornization service__ pre odosielanie hlasov a __report manager__ pre odosielanie zápisnice. __Token writer__ priamo komunikuje s USB NFC zapisovačkou, pomocou ktorej zapisuje nové tokeny na NFC tagy. O tieto tokeny sa pritom stará __token manager__. __Statevector__ je trochu atypická služba, ktorá iba uchováva stav niekoľkých atribútov a poskytuje ich ostatným službám. __Voting porcess manager__ je síce jeden kontajner, ale dali by sa z neho ešte oddeliť __local keys manager__, ktorý registruje a spravuje kľúče k terminálom v miestnosti, a __report manager__, ktorý má na starosti generovanie a distribúciu zápisnice. __Gateway DB__ je kontajner MongoDB, v ktorom beží niekoľko databáz.


## Mikroslužby a ich smerovanie

V nasledujúcej tabuľke uvádzame zoznam mikroslužieb a statických súborv na gateway-i a ich smerovanie za spomínaným reverse proxy.

| Service | Path |
| --- | --- |
| Voting service | `/voting-service-api/` |
| Synchronization service | `/synchronization-service-api/` |
| Voting process manager | `/voting-process-manager-api/` |
| Token manager | `/token-manager-api/` |
| State vector | `/statevector/` |
| _config.json_ | `/statevector/config/config.json` |
| _datamodels.yaml_ | `/statevector/config/datamodels.yaml` |
