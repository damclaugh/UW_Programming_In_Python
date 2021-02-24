
#!/usr/bin/env python

import sys

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
            for donor in donor_db:
                print(donor[0])
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

    for donor in donor_db:
        if name == donor[0]:
            donor[1].append(amount)
            break
    else:
        new_entry = (name, [amount])
        donor_db.append(new_entry)

    print(f"Thank you, {name}, for your generous donation of {amount:.2f}")


def create_report():
    for index, donor in enumerate(donor_db):
        total = round(sum(donor[1]), 2)
        num_gifts = len(donor[1])
        avg = round(total/num_gifts, 2)
        donor_db[index] += (total, num_gifts, avg)

    sorted_db = sorted(donor_db, key=lambda x: x[2], reverse=True)

    col_names = ["Donor Name", "Total Given", "Total Gifts", "Average Gift"]
    print("{:15} | {:^15} | {:^15} | {:^15}".format(*col_names))
    print("-"*70)
    for donor in sorted_db:
        print(f"{donor[0]:<15} {'$':>2} {donor[2]:>15.2f} {donor[3]:>16} {'$':>2} {donor[4]:>15.2f}")


def quit():
    sys.exit()

def main():
    while True:
        response = input(prompt)
        if response == "1":
            thank_you()
        elif response == "2":
            create_report()
        elif response == "3":
            quit()

if __name__ == "__main__":
    main()
