---
order: 100
---

## Závislosti
Pre spustenie docker kontajnerov je potrebné mať nainstalované technológie Docker, Docker compose.
Pre účely vývoja ďalej odporúčame mať nainštalovaný jazyk Python, nástroj na testovanie koncových bodov ako Postman alebo Insomnia a nástroj na manipuláciu s MongoDB ako napríklad MongoDB Compass.

Knižnice pythonu su definované v textovom súbore requirements.txt, ktoré si nainštalujete príkazom: 
```pip install -r requirements.txt```

## Spustenie
Lokálne samostatné spúšťanie jednotlivých častí potrebných pre chod serveru neodporúčame, z dôvodu radu problémov ktoré môžu vzniknúť. Najjednoduchším spôsobom je spustenie pomocou orchestrátora docker compose.

Prejdite do koreňového adresára servera a spustite nasledujúci príkaz.
```
docker compose up -d --build
```

After the build, you have two running services (MongoDB database and FastAPI server)

To see all available endpoints of the server navigate to: ```http://localhost:8222/docs```

## Ako si naimportovať skúšobné dáta a pripraviť Elastic Search cluster
V API docs špecifikácii spustite volania na jednotlivé koncové body v nasledovnom poradí:
1. /database/import-data
2. /database/seed-votes (s počtom hlasov, ktoré sa majú vygenerovať)
3. /elastic/setup-elastic-vote-index (Elastic uzly musia byť pred týmto volaním funkčné, ak nie sú, skontrolujte prosím sekciu týkajúcu sa problému s malou pamäťou dockera.)
4. /elastic/synchronize-votes-es (Synchronize votes in batches)

## Problém s Elastic search pamäťou
V prípade chybovej hlášky spomínajúcej prekročenie limitu pamäte, je potrebné nastaviť premmennú vm.max_map_count
v kerneli dockeru na najmenej 262144.

V závislosti od operačného systému použite jeden z nasledovných príkazov:
```
docker-machine ssh
sudo sysctl -w vm.max_map_count=262144

wsl -d docker-desktop
sysctl -w vm.max_map_count=262144
```

Na apple zariadeniach je možné toto nastavenie zmeniť priamo v nastaveniach Docker Desktop App v sekcii: Settings -> Resources -> Advanced -> Memory. 8Gb pamäte by malo postačovať.

## Testovanie vnútri dockeru
Jednotkové testovanie vykonávané v dockeri spustíte nasledovným príkazom v priečinku zdrojových kódov servera:
```
docker-compose -p test-server -f docker-compose.test.yml up --build --exit-code-from server --renew-anon-volumes 
```

Dostupné príznaky:
- -p                  - preped prefix to container names
- -f                  - docker-compose yml file
- --build             - build images if changed sources
- --exit-code-from    - get overall exit code from specified container
- --force-recreate    - recreate all containers
- --renew-anon-volumes - delete anonym volumens

Pre zastavenie kontajnerov použite príkaz:
```
docker-compose -f docker-compose.test.yml down
```