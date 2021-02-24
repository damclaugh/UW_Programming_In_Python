
#!/usr/bin/env python

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
        #self.rows.remove(row_id)
    
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
        pages = round(report.size()/report.limit)
        return pages
    
    def get_paged_rows(self, sort_field, page):

        if sort_field == '-fname':
            sorted_list = sorted(self.rows, key = operator.attrgetter('fname'), reverse = True)
        else:
            sorted_list = sorted(self.rows, key = operator.attrgetter('fname'))
    
        offset = (page - 1) * self.limit
        paged_rows = sorted_list[offset:]
        return paged_rows



def run_report():
    print("Report size: ", report.size())
    print("Report limit: ", report.limit)
    print("Number of pages: ", report.get_number_of_pages())
    print("---------------------------------------------------------------")

    for i in report.rows:
        print(i)

    print("---------------------------------------------------------------")


if __name__ == "__main__":

    report = Report(4)

    report.add_row(Row("natasha", "smith", "WA"))
    report.add_row(Row("devin", "lei", "WA"))
    report.add_row(Row("bob", "li", "CA"))
    report.add_row(Row("tracy", "jones", "OR"))
    report.add_row(Row("johny", "jakes", "WA"))
    report.add_row(Row("derek", "wright", "WA"))

    run_report()


# report = Report(4)

# report.add_row(Row("Natasha", "Smith", "WA"))
# report.add_row(Row("Devin", "Lei", "WA"))
# report.add_row(Row("Bob", "Li", "CA"))
# report.add_row(Row("Tracy", "Jones", "OR"))
# report.add_row(Row("Johnny", "Jakes", "WA"))
# report.add_row(Row("Derek", "Wright", "WA"))
# report.add_row(Row("Jordan", "Cooper", "WA"))
# report.add_row(Row("Mike", "Wong", "WA"))

# #natasha = Row('Natasha', 'Smith', 'WA')
# #print(natasha.id)

# #print(report.rows[0])

# for i in report.rows:
#     print(i)

# print(report.get_number_of_pages())

# print(report.get_paged_rows())


# count = 0
# for row in report.rows:
#     count += 1
# print(count)

# print(report.size())

# size = report.size()
# print
# print(report.limit)
# pages = round(int(report.size()/report.limit))
# print(pages)


# ids = []
# for i in report.rows:
#     ids.append(i.id)

# row_id = ids[0]
# print(row_id)

# print(report.rows[0].id)

# for i in report.rows:
#     if i.id == row_id:
#         report.rows.remove(i)

# #report.rows = [item for item in report.rows if item.id != row_id]

# for i in report.rows:
#     print(i)
