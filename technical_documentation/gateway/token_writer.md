# Token writer

Služba zodpovedná za zapisovanie tokenu na Mifare 1k tag.

Zapisovanie funguje nasledovne:
- zapisovačka čaká, pokým sa Mifare tag nachádza v dosahu zapisovačky
- prečíta zo štvrtého bloku zapísané 128-bitové číslo
- pošle požiadavku na token manager na deaktiváciu prečítaného čísla
- pošle požiadavku na token manager na vygenerovanie nového 128-bitového čísla
- zapíše hodnotu na tag
- verifikuje zapísanú hodnotu jej prečítaním z tagu
- po úspešnej verifikácií pošle požiadavku na token manager o aktiváciu tokenu

Pre zamedzenie zapísania dvoch tokenov na jedno priloženie je vytvorený cooldown 30 sekúnd, ktorý v tejto dobe neumoží zapísať na rovnaký Mifare tag znova ďalší token.

Služba používa linuxový wrapper popísaný nižšie.

## Linuxový wrapper pre SL600-NFC zapisovačku

Implementované funkcionality:
- Vypnutie LED svetla
- Zapnutie LED svetka
- Čítanie z Mifare 1k tagu (štvrtý blok)
- Zápis na Mifare 1k tagu (štvrtý blok)
- Validácia zápisu

Ukážkový kód v knižnici zapíše náhodné 128-bitové číslo do štvrtého bloku Mifare 1k tagu, potom ho prečíta z neho a tým zvaliduje zápis. Ak všetko prebehne úspešne, program skončí.

Pre vývoj bez použitia dockera je potrebné nainštalovať závislosť pyusb:
```bash
pip3 install pyusb
```

Program musí bežať so sudo oprávneniami

Funguje iba na Linuxe (vo WSL 2 nekomunikuje s čítačkou). Testované na Ubuntu 20.04 a Ubuntu 22.04.