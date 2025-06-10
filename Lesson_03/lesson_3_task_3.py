from mailing import Mailing

mail1 = Mailing()
mail1.from_adress.index = 23
mail1.from_adress.gorod = "Москва"
mail1.from_adress.street = "Ленина"
mail1.from_adress.home = 15
mail1.from_adress.appartment = 15
mail1.to_adress.index = 14
mail1.to_adress.gorod = "Ростов"
mail1.to_adress.street = "Победы"
mail1.to_adress.home = 14
mail1.to_adress.appartment = 53

mail1.track = "N547"
mail1.const = 1000

print(mail1.track + " из " + str(mail1.from_adress.index) + ", " 
      + mail1.from_adress.gorod + ", " + mail1.from_adress.street + ", " 
      + str(mail1.from_adress.home) + "-" + str(mail1.from_adress.appartment) + " в " 
      + str(mail1.to_adress.index) + ", " + mail1.to_adress.gorod + ", " 
      + mail1.to_adress.street + ", " + str(mail1.to_adress.home) + "-" 
      + str(mail1.to_adress.appartment) + " . " 
      + "Стоимость " + str(mail1.const) + " рублей")
