
#!/usr/bin/env python3

import sys
from operator import itemgetter

# donor list
donor_db = {"Bill Gates": [653772.32, 12.17],
            "Jeff Bezos": [877.33],
            "Paul Allen": [663.23, 43.87, 1.32],
            "Warren Buffett": [1663.23, 4300.87, 10432.25],
            "Mike Bloomberg": [10786.77, 4567.80, 17.32]
            }

# prompts user for input
prompt = ("Please choose one of the following options:\n"
        "1 -- Send a Thank You\n"
        "2 -- Create a Report\n"
        "3 -- Quit\n"
        ">>> ")

# sends thank you message
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
    print(f"Thank you, {name}, for your generous donation of ${amount:.2f}")

# prints list of donors
def print_list():
    for donor in donor_db:
        print(donor)

# adds new donation and new donor if not donor list
def add_donor(name, amount):
    for donor in donor_db.keys():
        if name == donor:
            donor_db[name].append(amount)
            break
    else:
        donor_db[name] = [amount]
    return donor_db

# tests add_donor function
def test_add_donor():
    new_name = "Test"
    new_amount = 100
    add_donor(new_name, new_amount)
    assert new_name in donor_db 
    assert new_amount == donor_db[new_name][0]

# creates summary data from donor dictionary
def get_report():
    report_data = {}
    for donor, donations in donor_db.items():
        total = round(sum(donations), 2)
        num_gifts = len(donations)
        avg = round(total/num_gifts, 2)
        report_data[donor] = [total, num_gifts, avg]
    
    sorted_data = dict(sorted(report_data.items(), key = itemgetter(1), reverse=True))

    return sorted_data

# prints summary data in table format
def display_report():
    col_names = ["Donor Name", "Total Given", "Total Gifts", "Average Gift"]
    print("{:15} | {:^15} | {:^15} | {:^15}".format(*col_names))
    print("-"*70)
    sorted_data = get_report()
    for name, data in sorted_data.items():
        print(f"{name:<15} {'$':>2} {data[0]:>15.2f} {data[1]:>16} {'$':>2} {data[2]:>15.2f}")

# tests display report function
def test_get_report():
    test_data = {'Bill Gates': [653784.49, 2, 326892.24],
                'Warren Buffett': [16396.35, 3, 5465.45],
                'Mike Bloomberg': [15371.89, 3, 5123.96],
                'Jeff Bezos': [877.33, 1, 877.33], 
                'Paul Allen': [708.42, 3, 236.14],
                'Test': [100, 1, 100]
                }
   
    assert test_data == get_report()

# quits program
def quit():
    sys.exit()

def main():
    switch_func_dict = {
        '1': thank_you,
        '2': display_report,
        '3': quit
        }

    while True:
        response = input(prompt)
        switch_func_dict.get(response)()

if __name__ == "__main__":
    main()
