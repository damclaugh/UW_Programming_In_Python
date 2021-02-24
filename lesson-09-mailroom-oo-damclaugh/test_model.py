
#!/usr/bin/env python3

import sys
from model import Donor
from model import DonorCollection

# initial data to test
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

# test get_report function
def test_get_report():
    test_data = {'Mackenzie Scott': [150000, 2, 75000.0], 
                'Warren Buffett': [42500, 3, 14166.67], 
                'Bill Gates': [32500, 3, 10833.33]
                }
    assert test_data == donor_db.get_report()

# test new_donations function
def test_add_donor():
    new_name = "Test"
    new_amount = 100
    donor_db.new_donation(new_name, new_amount)
    assert donor_db.check_donor(new_name) == True
    dict1 = donor_db.get_report()
    assert(dict1[new_name][0] == new_amount)
