---
order: 195
---
# Hlasovanie

Základná myšlienka hlasovania spočíva vo validácii prichádzajúceho zoznamu hlasov z gateway-u, ktorá musí prejsť niekoľkými krokmi. Samotný zoznam prichádzajúcich hlasov je zašifrovaný pomocou vlastnej knižnice *electiersa*, ktorého štruktúra je následovná:

```python
class VoteEncrypted(BaseModel):
    encrypted_message: str
    encrypted_object: str

class VotesEncrypted(BaseModel):
    polling_place_id: int
    votes: List[VoteEncrypted] = []
```

Ak je validácia úspešná, spomínaný zoznam prichádzajúcich hlasov sa uloží do kolekcie *votes* a informuje používateľa. V opačnom prípade, server vráti špecifickú hlášku, vďaka ktorej používateľ bude vedieť, v akom kroku bola validácia neúspešná. 

## Validácia
- *id* volebnej miestnosti sa musí nachádzať v kolekcii *key_pair*
- počet kandidátov nesmie byť väčší ako 5
- každý kandidát sa v prichádzajúcom hlase môže vyskytovať iba raz
- nezadaná politická strana nesmie obsahovať žiadneho kandidáta
- kandidát musí patriť do správne politickej strany
- v kolekcii *votes* sa nesmie nachádzať duplitcitná kombinácia tokenu a *id* volebnej miestnosti
- v príchádzajúcom zozname hlasov sa nesmie nachádzať duplicitný token
- *id* volieb musí byť totožné s tým, ktoré sa nachádza v konfiguračnom súbore *config.py*

