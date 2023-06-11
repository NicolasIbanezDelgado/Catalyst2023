import csv
import time


test_list = []

def get_scores():
    with open('test2.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
                if line_count != 0:
                    test_list.append( {'Name': f'{row[0]}', 'ID#': row[1], 'Points': int(row[2]), 'Ranking':row[3] })
                else:
                    line_count +=1
    return test_list
     
def add_points():
    temp_bool = True
    temp_input = (input('Enter ID number '))
    while(temp_bool):
        for key in test_list:
            # print(key, "AAAA")
            if(temp_input == str(key['ID#'])):
                # print(type(key['Points']))
                key['Points'] += 1

        temp_bool = False

    sources_fields = 'Name', 'ID#', 'Points', 'Ranking'
    with open('test2.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames= sources_fields)
        writer.writeheader()
        writer.writerows(test_list)

    # print(test_list)
get_scores()
add_points()


