# Inštalácia

## Spustenie v dockeri

```
docker-compose up -d --build
```

Implicitne sa používa základný súbor `docker-compose.yml` s rozšírením o `docker-compose.override.yml`.

Gateway by mal byť dostupný na [http://localhost:8080/](http://localhost:8080/).

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

Každá služba má v sebe `test.env` súbor. Zavolajú sa napr. takto (príklad pre synchronization-service):

```
docker-compose --env-file synchronization-service/test.env up --build --exit-code-from synchronization-service --renew-anon-volumes
```

Kratšie sa dá:

```
docker-compose --env-file synchronization-service/test.env up --build --renew-anon-volumes
```
