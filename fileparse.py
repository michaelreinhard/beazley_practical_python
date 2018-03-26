#fileparse.py

'''Read a csv file into a list of dictionaries'''

import csv

def parse_csv(filename, select=None,
              types=None, has_headers=True,
              delimiter=','):

    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        #read file headers
        headers = next(rows) if has_headers else []

        #get the index numbers for the select categories
        if select:
            indices = [headers.index(colname) for colname
                       in select]
            headers = select
            
        records = []

        for row in rows:
            #skip rows with no data
            if not row:   
                continue

            #filter the row if columns selected
            if select:
                row = [ row[index] for index in indices ]

            #apply type conversion on the row
            if types:
                row = [func(val) for func, val in zip(types, row)]
            #make a dictionary or a tuple if no headers
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

        return records


