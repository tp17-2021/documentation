# Inštalácia

## Vybrané premenné prostredia

Tieto je možné nastaviť v _`docker-compose.yml`_.

| ENV | Význam |
| --- | --- |
| VT_ONLY_DEV | Ak je nastavená hodnota `1`, gateway nie je potrebný a komunikácia s ním bude ignorovaná |
| DONT_WAIT_FOR_TOKEN | Ak je nastavená hodnota `1`, obrazovka sa automaticky aktivuje falošným tagom po chvíľke nečinnosti |


## Potreba spustenia gateway-a

`datamodel.yaml` je stiahnutý z gateway-a a pregenerovaný do `src/schemas/votes.py`, predtým ako sa rozbehne backend. Gateway by mal spustený, aby sa podarilo stiahnúť tento konfiguračný súbor. Ak je nastavená premenná VT_ONLY_DEV, malo by to byť ok aj bez gateway-a.

VT po spustení získa od gateway-a svoje `ID` a `public_key` gateway-a.


## Spustenie v dockeri
```
docker-compose up -d --build
```

### Bez gateway-a

V `docker-compose.yml` zmeňte premennú prostredia `VT_ONLY_DEV` na `0`, ak chcete reálne komunikovať s gateway-om, ako je požadované v produkcii. Default nastavenie je na `1`, takže gateway nie je potrebný.


## Spúštanie testov
```
docker-compose -f docker-compose.test.backend.yml up --build
```

## Nastavenia

Volebný terminál beží defaultne na porte `81`. To sa dá zmeniť v `docker-compose.yml`.

Backend je na subpath `/backend` a API špecifikáciu je možné vidieť na `/backend/docs` (celá path: `http://localhost:81/backend/docs`).

Fronetd je dostupný na (`http://localhost:81/frontend/`).
