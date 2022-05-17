---
order: 199
---
# Generovanie hlasov
Pre účely vývoja a testovania odporúčame generovať hlasy vo väčšom počte. Celý postup generovania spolu s naindexovaním prijatých hlasov dosiahnete vykonaním volaní v nasledujúcom poradí:
1. /database/import-data
2. /database/seed-votes (s počtom hlasov, ktoré sa majú vygenerovať)
3. /elastic/setup-elastic-vote-index (Elastic uzly musia byť pred týmto volaním funkčné, ak nie sú, skontrolujte prosím sekciu týkajúcu sa problému s malou pamäťou dockera.)
4. /elastic/synchronize-votes-es


V prípade potreby dogenerovania ďalších hlasov stačí vykonať kroky 2 a 4. 

Ak potrebujete vymazať existujúce hlasy len z Elastic Searchu stačí spustiť krok č. 3. 

V prípade potreby vymazania hlasov z MongoDB vykonajte príkazy 1 a 3.
