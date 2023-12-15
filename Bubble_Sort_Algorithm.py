# Problem:
# kullanıcıdan virgülle ayrılmış sayı listesi alıyoruz. Bu sayıları buble sort
# # algoritmasıyla sıralayıp tekrar virgülle ayrılmış şekilde kullanıcıya yazıyorum.

# Çözüm Akışı:
# 1. kullanıcıdan input alıp bunu listeye atamak
# 2. bu listedeki sayıları bubble sort ile sıralamak
# 3. bu sıralı listedeki sayıları virgülle yrılmış şekilde kullanıcıya göstermek

# 1. çözüm aşaması
sayilar = input('Moruk, bana biraz sayı ver de bubble sortlayayım onu\n>')
#print(sayilar, type(sayilar))
sayilar = sayilar.split(",")
for idx in range(len(sayilar)):
    sayilar[idx] = int(sayilar[idx])

# 2. çözüm aşaması
idx = 0
while idx < len(sayilar)-1:
    sayi1 = sayilar[idx]
    sayi2 = sayilar[idx+1]
    if sayi1 > sayi2:
        sayilar[idx], sayilar[idx+1] = sayi2, sayi1
        idx = 0
        #print(sayilar)
    else:
        #print(sayi1, sayi2, sayi1 > sayi2)
        idx += 1

#print(sayilar)

#3. Çözüm Aşaması
for idx in range(len(sayilar)):
    sayilar[idx] = str(sayilar[idx])
sayilar = ",".join(sayilar)
print(sayilar)
