---
order: 300
---

# Inštalačná príručka

Systém Electie pozostáva z hardvérovej a softvérovej časti, pričom je možné ho spustiť ako celok navrhnutým spôsobom na poskytnutom hardvéri vo volebnej miestnosti alebo iba čisto ako softvérové komponenty na vlasntej infraštruktúre.


## Príprava pred voľbami

Pred každými voľbami je potrebné zabezpečiť niekoľko vecí.
 - prirpaviť konfiguračný súbor so zoznam kandidátov
 - pripraviť zoznam volebných miestností
 - rozdistribuovať verejné kľúče medzi gateway zariadeniami a serverom
 - nahrať novú konfiguráciu na gateway zariadenia

## Zapojenie zariadení vo volebnej miestnosti

![](/assets/images/voting-place-architecture.png)

Komisia vo volebnej miestnosti musí zapojiť zariadenia podľa zobrazenej schémy. V miestnosti existuje jeden router, ktorý môže, ale nemusí byť pripojený na internet. Router disponuje DHCP serverom.

### Gateway

V miestnosti je ďalej práve jeden gateway. Ten sa skladá z Raspberry Pi, NFC zapisovačky a dotykového displeja. Dotytkový displej sa pripája k Raspberry pomocou HMDI a USB. NFC zapisovačka je pripojená pomocou USB. Ethernetovým káblom je gateway pripojený k centrálnemu routeru. Po tomto všetkom je možné pripojiť Raspberry do elektrickej siete.


### Volebný terminál

Volebných terminálov môže byť v miestnosti 1 až N. Volebný terminál pozostáva z Raspberry Pi, dotykovej obrazovky, NFC čítačky a termotlačiarne. Obrazovka a čítačka sa pripájajú podobne ako na gateway-i. Rovnako ethernetom sa VT pripája k routeru. Tlačiareň by mala byť pripojená ethernetovým káblom priamo k Raspberry Pi s osobitným DHCP serverom, ale pre účely študentského dema postačuje pripojiť tlačiareň ethernetovým káblom priamo do toho istého routera. Po prepojení týchto komponentov je možné pridať elektrickú energiu.


### Server

Z pohľadu volebnej komisie je server nejaký black box v cloude. Na starosti ho majú špecializovaní pracovníci verejnej správy. Aby volebné miestnosti mohli komunikovať s týmto serverom, potrebujú mať v gateway-och správne nakonfigurovanú jeho adresu.


## Inštalaácia systému na vlastnej architektúre

V kontexte spúšťania nášho systému na vlastnej architektúre, či už pri reálnom použití alebo pri ďalšej študentskej práci na projekte, podrobnejšie technické detaily sú potrebné.

### Technológie

Všetky API backendy bežia v Pythone na FastAPI frameworku. Používame Python verzie 3.10. Frontendy webových aplikácií sú u nás single page aplikácie vo frameworku Svelte. Na serveri a gateway-i používame MongoDB databázu. Pre poskytovanie finálnych štatistík existuje ešte na serveri aj inštancia ElasticSearch-u.

Naše riešenie postavené na oddelených kontajneroch, ktoré je možné inak označiť ako mikroslužby. Každý kúsok softvéru má svoj kontajner a teda nič nie je potrebné spúšťať lokálne priamo na počítači. Gateway, VT aj server sa skaldajú z viacerých služieb, ktoré je potrebné spúšťať istým spôsobom spolu. Preto je pre každú túto časť vytvorený docker-compose súbor, ktorý predpisuje požadovanú orchestráciu jednotlivých kontajnerov. Všetky časti riešenia je zaručene možné spustiť na amd64 aj arm64 architektúrach.

Je potrebné mať nainštalovaný Docker verzie aspoň `19.03` a Docker Compose aspoň `1.25.5`. V optimálnych prípadoch stačí v koreni repozritára zavolať príkaz podobný nasledovnému:

```
docker-compose up -d
```

Pre lepšie pochopenie a zorientovanie sa v aplikáciách odporúčame sa všeobecne popozerať do docker-compose súborov, Dockerfilov a start.sh skriptov, z ktorých je možné sa dozvedieť ďalšie detaily o premenných prostredia, orchestrácii a jednotlivých kontajneroch.

Nižšie úvádzamé najzákladnejší spôsob spustenia jednotlivých komponentov z koreňov repozitárov. Pre detailnejšie informácie pozri dokumentáciu jednotlivých častí.


### Server

```
docker compose up -d --build
```

Server by mal byť dostupný na [http://localhost:8222/](http://localhost:8222/). Overte cez [http://localhost:8222/docs](http://localhost:8222/docs)

[Viac tu](../server/installation)


### Gateway

```
docker-compose up -d --build
```

Gateway by mal byť dostupný na [http://localhost:8080/](http://localhost:8080/).

Jeho služby sú ale až na subpath-och:


| Služba | Cesta |
| --- | --- |
| Voting service | `localhost:8080/voting-service-api/` |
| Synchronization service | `localhost:8080/synchronization-service-api/` |
| Voting process manager | `localhost:8080/voting-process-manager-api/` |
| Token manager | `localhost:8080/token-manager-api/` |
| State vector | `localhost:8080/statevector/` |


[Viac tu](../gateway/installation)


### Volebný terminál

__Pozor: Aby sa VT dokázal zaregistrovať a spustiť, je potrebné v gateway adminovi v časti "Volebné terminály" spustiť registráciu volebných terminálov. (PIN je defaultne 0000)__

```
docker-compose up -d --build
```

Volebný terminál by mal byť dostupný na [http://localhost:81/](http://localhost:81/)

[Viac tu](../voting_terminal/installation)

