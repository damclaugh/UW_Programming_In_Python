
from operator import itemgetter

class Donor: 
    def __init__(self, name):
        self.name = name
        self.donations = []

    def add_donation(self, donation):
        self.donations.append(donation)

    def sum_donations(self):
        return sum(self.donations)
    
    def num_donations(self):
        return len(self.donations)
    
    def avg_donation(self):
        return round(sum(self.donations)/len(self.donations), 2)
    
    def get_last_donation(self):
        return self.donations[-1]


class DonorCollection:
    def __init__(self, *donors):
        self.donors = {obj.name: obj for obj in donors}

    def donor_names(self):
        for key in self.donors:
            print(key)
        
    def get_report(self):
        report_data = {}
        for donor, donations in self.donors.items():
            report_data[donor] = [donations.sum_donations(), donations.num_donations(), donations.avg_donation()]
        sorted_data = dict(sorted(report_data.items(), key = itemgetter(1), reverse=True))
        return sorted_data
    
    def check_donor(self, name):
        for donor in self.donors.keys():
            if donor == name:
                return True
        else:
            return False

    def print_donors(self):
        for donor in self.donors.keys():
            print(donor)
 
    def new_donation(self, name, donation):
        if self.check_donor(name):
            self.donors[name].add_donation(donation)
        else:
            new_donor = Donor(name)
            new_donor.add_donation(donation)
            self.donors[name] = new_donor

    def rpt(self):
        for donor, donations in self.donors.items():
            donation = donations.get_last_donation()
            print(donation)
            

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

#print(d1.sum_donations())

# print(donor_db.get_report())

# print(donor_db.check_donor('Bill Gates'))


print(donor_db.get_report())

new_name = 'Joe'
new_donation = 100
donor_db.new_donation(new_name, new_donation)

# donor_db.new_donation('Warren Buffett', 10000000)

print(donor_db.get_report())

# print(donor_db.check_donor(new_name))

# donor_db.new_donation('Mackenzie Scott', 20000000)

print(donor_db.print_donors())

dict1 = donor_db.get_report()
print(dict1['Joe'][0] == 100)




# # prompts user for input
# prompt = ("Please choose one of the following options:\n"
#         "1 -- Send a Thank You\n"
#         "2 -- Create a Report\n"
#         "3 -- Quit\n"
#         ">>> ")

# def thank_you():


# # adds new donation and new donor if not donor list
# def add_donor(name, amount):
#     for donor in donor_db.keys():
#         if name == donor:
#             donor_db[name].append(amount)
#             break
#     else:
#         donor_db[name] = [amount]
#     return donor_db


# # creates summary data from donor dictionary
# def get_report():
#     report_data = {}
#     for donor, donations in donor_db.items():
#         total = round(sum(donations), 2)
#         num_gifts = len(donations)
#         avg = round(total/num_gifts, 2)
#         report_data[donor] = [total, num_gifts, avg]
    
#     sorted_data = dict(sorted(report_data.items(), key = itemgetter(1), reverse=True))

#     return sorted_data

# # prints summary data in table format
# def display_report():
#     col_names = ["Donor Name", "Total Given", "Total Gifts", "Average Gift"]
#     print("{:15} | {:^15} | {:^15} | {:^15}".format(*col_names))
#     print("-"*70)
#     sorted_data = get_report()
#     for name, data in sorted_data.items():
#         print(f"{name:<15} {'$':>2} {data[0]:>15.2f} {data[1]:>16} {'$':>2} {data[2]:>15.2f}")


# # quits program
# def quit():
#     sys.exit()

# def main():
#     switch_func_dict = {
#         '1': thank_you,
#         '2': display_report,
#         '3': quit
#         }

#     while True:
#         response = input(prompt)
#         switch_func_dict.get(response)()

# if __name__ == "__main__":
#     main()
