def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    "Avto xaqida malumotlarni lugat korinishida qaytaruvchi funksiya"
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rangi':rangi,
            'korobka':korobka,
            'yili':yili,
            'narxi':narxi}
    return avto

def avto_kirit():
    "Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar xaqida malumotni biitta royxatga kirituvchi funksiya"
    avtolar=[]
    while True:
       print("\nQUyidagi malumotlarni kiriting:", end='')
       kompaniya=input("Ishlab chiqaruvchi: ")
       model=input("Modeli: ")
       rangi=input("Rangi: ")
       korobka=input("Korobka turi: ")
       yili=input("Ishlab chiqarilgan yili: ")
       narxi=input("Narxi: ")
       avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
       javob = input("Yana avto kiritasizmi? (yes/no) :")
       if javob=="no":
           break
    return avtolar

def info_print(avto_info):
    "Avtolar saqlanadigan lugatni consolga chaqaruvchi funksiya"
    print(f"{avto_info['rangi'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka"
          f"{avto_info['yili']}-yil, {avto_info['narxi']}$")

