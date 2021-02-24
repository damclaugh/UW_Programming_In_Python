
#!/usr/bin/env python3

# Task 1
print("file_{:03d} : {:>8.2f}, {:.2e}, {:.2e}".format(2, 123.4567, 10000, 12345.67))

# Task 2
print(f"file_{2:03d} : {123.4567:>8.2f}, {10000:.2e}, {12345.67:.2e}")

# Task 3
def formatter(in_tuple):
    length = len(in_tuple)
    first = "the {} numbers are: ".format(length)
    second = "{:d}, "*length
    combine = first + second
    fstring = combine[:-2]
    return fstring.format(*in_tuple)
print(formatter((1,2,3)))
print(formatter((2,3,5,7,9)))

# Task 4
tup = (4, 30, 2017, 2, 27)
new_tup = (tup[3], tup[4], tup[2], tup[0], tup[1])
print("{:02d}, {:d}, {:d}, {:02d}, {:d}".format(*new_tup))

# Task 5
l = ['oranges', 1.3, 'lemons', 1.1]
print(f"The weight of an {l[0][:-1]} is {l[1]} and the weight of a {l[2][:-1]} is {l[3]}")
print(f"The weight of an {l[0][:-1].upper()} is {l[1]*1.2} and the weight of a {l[2][:-1].upper()} is {l[3]*1.2}")

# Task 6
table_data = [
    ['Name', 'Age', 'Cost'],
    ['First', '10', '1000'],
    ['Second', '20', '10000'],
    ['Third', '30', '5000000'],
]
for row in table_data:
    print("{:>10} {:>10} {:>10}".format(*row))
