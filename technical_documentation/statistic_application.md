---
order: 110
---

# Štatistická aplikácia
Aplikácia bola naimplementovaná pomocou frameworku Svelte a je určená na zobrazovanie výsledkov volieb. Aplikácia ponúka množstvo typov zobrazenia výseldkov v grafických podobách a disponuje možnosťou filtrovania, či už podľa regiónu (obec, okres alebo kraj) alebo mena polického subjektu.

## Závislosti
Pre spustenie docker kontajnerov je potrebné mať nainstalované technológie Node, Git, Docker a Docker compose.
Pre účely vývoja ďalej odporúčame mať nainštalovaný nástroj na testovanie endpointov ako Postman alebo Insomnia.

## Spustenie
Svelte aplikáciu je možné spsutiť aj lokálne vykonaním príkazu:
```node
npm run dev
```
Po spustení bude aplikácia dostupná na adrese: ```http://localhost:5000```

Druhým spôsobom je spustenie pomocou orchestrátora docker-compose.

Prejdite do koreňového adresára štatistickej aplikácie a spustite nasledujúci príkaz:
```
docker compose up -d --build
```

Vybuildovaný kontaijner má premmenné prostredia potrebné pre napojenie na server a nasadenie kontajnera do celkového riešenia volebného systému.

## Nepublikované výsledky
Ak sa používateľovi zobrazuje modálne okno s hláškou o nepublikovaných dátach, je potrebné najprv zverejniť výsledky pomocou endpointu `/elastic/results/publish` na serveri. Tento endpoint však vyžaduje autorizáciu s použitím prihlasovacieho mena a hesla.
