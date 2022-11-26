import cv2
import pandas as pd
import os
import glob

def cleanup_data():
    files = glob.glob('generated-certificates/*')
    for f in files:
        print(f)
        os.remove(f)


def generate_certificates():
    from_date = []
    to_date = []
    df = pd.read_excel('Contact Information.xlsx', index_col=None)
    key = df['Full Name'].tolist()
    from_dates = df['Event From Date'].tolist()
    to_dates = df['Event To Date'].tolist()
    for date in from_dates:
        from_date.append(str(date.date()))
    print(type(from_date))

    for index, names in enumerate(key):
        template = cv2.imread("certificate-generator/cretificate-template.jpg")
        cv2.putText(template, names, (500, 405),
                    cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 2, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(template, from_date[index], (782, 552),
                    cv2.FONT_HERSHEY_SCRIPT_COMPLEX, 1, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.imwrite(f'generated-certificates/{names}.jpg', template)
        print(f'Processing {index + 1} / {len(key)}')


cleanup_data()
generate_certificates()
