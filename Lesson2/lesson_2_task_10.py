def bank():
    x = 10
    n = int(input("Начальная сумма?"))
    years = int(input("На сколько лет хотите сделать вклад?"))

    for i in range(years):
        n = int(n + x*n/100)
        print("По итогу вы получаете", n, "рублей")
bank()