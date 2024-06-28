from smartphone import Smartphone

catalog = []

phone1 = Smartphone("Samsung", "AP8", "+79568967820")
phone2 = Smartphone("iPhone", "15", "+79205007850")
phone3 = Smartphone("LG", "Qwer", "+79872023054")
phone4 = Smartphone("BQ", "Bonk", "+79105067269")
phone5 = Smartphone("Reno", "Uoy", "+79569305210")

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}, {phone.number}")
