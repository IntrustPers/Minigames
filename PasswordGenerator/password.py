import random

#Lists from which random can choose letters and numbers
let_cap = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
           "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]

let_low = ["a", "b", "c", "d", "e", "f", "g", "h", "i",
           "j", "k", "l", "m", "n", "o", "p", "q", "r",
           "s", "t", "u", "v", "w", "q", "y", "z"]

num = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

#Lists for sorting random inputs
list_num = []
list_cap = []
list_low = []

#Get password length
length = 0
while not (5 <= length <= 20):
    length = int(input("Enter the length for your password (5-20): "))

#Generate password
if 5 <= length <= 7:
    for x in range(1):
        list_num.append(random.choice(num))
    for y in range(2):
        list_cap.append(random.choice(let_cap))
    if length == 5:
        for z in range(3):
            list_low.append(random.choice(let_low))
    elif length == 6:
        for z in range(4):
            list_low.append(random.choice(let_low))
    elif length == 7:
        for z in range(5):
            list_low.append(random.choice(let_low))
elif 8 <= length <= 10:
    for x in range(2):
        list_num.append(random.choice(num))
    for y in range(3):
        list_cap.append(random.choice(let_cap))
    if length == 8:
        for z in range(3):
            list_low.append(random.choice(let_low))
    elif length == 9:
        for z in range(4):
            list_low.append(random.choice(let_low))
    elif length == 10:
        for z in range(5):
            list_low.append(random.choice(let_low))
elif 11 <= length <= 14:
    for x in range(3):
        list_num.append(random.choice(num))
    for y in range(4):
        list_cap.append(random.choice(let_cap))
    if length == 11:
        for z in range(4):
            list_low.append(random.choice(let_low))
    elif length == 12:
        for z in range(5):
            list_low.append(random.choice(let_low))
    elif length == 13:
        for z in range(6):
            list_low.append(random.choice(let_low))
    elif length == 14:
        for z in range(7):
            list_low.append(random.choice(let_low))
elif 15 <= length <= 17:
    for x in range(5):
        list_num.append(random.choice(num))
    for y in range(5):
        list_cap.append(random.choice(let_cap))
    if length == 15:
        for z in range(5):
            list_low.append(random.choice(let_low))
    elif length == 16:
        for z in range(6):
            list_low.append(random.choice(let_low))
    elif length == 17:
        for z in range(7):
            list_low.append(random.choice(let_low))
else:
    for x in range(5):
        list_num.append(random.choice(num))
    for y in range(7):
        list_cap.append(random.choice(let_cap))
    if length == 18:
        for z in range(6):
            list_low.append(random.choice(let_low))
    elif length == 19:
        for z in range(7):
            list_low.append(random.choice(let_low))
    elif length == 20:
        for z in range(8):
            list_low.append(random.choice(let_low))

password = list_num + list_cap + list_low
random.shuffle(password)

#The .join is there because if you do print(password) it is going to copy the whole list with commas and brackets
print("".join(password))

