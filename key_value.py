#Написать программу, которая берет словарь и меняет местами ключи и значения
distionary ={'name': 'Channing', 'surname': 'Tatum'}
for key in distionary:
    print(key, distionary[key])
new_distionary = {value:key for key, value in distionary.items()}
for key in new_distionary:
    print(key, new_distionary[key])
