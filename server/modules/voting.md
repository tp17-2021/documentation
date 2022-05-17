---
order: 195
---
# Hlasovanie

Základná myšlienka hlasovania spočíva vo validácii prichádzajúceho zoznamu hlasov z gateway-u. 



 a jeho následného uloženia do databázy. Prichádzajúci hlas musí prejsť niekoľkými validačnými krokmi, ktorými sú:
- validácia id volebnej miestnosti
- validácia samotného šifrovania
- validácia počtu kandidátov
- validácia duplicitných kandidátov
- validácia nezadanej politickej strany
- validácia nevhodného kandidáta pre politickú stranu
- validácia duplicitnej kombinácie tokenu a id politickej strany
- validácia duplicitných tokenov v zozname
- validácia id volieb



todo
- na co sluzi hlasovanie
- aka je zivotnost hlasu - flow
- ako hlas vyzera
- co sa s nim robi, cez ake vsetky validacie musi prejst
- co sa robi / ako vyzera hlas v pripade, ze padne na nejake validacii
- co sa robi / ako vyzera hlas v pripade ze hlas prejde na validacii