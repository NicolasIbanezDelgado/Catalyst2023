import csv
import time
import cv2

test_list = []
user = ()

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

# print(type(get_scores()[0]['Points']))


def login():
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    while True:
        _, img = cap.read()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            a=data
            # print(a)
            break

        cv2.imshow("QRCODEscanner", img)
        if cv2.waitKey(1) == ord("q"):
            break

    temp_bool = True
    while(temp_bool):
        for key in test_list:
            if(a == str(key['ID#'])):
                user = (key['Name'], key['ID#'],key['Points'])
                # print(type(key['Ranking']))

        temp_bool = False

    return user
     
def add_points():
    local_user = login()

    for key in test_list:
        if key['ID#'] == local_user[1]:
            key['Points'] += 1

    sources_fields = 'Name', 'ID#', 'Points', 'Ranking'
    with open('test2.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames= sources_fields)
        writer.writeheader()
        writer.writerows(sort())

def sort():
    length = len(test_list)

    for i in range(length):
        swapped = False
        for j in range(0, length-i-1):
            if(test_list[j]['Points'] < test_list[j+1]['Points']):
                test_list[j], test_list[j+1] = test_list[j+1], test_list[j]
                swapped = True
        if(swapped == False):
            break

    for i in range(len(test_list)):
        test_list[i]['Ranking'] = i + 1

    return test_list

def get_ranks():
    temp_str = ""
    for key in test_list:
        temp_str += f"Name: {key['Name']},Points: {key['Points']},Rank: {key['Ranking']}\n"
    return temp_str


if __name__ == "__main__":
    get_scores()
    add_points()
    sort()
    print(get_ranks())

