
#!/usr/bin/env python3

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

    def check_donor(self, name):
        for donor in self.donors.keys():
            if name == donor:
                return True
        else:
            return False
        
    def get_report(self):  
        report_data = {}
        for donor, donations in self.donors.items():
            report_data[donor] = [donations.sum_donations(), donations.num_donations(), donations.avg_donation()]
        sorted_data = dict(sorted(report_data.items(), key = itemgetter(1), reverse=True))
        return sorted_data
    
    def new_donation(self, name, donation):
        if self.check_donor(name):
            self.donors[name].add_donation(donation)
        else:
            new_donor = Donor(name)
            new_donor.add_donation(donation)
            self.donors[name] = new_donor

    def donor_letters(self):
        for donor, donations in self.donors.items():
            donation = donations.get_last_donation()
            letter = ("Dear {},\n"
            "Thank you for your donation of ${}.\n"
            "It will be put to very good use.\n"
            "Sincerely,\n"
            "-The Team".format(donor, donation))

            with open('{}.txt'.format(donor), 'w') as f:
                f.write(letter)