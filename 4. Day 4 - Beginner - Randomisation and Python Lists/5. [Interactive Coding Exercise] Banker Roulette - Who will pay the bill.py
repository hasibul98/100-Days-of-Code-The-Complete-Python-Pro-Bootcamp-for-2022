import random
# test_seed = int(input('create a seed number: '))

# random.seed(test_seed)

nameAsCSV = input("Give me everybody's names, separated by a comma. ")

names = nameAsCSV.split(', ')
# print(len(names))
num_items = len(names)
random_choice = random.randint(0, num_items - 1)
# print(random_choice)
# peson_who_will_pay = names[random_choice]
# print('this bill will pay mr. ' + person_who_will_pay)

person_who_will_pay = random.choice(names)

print('this bill will pay mr. ' + person_who_will_pay)