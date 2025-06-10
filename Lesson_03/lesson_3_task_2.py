from smartphone import Smartphone

catalog = []
phone1 = Smartphone("Nokia", "A1", "+79185524789")
phone2 = Smartphone("Sumsung", "A2", "+79185524789")
phone3 = Smartphone("Nokia", "A3", "+79185524789")
phone4 = Smartphone("Nokia", "A4", "+79185524789")
phone5 = Smartphone("Nokia", "A5", "+79185524789")
catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(phone.markaPhone + "-" + phone.modelPhone + "." + phone.numPhone)
