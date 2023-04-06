baslik= "HABERİNİZ OLSUN"
vade = 12
faizOrani1= 1.47
faizOrani2=1.44
faizOrani=1.47
print(baslik)
print(type(baslik))
print(type(vade))
print(type(faizOrani))
mesaj = "Hoşgeldin"
müsteriAdi= "Buse"
müsteriSoyadi= "Bebütoğlu"
sonucMesaj = mesaj + " " + müsteriAdi + " " + müsteriSoyadi + "!"
print(sonucMesaj)

sayi1 = 10
sayi2 = 20
print(sayi1 + sayi2)

dolarDun = 7.65
dolarBugun = 7.75

if  dolarDun > dolarBugun:
    print("Azalış oku")
elif dolarDun < dolarBugun:
    print("Artış oku")
else:
    print("Eşittir")

krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan Alanlara Özel","Mutlu Emekli İhtiyaç Kredisi"]
print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])
print(len(krediler)) #listenin uzunluğu
krediler[0] = "Çabuk Kredi"
print(krediler)
print(krediler[3])
krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan Alanlara Özel","Mutlu Emekli İhtiyaç Kredisi"]
#alias
for kredi in krediler:
  print(kredi)

for i in len(krediler):
  print(krediler(i))

for i in range (3,10):
  print(i)

for i in range (0,11,2):
  print(i)

def kredileriListele():
    krediler = ["Hızlı Kredi", "Maaşını Halkbank'tan alanlara özel","Mutlu emekli ihtiyaç kredisi"]
    for kredi in krediler:
        print("<option>" +kredi + "<option>")
kredileriListele()