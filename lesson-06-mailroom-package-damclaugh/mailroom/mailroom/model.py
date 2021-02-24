
#!/usr/bin/env python3

import sys
from mailroom import donors
from operator import itemgetter

# add new donation and new donor if not donor list
def add_donor(name, amount):
    for donor in donors.donor_db.keys():
        if name == donor:
            donors.donor_db[name].append(amount)
            break
    else:
        donors.donor_db[name] = [amount]
    return donors.donor_db

# create summary data from donor dictionary
def get_report():
    report_data = {}
    for donor, donations in donors.donor_db.items():
        total = round(sum(donations), 2)
        num_gifts = len(donations)
        avg = round(total/num_gifts, 2)
        report_data[donor] = [total, num_gifts, avg]
    
    sorted_data = dict(sorted(report_data.items(), key = itemgetter(1), reverse=True))

    return sorted_data
