import csv
day = 8
month = 3
variant = (5 + day) * 2 + month
print(variant)
fullprice = 0
calls = {}
max_number = 0
max_call = 0
output_filename = 'output_' + str(variant) + '.csv'
with open('input.csv', 'r') as r_file:
    readerCRP = csv.DictReader(r_file, delimiter=';', fieldnames=['calling phone', 'receiving phone', 'date','price'])
    with open(output_filename, 'w') as w_file:
        file_writer = csv.DictWriter(w_file, delimiter=';', lineterminator='\r', fieldnames=['calling phone', 'receiving phone', 'date', 'price'])
        for row in readerCRP:
                if (row['calling phone']) == str(variant):
                    file_writer.writerow(row)
    with open(output_filename, 'r') as s_file:
        readerCRP = csv.DictReader(s_file, delimiter=';', fieldnames=['calling phone', 'receiving phone', 'date', 'price'])
        for row in readerCRP:
            fullprice = fullprice + int(row['price'])
            calls[row['receiving phone']] = calls.get(row['receiving phone'], 0) + 1
            for k, v in calls.items():
                if v > max_call:
                    max_number = k
                    max_call = v
                    print('Цена за звонки: %s' % fullprice)
                    print('Наиболее частый вызываемый номер: %s' % max_number)
                    print('Количество звонков часто вызываемого номера: %s' % max_call)
