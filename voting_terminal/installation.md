# Inštalácia

## Vybrané premenné prostredia

_Tieto je možné nastaviť v `docker-compose.yml`_

| ENV | Význam |
| --- | --- |
| VT_ONLY_DEV | Ak `==1` Gateway nie je potrebný a komunikácia s ním bude ignorovaná |
| DONT_WAIT_FOR_TOKEN | Ak `==1` obrazovka sa automaticky aktivuje falošným tagom po chvíľke nečinnosti |


## Gateway by mal bežať, aby bolo všetko ok

`datamodel.yaml` je stiahnutý z gateway-a a pregenerovaný do `src/schemas/votes.py` predtým ako sa rozbehne backend. Gateway by mal spustený, aby sa podarilo stiahnuť tento konfigurák. Ak je nastavená premenná VT_ONLY_DEV, malo by to byť ok aj bez G.

Druhou vecou je, že VT po spustení získa od G svoje `id` a G `public_key`.


## Klasické spustenie Dockeru
```
docker-compose up -d --build
```

### Bez Gateway

V `docker-compose.yml` zmeňte environment variable `VT_ONLY_DEV` na `0` ak chcete reálne komunikovať s G, ako je požadované v reálnej produkcii.

Defaultne je to `1` takže G nie je potrebný.


## Spúštanie testov
```
docker-compose -f docker-compose.test.backend.yml up --build
```


## Porty

VT beží na porte `81` defaultne. To sa dá zmeniť v `docker-compose.yml`.

Backend je na subpathe `/backend` a Fast API GUI je možné vidieť na `/backend/docs` (celá path: `http://localhost:81/backend/docs`)

Fronetd je na subpath (`http://localhost:81/frontend/`).
