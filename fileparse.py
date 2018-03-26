#fileparse.py

'''Read a csv file into a list of dictionaries'''

import csv

def parse_csv(filename, select=None,
              types=None, has_headers=True,
              delimiter=',', silence_errors=False):
    if select and not has_headers:
        raise RuntimeError('select requires column headers')
    
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

        for rowno, row in enumerate(rows, 1):
            #skip rows with no data
            if not row:   
                continue

            #filter the row if columns selected
            if select:
                row = [ row[index] for index in indices ]

            #apply type conversion on the row
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if not silence_errors:
                        print(f'Row {rowno}: Could not convert {row}')
                        print(f'Row {rowno}: Reason {e}')
                    continue
                    
            #make a dictionary or a tuple if no headers
            if headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            print("This is row {}: {}".format(rowno, row))
            records.append(record)

        return records


