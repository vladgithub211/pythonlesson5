money = int(input('Введите сумму='))
proc = int(input('Введите процент='))
for a in range(5):
        a = a+1
        money = money+money*(proc/100)
        print(int(money))
