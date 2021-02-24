
#!/usr/bin/env python3

import sys
from model import Donor
from model import DonorCollection

prompt = ("Please choose one of the following options:\n"
        "1 -- Display donor report\n"
        "2 -- Add donation\n"
        "3 -- Send thank you letters to donors for last donation\n"
        "4 -- Quit\n"
        ">>> ")

def display_report():
    '''
    Display table of all donors ranked by total donations
    from largest to smallest
    '''
    col_names = ["Donor Name", "Total Given", "Total Gifts", "Average Gift"]
    print("{:15} | {:^15} | {:^15} | {:^15}".format(*col_names))
    print("-"*70)
    sorted_data = donor_db.get_report()
    for name, data in sorted_data.items():
        print(f"{name:<15} {'$':>2} {data[0]:>15.2f} {data[1]:>16} {'$':>2} {data[2]:>15.2f}")

def add_donation():
    '''
    Add new donation from existing donor or a new donor
    '''
    name = input("Enter name of donor: ")
    donation = int(input("Enter donation amount: "))
    donor_db.new_donation(name, donation)

def donor_letters():
    '''
    Generate thank you letters to all donors for their last donation
    and saves each to a text file
    '''
    donor_db.donor_letters()
    
def quit():
    sys.exit()

def main():
    switch_func_dict = {
        '1': display_report,
        '2': add_donation,
        '3': donor_letters,
        '4': quit
        }

    while True:
        response = input(prompt)
        switch_func_dict.get(response)()

if __name__ == "__main__":

    # initial donors
    d1 = Donor('Bill Gates')
    d1.add_donation(10000)
    d1.add_donation(15000)
    d1.add_donation(7500)

    d2 = Donor('Mackenzie Scott')
    d2.add_donation(50000)
    d2.add_donation(100000)

    d3 = Donor('Warren Buffett')
    d3.add_donation(7500)
    d3.add_donation(15000)
    d3.add_donation(20000)

    donor_db = DonorCollection(d1, d2, d3)

    main()