#countries = ["Cypro", "UAE", "USA", "England", "Portugal"]
#print(countries)
#print(len(countries))
#countries.sort()
#print(countries)
#countries.sort(reverse = True)
#print(countries)
#print(countries)
#countries.reverse()
#print(countries)
#countries.sort()
#print(countries)
#countries.sort(reverse = True)
#print(countries)

#juft_sonlar = list(range(120,1202,2))
#print(juft_sonlar)
#print("120 dan 1200 gacha bolgan juft sonlar yigindisi ",sum(juft_sonlar))
#print(max(juft_sonlar)-min(juft_sonlar))
#print("Elementlar soni: ", len(juft_sonlar))
#print(juft_sonlar[:20], juft_sonlar[270:290], juft_sonlar[520:]) 

# =============================================================================
# taomlar = ["Manti", "Palov", "Somsa", "Kabob"]
# nonushta = taomlar[:]
# nonushta.remove("Manti")
# nonushta.remove("Kabob")
# nonushta.append("Tuxum")
# nonushta.append("Kolbasa")
# print(taomlar)
# print(nonushta)
# nonushta = tuple(nonushta)
# nonushta[0] = "qaymoq va non"
# =============================================================================
# =============================================================================
# ismlar = ["Anvar", "Muxtor", "Dilshod", "Botir", "Vali"]
# # = 0
# for ism in ismlar:
#     print("Salom", ism)
# #    n = n+1
# print("Kod ", len(ismlar), " martta takrorlandi")
# =============================================================================
# =============================================================================
# toq_sonlar = list(range(11,100,2))
# for n in toq_sonlar:
#     print(n**3)
# =============================================================================
# =============================================================================
# filmlar = []
# print("5 ta sevimli filmingizni kiriting:")
# for n in range(5):
#     filmlar.append(input(f"{n+1}-chi filmingizni kiriting:"))
#     
# print(filmlar)
# =============================================================================
# =============================================================================
# odamlar = []
# n = int(input("Bugun nechta odam bilan gaplashdingiz?"))
# for odam in range(n):
#     odamlar.append(input(f"{odam+1}-chi odamninig ismini kiriting:"))
# print(odamlar)
# =============================================================================
# =============================================================================
# cars = ["toyota", "mazda", "hyundai", "gm", "kia"]
# for car in cars:
#     if car != "gm":
#         print(car.title())
#     else:
#         print(car.upper())
# =============================================================================
# =============================================================================
# user = input("Loginni kiriting>>>")
# if user.lower() == "admin":
#     print("Xush kelibsiz, Admin! Foydalanuvchilar royxatini korasizmi?")
# else:
#     print("Xush kelibsiz " + user.title() + "!")
# =============================================================================
# =============================================================================
# print("1 ta son kiriting: ")
# a = int(input())
# #b = input("Ikkinchi son :")
# if a >= 0:
#     print(a, "sonining ildizi: ", a ** (0.5), " ga teng.")
# else:
#     print("Musbat son kiriting")
# =============================================================================
# =============================================================================
# son = int(input("Juft son kiriting: "))
# if (son%2) == 0:
#     print("Raxmat!")
# else:
#     print("Bu juft son emas!")
# =============================================================================
# =============================================================================
# yosh = int(input("Yoshingizni kiriting: "))
# narx = 0
# if yosh < 4 or yosh > 60:
#     print("Sizga kirish bepul")
# elif yosh < 18:
#     print("Kirish 10 000 sum")
# else : 
#     print("Kirish 20 000 sum.")
#         
# =============================================================================
# =============================================================================
# print("Ikkita son kiriting" )
# a = int(input("Birinchi sonni kiriting: "))
# b = int(input("Ikkinchi sonni kiriting: "))
# if a>b:
#     print(f"{a} > {b}")
# elif a<b:
#     print(f"{a} < {b}")
# else : 
#     print(f"{a} = {b}")
# =============================================================================
# =============================================================================
# maxsulotlar = ["olma", "anor", "uzum", "shaftoli", "orik", "anjir", "nok", "tarvuz", "qovun", "xandalak"]
# savat = []
# print("Savatga 5 ta mahsulot kiriting")
# for n in range(5):
#     savat.append(input(f"Savatga {n+1} -mahsulotni kiriting:"))
# if savat:
#     for maxsulot in savat :
#         if maxsulot in maxsulotlar:
#             print(f"Dokonimizda {maxsulot} bor.")
#         else:
#             print(f"Dokonimizda {maxsulot} yoq.")
# else:
#     print("Savat bosh.")
# ==========================================================================
# =============================================================================
# users = ["dilshod", "anvar", "sveta", "ira", "nodir"]
# user = input("Yangi login kiriting: ")
# if user.lower() in users:
#     print("Login band, boshqa login tanlang!")
# else:
#     print("Xush kelibsiz!")
# =============================================================================
# =============================================================================
# =============================================================================
# otam = {"ismi":"Axmadjon", "yoshi":63, "tugilgan yili":1957, "manzil":"Oqqorgon tumani"}
# print(f"Mening otamning ismi {otam['ismi']}")
# print(f"yoshlari {otam['yoshi']} da")
# print(f"{otam['tugilgan yili']} yilda {otam['manzil']}da tugilgan")
# =============================================================================
# =============================================================================
# ovqatlar = {'onam':'palov', 'otam':'manti', 'singlim':'shorva'}
# print(f"Onamning sevimli ovqati {ovqatlar['onam']}.")
# =============================================================================

# =============================================================================
# dic = {'print':'chpop etish', 'if':'agar', 'else':'aks holda'}
# soz = input("Kalit soz kiriting: ")
# #tarjima = dic.get(soz, "Bunday soz mavjud emas!")
# if soz in dic:
#     print(dic.get(soz))
# else:
#     print("Bunday soz mavjud emas!")
# =============================================================================
# =============================================================================
# countries = {
#        'uzbekistan':'tashkent',
#        'rossiya':'moskva',
#        'qozogiston':'astana',
#        'ukraina':'kiev',
#        'fransiya':'parij',
#        'germaniya':'berlin',
#        'italiya':'milan',
#        'gretsiya':'afina',
#        'turkiya':'anqara',
#        'kanada':'toronto'
#        }
# #print("Qaysi davlatning poytahtini bilmoqchisiz?: ")
# #for davlat in sorted(countries.keys()):
# #    print(davlat.title())
# #print("\nDavlat poytahtlari: ")
# #for shahar in sorted(countries.values()):
#  #   print(shahar.title())
# country = input("Qaysi davlatning poytahtini bilmoqchisiz?: ")
# if country in countries:
#     print(country.title() + " davlatining poytahti - "+countries.get(country).title() + " shahri.")
# else:
#     print("Bunday malumot bizda yoq.")
# =============================================================================
menu = {
       'manti':'15000',
       'non':'3000',
       'osh':'20000',
       'mastava':'10000',
       'salat':'5000',
       'choy':'1000',
       'kabob':'8000',
       'norin':'18000',
       'gamburger':'12000',
       'hot-dog':'7000'
       }
print("3 ta taom buyurtma bering:")
buyurtma = []
for n in range(3):
    buyurtma.append(input(f"{n+1} chi taom:"))
    
for z in range(3):
    if buyurtma[z] in menu:
        print(buyurtma[z].title() + " - " + menu.get(buyurtma[z]) + " som")
    else:
        print("Kechirasiz, bizda " + buyurtma[z] + " yoq.")

    


