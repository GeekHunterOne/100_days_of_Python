# Приветственное сообщение, которое будет выводиться при запуске программы
print("Welcome to the band name generator")

# Запрашиваем у пользователя ввод города проживания и сохраняем его в переменной city
city = input("Which city did you grow up in?\n")

# Запрашиваем у пользователя ввод имени своего питомца и сохраняем его в переменной pet
pet = input("What is the name of a pet? \n")

# Генерируем имя группы объединяя город проживания и имя питомца
print("Your band name could be " + city + pet)
