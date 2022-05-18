---
order: 500
---

# Všeobecný pohľad

Súčasný systém volieb čelí problémom ako pomalé manuálne sčítanie hlasov, vysoké organizačné náklady, je náchylný na chyby spôsobené ľudským faktorom a občas chýba dôvera širokej verejnosti. Digitalizované volebné systémy by výrazne znížili náklady na voľby, čas potrebný na finalizáciu výsledkov, spotrebu papiera a eliminovali ľudský vstup do sčítania hlasov. Preto náš tím Electie prichádza s inovatívnou vízou pre elektronizáciu volebného procesu. Hlasovacie hárky sme nahradili dotykovými obrazovkami, vďaka čomu je možné hlasy zbierať a sčítavať automatizovane.

## Volebný proces

![](/assets/images/voting_process.png)

Z pohľadu voliča sa samotný proces hlasovania zásadne nemení v porovnaní s tradičným spôsobom. Volič príde do volebnej miestnosti a podrobí sa overeniu identity členom komisie. Namiesto obdržania veľkého množstva papierov s kandidátmi dostane volič NFC tag určený na autorizáciu pri volebnom termináli. Volič pristúpi k volebnému terminálu a priloží NFC tag ku čítačke a po úspešnej autorizácii je odomknutá volebná aplikácia. Veľký dotykový displej zobrazuje zoznam dostupných kandidátov. Volič môže vyhľadávať kandidátov podľa mena, prechádzať stránkami v zozname strán a vyberať preferovaných kandidátov. Volič musí potvrdiť svoju voľbu v každom medzikroku a na konci po zobrazení sumáru hlasovania opäť potvrdiť svoj výber.

Taktiež je možné odovzdať aj prázdny hlas ako to je možné pri klasických voľbách. Volebný terminál informuje voliča o úspechu voľby a vytlačí potvrdenie o hlasovaní (malý papier, ktorý obsahuje QR kód pre možnosť offline sčítania hlasov). Následne volič vhodí potvrdenie do volebnej urny a hlasovací proces je z pohľadu voliča ukončený.


## Životný cyklus hlasu

Dáta reprezentujúce hlas voliča v JSON formáte sú odoslané na backend terminálu, kde sa overí platnosť voličovho autorizačného tokenu a následne je potvrdený aj jeho hlas. Šifrovaný hlas spolu s identifikátorom volebného terminálu a autorizačným tokenom voliča je odoslaný na gateway, kde sa spracuje. Voting Service dešifruje hlas kľúčom daného volebného terminálu a následne overí platnosť autorizačného tokenu. Ak je token platný, hlas sa uloží do databázy a je vrátená správa o úspešnom spracovaní požiadavky. Akonáhle terminál prijme odpoveď, tlačiareň vytlačí potvrdzujúci doklad (malý papier) s podrobnosťami o hlasovaní a QR kódom.

![](/assets/images/vote_lifecycle.png)

Po odhlasovaní je použitý autorizačný token deaktivovaný, takže s ním nie je možné znova hlasovať. Ak je gateway pripojený k internetu, Synchronization service začne odosielať šifrované hlasy na hlavný server v pravidelných intervaloch. Hlasy sú potom spracované na serveri službou Voting service, kde sa dešifrujú hlasy pomocou príslušných kľúčov a ak je elektronický podpis platný, hlas je uložený do hlavnej databázy. Hlavný server pravidelne reindexuje nové hlasy pomocou technológie ElasticSearch pre efektívne získavanie štatistík a umožnenie rôznych dopytov nad výsledkami.

Konečné výsledky sú k dispozícii hneď ako všetky gateway-e zosynchronizujú všetky svoje hlasy. Naše riešenie sme pripravili na veľké množstvo návštevníkov, preto je dopytovanie nad výsledkami vykonávané pomocou ElasticSearch-u. Táto technológia podporuje distribuované výpočty a je vysoko škálovateľná. Používateľom ponúkame vizualizáciu výsledkov volieb podľa krajov a okresov Slovenska a taktiež je možné vidieť aj rozdelenie kresiel pre strany v parlamente.

Používatelia môžu tiež zadávať vlastné dopyty filtrovaním konkrétneho mesta, regiónu, alebo iného geografického členenia. Zároveň je možné poskytovať čiastkové výsledky volieb aj pokým ešte nie sú ukončené, ak to individuálny prípad použitia umožňuje.

