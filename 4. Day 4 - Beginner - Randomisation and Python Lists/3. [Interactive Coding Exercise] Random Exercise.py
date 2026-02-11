import random

# random.seed(123)
# print(random.randint(1, 10))
# print(random.random() * 5)

test_seed = int(input('create a seed number: '))
random.seed(test_seed)

random_side = random.randint(0, 1)
if random_side == 1:
    print('Heads')
else:
    print('tails')    