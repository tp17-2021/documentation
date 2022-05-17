# Inštalácia

## How to run it

```
docker-compose up -d --build
```

Toto implicitne používa základný súbor: `docker-compose.yml` s rozšírením o `docker-compose.override.yml`.

Gateway by mal byť dostupný na [http://localhost:8080/](http://localhost:8080/).

Jeho služby sú ale až na subpathoch:


| Služba | Cesta |
| --- | --- |
| Voting service | `localhost:8080/voting-service-api/` |
| Synchronization service | `localhost:8080/synchronization-service-api/` |
| Voting process manager | `localhost:8080/voting-process-manager-api/` |
| Token manager | `localhost:8080/token-manager-api/` |
| State vector | `localhost:8080/statevector/` |
| _config.json_ | `localhost:8080/statevector/config/config.json` |
| _datamodels.yaml_ | `localhost:8080/statevector/config/datamodels.yaml` |



Nepovinný `-p` flag určuje prefix pre názvy kontajnerov v celom orchestri. Inak je prefix daný podľa root adresára. Napr. `docker-compose -p g up -d --build` prefixne všetky kontajnery písmenom `g` namiesto dlhšieho `gateway`.

### Pro tip

Kontajnery a virtuálne siete je možné ľahko zahodiť commandom `down`. Pre základné spustenie stačí zavolať toto v `gateway/` adresári:

```
docker-compose down
```

Alebo špecifikovať `project-name` daného composu:

```
docker-compose -p gtest-sync down
```


## Testovanie

Každá alužba má v sebe `test.env` súbor. Zaovlajú sa napr takto (príklad pre synchronization-service):

```
docker-compose --env-file synchronization-service/test.env up --build --exit-code-from synchronization-service --renew-anon-volumes
```

Kratšie sa dá:

```
docker-compose --env-file synchronization-service/test.env up --build --renew-anon-volumes
```
