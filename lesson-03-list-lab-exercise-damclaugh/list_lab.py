
#!/usr/bin/env python3

# SERIES 1
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
print(fruit)

response = input("Add another fruit > ")

fruit.append(response)

print(fruit)

position = input("Enter a number between 1 and 5 > ")
print(fruit[int(position) - 1])

response = input("Add another fruit > ")
fruit = [response] + fruit
print(fruit)

response = input("Add another fruit > ")
fruit.insert(0, response)
print(fruit)

for i in range(len(fruit)):
    if fruit[i][0] == 'P' or fruit[i][0] == 'p':
        print(fruit[i])


# SERIES 2
print(fruit)
del fruit[-1]
print(fruit)

response = input("Which fruit should be deleted? > ")
fruit.remove(response)

fruit = fruit*2
response = input("Which fruit should be deleted? > ")
for i in fruit:
    if i == response:
        fruit.remove(i)
print(fruit)


# SERIES 3
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
new_fruit = []

for i in fruit:
    i = i.lower()
    while True:
        response = input("Do you like {0}? Enter yes or no: ".format(i))
        if response not in ('yes', 'no'):
            continue
        else:
            break
            
    if response == 'yes':
        i = i.capitalize()
        new_fruit.append(i)

print(new_fruit)


# SERIES 4
fruit = ['Apples', 'Pears', 'Oranges', 'Peaches']
new_fruit = []

for i in range(len(fruit)):
    new_fruit.append(fruit[i][::-1])

del fruit[-1]

print(fruit)
print(new_fruit)

    