import cv2
import pandas as pd
import os
import glob

list_of_names = []


def cleanup_data():
    files = glob.glob('generated-certificates/*')
    for f in files:
        print(f)
        os.remove(f)

    # with open("name-list-data") as file:
    #     for line in file:
    #         list_of_names.append(line.strip())


def generate_certificates():
    df = pd.read_excel('Contact Information.xlsx', index_col=None)
    key = df['Full Name'].tolist()

    for index, names in enumerate(key):
        template = cv2.imread("certificate-generator/cretificate-template.jpg")
        cv2.putText(template, names, (500, 405),
                    cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imwrite(f'generated-certificates/{names}.jpg', template)
        print(f'Processing {index + 1} / {len(key)}')


cleanup_data()
# generate_certificates()
