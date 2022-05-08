# Voting process manager

Hlavná služba na gateway-i zodpovedná za spustenie a zastavenie volieb, registráciu volebných terminálov, poskytuje informáciu o stave pripojených terminálov a udalosti o spustení a zastavení volieb. Rovnako zabezpečuje generovanie zápisnice a odoslanie zápisnice na server.

## Registrácia volebného terminálu
Pri spustení volebného terminálu sa terminál dopytuje na endpoint `/register-vt` kedy sa pri spustenej registrácii vymení verejný kľúč gataway-a, aby mohla priebehať šifrovaná komunikácia medzi volebným terminálom a gateway-om. Ak registrácia nie je spustená vráti sa status `400`.


## Komunikácia medzi volebným terminálom
Táto služba komunikuje so všetkými registrovanými volebnými terminálmi pomocou websocketov. Vo websockete sa posiela udalosť `actual_state`, ktorý obsahuje aktuálny stav volieb volebným terminálom. Rovnako aj volebné terminály notifikujú gateway o ich aktuálnom stave udalosťou `vt_status`.

## Popis API

### Spustenie volieb
Spustí voľby a notifikuje všetky volebné terminály.

```http
POST /start
```


### Zastavenie volieb
Ukončí voľby a notifikuje všetky volebné terminály.

```http
POST /end
```

### Konfigurácia volieb
Vráti všetky potrebné texty z konfiguračného súboru pre frontend.

```http
GET /election-config
```

### Stav terminálov
Vráti informácie o stave všetkých pripojených voliebných terminálov.

```http
GET /terminals-status
```

### Udalosti volieb na gateway-i
Vráti zoznam všetkých udalostí o spustení a zastavení volieb na gateway-i.

```http
GET /gateway-elections-events
```

### Generovanie zápisnice
Vygeneruje závisnicu o voľbách a uloží ju do databázy vo formáte base64.

```http
POST /commission-paper/generate
```

```json
{
  "polling_place_id": 0,
  "participated_members": [
    {
      "name": "Jožko Mrkvička",
      "agree": true
    },
    {
      "name": "Ferko Mrkvička",
      "agree": false
    },
    {
      "name": "Jan Mrkvička",
      "agree": true
    }
  ],
  "president": {
    "name": "Jožko Hlavný",
    "agree": true
  }
}
```

### Získanie zápisnice
Vráti zápisnicu vo formáte base64.

```http
GET /commission-paper
```

### Odoslanie zápisnice
Odošle vygenerovanú zápisnicu na server.

```http
POST /commission-paper/send
```

