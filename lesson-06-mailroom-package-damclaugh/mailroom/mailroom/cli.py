
#!/usr/bin/env python3

import sys
from mailroom import donors
from mailroom import model

# prompts user for input
prompt = ("Please choose one of the following options:\n"
        "1 -- Send a thank you to a single donor\n"
        "2 -- Create a report\n"
        "3 -- Send letters to all donors\n"
        "4 -- Quit\n"
        ">>> ")

# send thank you message
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
    model.add_donor(name, amount)
    print(f"Thank you, {name}, for your generous donation of ${amount:.2f}.")

# print list of donors
def print_list():
    donor_list = []
    for donor in donors.donor_db:
        donor_list.append(donor)
        print(donor)
    return donor_list

# print summary data in table format
def display_report():
    col_names = ["Donor Name", "Total Given", "Total Gifts", "Average Gift"]
    print("{:15} | {:^15} | {:^15} | {:^15}".format(*col_names))
    print("-"*70)
    sorted_data = model.get_report()
    for name, data in sorted_data.items():
        print(f"{name:<15} {'$':>2} {data[0]:>15.2f} {data[1]:>16} {'$':>2} {data[2]:>15.2f}")

# write to files letters to all donors 
def donor_letters():
    for donor, donations in donors.donor_db.items():
        letter = ("Dear {},\n"
        "Thank you for your donation of ${}.\n"
        "It will be put to very good use.\n"
        "Sincerely,\n"
        "-The Team".format(donor, donations[-1]))

        with open('{}.txt'.format(donor), 'w') as f:
            f.write(letter)

# quit program
def quit():
    sys.exit()

def main():
    switch_func_dict = {
        '1': thank_you,
        '2': display_report,
        '3': donor_letters,
        '4': quit
        }

    while True:
        response = input(prompt)
        switch_func_dict.get(response)()

if __name__ == "__main__":
    main()