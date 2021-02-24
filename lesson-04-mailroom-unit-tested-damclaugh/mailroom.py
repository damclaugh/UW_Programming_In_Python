
#!/usr/bin/env python

import sys
from operator import itemgetter

donor_db = [("Bill Gates", [653772.32, 12.17]),
            ("Jeff Bezos", [877.33]),
            ("Paul Allen", [663.23, 43.87, 1.32]),
            ("Warren Buffett", [1663.23, 4300.87, 10432.25]),
            ("Mike Bloomberg", [10786.77, 4567.80, 17.32]),
            ]

prompt = "\n".join(("Please choose one of the following options",
        "1 -- Send a Thank You",
        "2 -- Create a Report",
        "3 -- Quit",
        ">>> "))

def thank_you():
    while True:
        name = input("Enter name of donor: ")
        if name == "list":
            print_list()
            continue
        else:
            break
    while True:
        amount = input("Enter donation amount: ")
        try:
            amount = float(amount)
        except ValueError:
            print("Input must be a number. Try again")
            continue
        else:
            break
    add_donor(name, amount)
    print(f"Thank you, {name}, for your generous donation of {amount:.2f}")

# PRINTS INITIAL LIST OF DONORS
def print_list():
    names = []
    for donor in donor_db:
        names.append(donor[0])
        print(donor[0])
    return names

# TEST FOR PRINT_LIST FUNCTION
def test_list():
    donors = ["Bill Gates", "Jeff Bezos", "Paul Allen", "Warren Buffett", "Mike Bloomberg"]
    result = print_list()
    assert donors == result

def add_donor(name, amount):
    for donor in donor_db:
        if name == donor[0]:
            donor[1].append(amount)
            break
    else:
        new_entry = (name, [amount])
        donor_db.append(new_entry)
    return donor_db

# TEST FOR ADD_DONOR FUNCTION
def test_add_donor():
    new_name = "Test"
    new_amount = 100
    add_donor(new_name, new_amount)
    assert new_name == donor_db[-1][0]
    assert new_amount in donor_db[-1][1]

def get_report():
    report_data = []
    for name, donations in donor_db:
        total = round(sum(donations), 2)
        num_gifts = len(donations)
        avg = round(total/num_gifts, 2)
        report_data.append((name, total, num_gifts, avg))
    
    sorted_data = sorted(report_data, key = itemgetter(1), reverse=True)

    return sorted_data

def display_report():
    col_names = ["Donor Name", "Total Given", "Total Gifts", "Average Gift"]
    print("{:15} | {:^15} | {:^15} | {:^15}".format(*col_names))
    print("-"*70)
    for data in get_report():
        print(f"{data[0]:<15} {'$':>2} {data[1]:>15.2f} {data[2]:>16} {'$':>2} {data[3]:>15.2f}")

# TEST FOR DISPLAY_REPORT FUNCTION
def test_get_report():
    test_data = [('Bill Gates', 653784.49, 2, 326892.24),
                ('Warren Buffett', 16396.4, 3, 5465.47),
                ('Mike Bloomberg', 15371.89, 3, 5123.96),
                ('Jeff Bezos', 877.33, 1, 877.33), 
                ('Paul Allen', 708.42, 3, 236.14),
                ('Test', 100, 1, 100)]
   
    assert test_data == get_report()

def quit():
    sys.exit()

def main():
    while True:
        response = input(prompt)
        if response == "1":
            thank_you()
        elif response == "2":
            display_report()
        elif response == "3":
            quit()

if __name__ == "__main__":
    main()
