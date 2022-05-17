---
order: 199
---
# Databáza
Server používa na ukladanie dát dokumentovú databázu MongoDB. Aj keď je do MongoDB vkladať dáta s rôznymi atribútmi, používame modely jednoitlivých dátových entít, ktoré špecifikujú štruktúru objektu a definujú typy jeho atribútov. Pracujeme s nasledujúcimi kolekciami:
- votes
- parties
- candidates
- polling_places
- key_pairs

Štruktúra uloženého hlasu:
```python
class Vote(BaseModel):
    token: str
    party_id: Optional[int] = None
    election_id: str
    candidate_ids: List[int] = []
```
Dátová štruktúra hlasu obsahuje referenciu na . Ďalej sa počas spracovania hlasov dynamicky pridajú dva atribúty a to:

```python
polling_place_id: int
synchronized: bool
```
Atribút polling_place_id slúži na spojenie hlasu s miestnosťou, v ktorej bol zvolený a atribút synchronized, ktorý indikuje, či bol daný hlas už zandexovaný do Elastic Searchu.



Štruktúra politickej strany:
```python
class Party(BaseModel):
    id: int = Field(..., alias="_id")
    party_number: int
    name: str
    official_abbr: str
    abbr: str
    image: str
    image_bytes: str
    color: str
    candidates: List[Candidate] = []
```
Dátová štruktúra politickej strany obsahuje základné údaje ako názov, skratka a číslo a doplnkové údaje ako farba a logo, ktoré sa používajú v štatistickej aplikácii. Ďalej strana obsahuje zoznam kadidátov, ktorý sú reprezentovaný vlastným modelom.

Štruktúra volebnej miestnosti:
```python
class PollingPlace(BaseModel):
    id: int = Field(..., alias="_id")
    region_code: int
    region_name: str
    administrative_area_code: int
    administrative_area_name: str
    county_code: int
    county_name: str
    municipality_code: int
    municipality_name: str
    polling_place_number: int
    registered_voters_count: int
```
Dátová štruktúra volebnej miestnosti obsahuje ifnormácie o územných celkoch, v ktorých sa daná miestnosť nachádza. Tieto údaje budú následne použité na prepočítavanie výslekov pre rôzne lokality (obce, okresy a kraje).

Štruktúra kandidáta:
```python
class Candidate(BaseModel):
    id: int = Field(..., alias="_id")
    party_number: int
    order: int
    first_name: str
    last_name: str
    degrees_before: str
    age: int
    occupation: str
    residence: str
```
Dátová štruktúra kandidáta obsahuje základné údaje o kandidátovy, ktoré sú použité na zobrazovanie výsledkov a obsahuje taktiež prepojenie na politickú stranu, ktorej je súčasťou.

Štruktúra kľúčového páru:
```python
class KeyPair(BaseModel):
    id: int = Field(..., alias="_id")
    polling_place_id: int
    private_key_pem: str
    public_key_pem: str
    g_private_key_pem: str
    g_public_key_pem: str
```
Kľúčový pár je špecifický pre každú volebnú meistnosť a jeho privátnym kľúčom je dešifrovaná iba kominikácia, ktorá prichádza z tejto volebnej miestnosti. Tento krok zvyšuje bezpečnosť komunikácie.
