#a = input()
#if a == "Python":
# print("ДА")
#else:
# print("НЕТ")

#zxc = input()
#zxc2 = input()
#if zxc in "да" and zxc2 in "да":
#  print("верно")
#elif zxc in "нет" and zxc2 in "нет":
#  print("верно")
#else:
#   print("неверно")

#zov = input()
#zov2 = input()
#zov3 = input()
#if zov == "1" and zov2 == "2" and zov3 == "3":
#   print("ГОРИ")
#elif zov == "раз" and zov2 == "два" and zov3 == "три":
#   print("ГОРИ")
#else: print("не гори")

#category = input("Введите категорию товара: ")

#if category.lower() == "продукты":
#    price = int(input("Введите цену товара: "))
#    if price < 100:
#        print("Попробуйте нашу выпечку!")
#    elif price>= 100 and price <= 500:
#       print("Как насчёт орехов в шоколаде?")
#    else:
#        print("Попробуйте экзотические фрукты!")
#    print("Загляните в товары для дома!")

price1 = int(input('Цена первого товара:'))
price2 = int(input('Цена второго товара:'))
price3 = int(input('Цена третьего товара:'))
if price1 <= price2 and price2 <= price3:
    print('Акция!')
    print('К оплате:', (price1 + price2 + price3)/2)
elif price3 <= price2 and price2 <= price1:
    print('Акция!')
    print('К оплате:', (price1 + price2 + price3)/3)
else: print('К оплате:', price1 + price2 + price3)