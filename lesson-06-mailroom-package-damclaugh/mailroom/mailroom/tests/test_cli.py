
#!/usr/bin/env python3

import sys
from mailroom import donors
from mailroom import model
from mailroom import cli

# test print_list function
def test_list():
    test_donors = ["Bill Gates", "MacKenzie Scott", "Paul Allen", "Warren Buffett", "Mike Bloomberg"]
    donor_list = cli.print_list()
    assert test_donors == donor_list


    
    