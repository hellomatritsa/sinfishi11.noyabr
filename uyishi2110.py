##1-masala

# mb=int(input("fayl hajmi: "))
# tezlik=int(input("Tezlik kiriting: "))

# vaqt=(mb*8)/tezlik

# print(f"Fayl {vaqt} soniyada yuklanadi")

##2-masala

# son=int(input("Uch xonali son: "))
# birlik=son%10
# onlik=son//10%10
# yuzlik=son//100

# print(f"{son} dagi raqamlar yig'indisi = {birlik+onlik+yuzlik}")

##3-masala

# soch=int(input("Soch oldirasizmi? 1.Ha 0.Yo'q"))
# soqol=int(input("Soqol oldirasizmi? 1.Ha 0.Yo'q"))

# if soch == 1 and soqol == 1:
#     print(f"Jami to'lov: {25000+10000} so'm")
# elif soch == 1:
#     print("Jami to'lov: 25000 so'm ")
# elif soqol == 1:
#      print("Jami to'lov: 10000 so'm ")
# else:
#     print("Siz soch ham soqol ham oldirmadingiz! ")

##4-masala

# soz=input("Ismingizni kiriitng: ")
# soz=soz.lower()
# print(f"@{soz}")

##5-masala

# narx=40000
# nechta=int(input("Necha kishi: "))

# print(f"""Jami to'lov: {narx*nechta} so'm 
# Har bir kishi: {narx} so'm""")

##6-masala

# ism_sharif=input("Ism sharifingizni kiriting: ")
# bir_harf=ism_sharif[0]
# oxir_harf=ism_sharif[-1]


# print(f":Birinchi harf: {bir_harf}\nOxirgi_harf: {oxir_harf}")

##7-masala

# ism=input("Ismingiz: ")
# matn=ism[0:2:]+ism[-2:]

# print(matn*3)

##8-masala

# kitob=input("Kitob nomini kiriting: ")
# kitob=kitob.title()
# print(kitob.center(30))

##9-masala

# sms=input("Habar kiriting: ")
# belgi=len(sms)
# print(f"SMS uzunligi: {belgi} ta belgi")

##10-masala

# belgi=ord(input("Belgi kiriting: "))
# belgi=belgi+3

# print(chr(belgi))

##11-masala

# soz=input("So'z kiriitng: ")
# soz=soz[::-1]
# print(soz)

##12-masala

# parol=input("Parol kiriting: ")
# uzunligi=len(parol)

# if(uzunligi >= 8):
#     print(f"Parol uzunligi {uzunligi} belgi - True")
# else:
#     print(f"Parol uzunligi {uzunligi} belgi - False")

##13-masala

# nomer=input(("Tel nomer: "))

# nomer=nomer.replace("+", "").replace("-","")
# print(nomer)

##14-masala

# matn=input("Matn kiriting: ")
# print(f"Faqat harfmi? {matn.isalpha()}")
# print(f"Faqat raqammi? {matn.isdigit()}")
# print(f"Harf+raqammi? {matn.isalnum()}")

##15-masala

ism=input("ISm kiriting: ")
a=ord(ism[0])
b=ord(ism[1])
c=ord(ism[2])

print(a+b+c)

