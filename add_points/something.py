import csv
import time
import cv2

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
    cap = cv2.VideoCapture(0)
    detector = cv2.QRCodeDetector()

    while True:
        _, img = cap.read()
        data, bbox, _ = detector.detectAndDecode(img)
        if data:
            a=data
            print(a)
            break

        cv2.imshow("QRCODEscanner", img)
        if cv2.waitKey(1) == ord("q"):
            break

    temp_bool = True
    while(temp_bool):
        for key in test_list:
            if(a == str(key['ID#'])):
                key['Points'] += 1
            else:
                print(type(a))

        temp_bool = False

    sources_fields = 'Name', 'ID#', 'Points', 'Ranking'
    with open('test2.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames= sources_fields)
        writer.writeheader()
        writer.writerows(test_list)

    # print(test_list)
get_scores()
add_points()  


