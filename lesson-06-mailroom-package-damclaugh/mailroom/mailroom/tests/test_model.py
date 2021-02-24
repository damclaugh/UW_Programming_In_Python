
#!/usr/bin/env python3

import sys
from mailroom import model
from mailroom import donors
from operator import itemgetter

# test add_donor function
def test_add_donor():
    new_name = "Test"
    new_amount = 100
    model.add_donor(new_name, new_amount)
    assert new_name in donors.donor_db
    assert new_amount == donors.donor_db[new_name][0]

# test get_report function
def test_get_report():
    test_data = {'Bill Gates': [653784.49, 2, 326892.24],
                'Warren Buffett': [16396.35, 3, 5465.45],
                'Mike Bloomberg': [15371.89, 3, 5123.96],
                'MacKenzie Scott': [877.33, 1, 877.33], 
                'Paul Allen': [708.42, 3, 236.14],
                'Test': [100, 1, 100]
                }
    assert test_data == model.get_report()