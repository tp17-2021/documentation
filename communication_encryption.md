---
order: 400
---

# Bezpečnosť a šifrovanie

Bezpečnosť je vo voľbách, najmä v elektronických, prakticky najdôležitejším prvkom. Porušenie integrity volieb môže viesť k zmene výsledkov a v dôsledku toho k zvoleniu nesprávnych kandidátov. Takéto bezpečnostné incidenty by spravili riešenie prakticky nepoužiteľným a reputačne by zrujnovali jeho tvorcov. Preto je potrebné dostatočne dbať na bezpečnosť.

Naše riešenie zahŕňa jeden centrálny server, na ktorý sú hlasy z gateway-ov sú odosielané cez verejnú internetovú sieť. Práve táto časť komunikácie predstavuje najzraniteľnejší článok v celom volebnom procese. Existuje tu možnosť, že potenciálny útočník by túto komunikáciu odychytil a následne by bol schopný prečítať odosielané hlasy alebo v horšom prípade ich nahradiť inými.

Preto sme navhrli a implementovali vlasntý šifrovací a podpisovací protokol. Rozhodli sme sa použiť 4096bit RSA a 256bit AES algoritmy na šifrovanie prenášaných hlasov. Samotné hlasy sú zašifrované pomocou symetrického kľúča AES, ktorý je potom zašifrovaný verejným kľúčom RSA hlavného serveru. Hlasy sú tiež podpísané privátnym RSA kľúčom gateway-a, ktorý zabezpečí, že počas prenosu na server dáta nemôžu byť zmenené bez toho, aby to server zistil pri validácii podpisu.

## Nástrahy RSA

Pri RSA kľúčoch je potrebné zabezpečiť, aby privátny kľúč zariadenia nebol nikdy nikde zverejnený. V tom prípade je prakticky nemožné ho náhodne uhádnuť a sfalšovať správu.
Algoritmus AES sa používa kvôli jeho rýchlosti a schopnosti šifrovať správy neobmedzenej dĺžky a je v súčasnosti priemyselným štandardom.

Výmena kľúčov je najdôležitejšou súčasťou RSA šifrovania. Pri výmene verejných kľúčov po verjenej sieti je teoreticky možný man-in-the-middle útok, kedy komunikácia prechádza cez nejaký napadnutý uzol, v ktorom útočník odchytí verejné kľúče, tie si zapamätá a reálnym zariadeniam pošle vlastné kľúče bez toho, aby to zariadenia mohli odhaliť. Výmena verejných kľúčov sa u nás vykonáva ešte počas procesu konfigurácie gateway-a autorizovaným personálom pred voľbami v špecializovaných krajských volebných centrálach. Tu môže zapríčiniť chybu iba ľudský faktor, čo sa rovanko môže stať aj pri doteraz zaužívanom spôsobe volieb.

## Vlastná knižnica

![](/assets/images/encryption.png)

Pre každý gateway existuje iný RSA pár, čo znamená, že aj v prípade odhalenia jedného kľúča zostáva integrita volieb pomerne neporušená. Implementovali sme [vlastnú knižnicu](https://pypi.org/project/electiersa/) v Pythone, ktorá poskytuje hlavne dve metódy - šifrovanie a dešifrovanie správy. Tieto metódy potrebujú privátny kľúč lokálneho zariadenia, verejný kľúč opačného zariadenia a ID opačného zariadenia. Na základe tohto sa hlas podpíše, zašifruje AES kľúčom, AES kľúč sa zašifruje verejným RSA kľúčom, pribalí sa do finálnej správy a môže sa odoslať. Na opačnom zariadení sú tieto operácie vykonané opačne.

## Volebná miestnosť

Rovnaký proces šifrovania sa používa aj vo vnútri lokálnej siete s volebnými terminálmi. Všetka komunikácia medzi volebnými terminálmi a gateway-om prebieha len po lokálnej sieti realizovanej fyzickými káblami, ktoré má pod kontrolou volebná komisia v miestnosti. Keby sa i napriek tomu útočník pokúsil pripojiť k sieti a odoslať falošný hlas, nemal by platný privátny kľúč volebného terminálu, takže jeho pokus o útok by zlyhal pri overovaní hlasu, hlas by nebol prijatý.
