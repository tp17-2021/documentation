# Zariadenia vo volebnej miestnosti
Vo volebnej miestnosti sa nachádza gateway a viaceré volebné terminály pripojené na gateway ethernetovým káblom. Gateway komunikuje s jediným centrálnym serverom, vykonáva synchronizáciu hlasov.

![](/assets/images/polling_place_devices.png)

Volebný terminál pozostáva z 22 palcovej LCD dotykovej obrazovky, na ktorej je voličovi umožnené voliť. Obrazovka je pripojená k Raspberry Pi, ktoré komunikuje s NFC čítačkou pre umožnenie autorizácie pomocou autorizačných tokenov nahraných na NFC tagoch. Ďalej komunikuje s termo-tlačiarňou, ktorá umožňuje tlač potvrdenia o voľbe.

Gateway umožňuje manažovať celú volebnú miestnosť s terminálmi. Ako jediné zariadenie komunikuje priamo s centrálnym serverom cez internet. Skladá sa z Raspberry Pi, ktoré hostuje všetky mikroslužby manažujúce priebeh volieb. Ku gateway-u je pripojená malá dotyková obrazovka, ktorá slúži na prístup volebnej komisie k systému pre umožnenie riadenia priebehu volieb. Ku gateway-u je tiež pripojená NFC zapisovačka na zapisovanie generovaných autorizačných tokenov na tagy.

Hlavný server je zodpovedný za spracovanie hlasov zo všetkých gateway-ov do jednej databázy a vykonávanie štatistických výpočtov, vizualizáciu výsledkov
volieb.

Nastavenia pre jednotlivé voľby sú dané konfiguráciou.
