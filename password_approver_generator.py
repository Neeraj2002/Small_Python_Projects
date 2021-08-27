import random


def generator():
    pass_len = 8
    password = []
    while len(password) <= pass_len:
        password.append(chr(random.randint(65, 90)))
        password.append(chr(random.randint(97, 122)))
        password.append(chr(random.randint(48, 57)))
        password.append(chr(sum(random.sample([33, 64, 35, 36, 37, 38, 42, 47], 1))))
    if len(password) >= pass_len:
        print("".join(random.sample(password, pass_len)))


print("Password Generator Software:")
a = int(input("Commands: Press 1 to generate a Password \n          Press 0 to Exit\n"))
i = 0
while i == 0:
    if a == 1:
        generator()
        i += 1
    elif a == 0:
        break
    else:
        print("Feature with this number will be updated soon!")
        i += 1
