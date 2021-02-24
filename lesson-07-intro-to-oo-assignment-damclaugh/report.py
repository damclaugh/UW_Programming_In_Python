#!/usr/bin/env python

"""
A set of classes to facilitate report writing
"""

import math
import operator
from uuid import uuid4

class Row:
    """
    This class represents a single row
    with ID, first name, last name and state attributes
    """
    def __init__(self, fname, lname, state):
        self.id = str(uuid4())  # randomly generated unique ID
        self.fname = fname
        self.lname = lname
        self.state = state

    def __str__(self):
        return f"| {self.id} | {self.fname + ' ' + self.lname:<15} | {self.state} |"


class Report:
    def __init__(self, limit):
        self.limit = limit
        self.rows = []

    def add_row(self, row):
        """Add a row object to the report"""
        self.rows.append(row)

    def remove_row(self, row_id):
        """Remove a row object by the row's ID"""
        for i in report.rows:
            if i.id == row_id:
                report.rows.remove(i)
        
    def size(self):
        """Return how many total rows the report has"""
        count = 0
        for row in self.rows:
            count += 1
        return count

    def get_number_of_pages(self):
        """
        Get how many pages the report has; this will be based on limit variable.
        If your limit=4 and rows list has 6 records then there are two pages:
          page1 has 4 records, page2 has 2 records
        hint: you'll want to round up
        """
        pages = math.ceil(self.size()/self.limit)
        return pages

    def get_paged_rows(self, sort_field, page):
        """Return a list of rows for a specific page number
        :param sort_field:  field to sort on, "name" or "-name" (descending)
        :param page:        specific page for returning data
        :return:            list of row objects for specific page
        """

        if sort_field == '-fname':
            sorted_list = sorted(self.rows, key = operator.attrgetter('fname'), reverse = True)
        else:
            sorted_list = sorted(self.rows, key = operator.attrgetter('fname'))

        if page == 1:
            paged_rows = sorted_list[:self.limit]
        else:
            offset = (page - 1) * self.limit
            paged_rows = sorted_list[offset:offset+self.limit]
        return paged_rows


def run_report(sort_field):
    print(f"... PAGED REPORT SORTED BY: '{sort_field}'...")
    page = 1
    while True:
        rows = report.get_paged_rows(sort_field, page=page)

        if not rows:
            break

        input(f"Press ENTER to see page {page} ")

        print(f"PAGE: {page} of {report.get_number_of_pages()}")
        print("---------------------------------------------------------------")

        for row in rows:
            print(row)

        print("---------------------------------------------------------------")

        page += 1


if __name__ == "__main__":

    report = Report(4)

    report.add_row(Row("natasha", "smith", "WA"))
    report.add_row(Row("devin", "lei", "WA"))
    report.add_row(Row("bob", "li", "CA"))
    report.add_row(Row("tracy", "jones", "OR"))
    report.add_row(Row("johny", "jakes", "WA"))
    report.add_row(Row("derek", "wright", "WA"))

    run_report("fname")

    print("\n\nRemoving student: "
          f"{report.rows[1].fname} [{report.rows[1].id}]... \n\n")

    report.remove_row(report.rows[1].id)

    run_report("-fname")
