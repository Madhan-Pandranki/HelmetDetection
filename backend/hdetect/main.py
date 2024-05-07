from easyocr import Reader
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import cv2
import pandas as pd
import smtplib
import os
from twilio.rest import Client
import geocoder
import re
import mailtrap as mt
from dotenv import load_dotenv

load_dotenv()

g = geocoder.ip('me')
CAMERA_LOCATION = g.json['address']+f'. [Lat: {g.lat}, Lng:{g.lng}]'


def sendMail(mail):
    body = f'You were caught riding without helmet or triple riding near {CAMERA_LOCATION}, and were fined Rupees 500. Please visit https://bit.ly/3QQxTRO to pay your due challan. If you are caught riding again without proper gear, you will be severely penalized.'
    message = MIMEText(body)
    message["Subject"] = 'Notification regarding e-challan fine'
    message["From"] = "jitendralohani01@gmail.com"
    message["To"] = mail
    with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
        server.login(os.getenv('EMAIL'), os.getenv('PASS'))
        server.sendmail('jitendralohani01@gmail.com', mail, message.as_string())
    # server.quit()
  

database = pd.read_csv('database.csv')
def countf(directory):
    try:
        return sum(1 for _ in os.scandir(directory) if _.is_file())
    except FileNotFoundError:
        return 0  



BASE_D="yolov9/runs/detect/exp/crops/bike"
warnedNums = []

for path in os.listdir(BASE_D):
    FILE=os.path.join(BASE_D, path)
    command_v=f"rm -rf ./runs/detect/exp2 && python /home/jitu/Projects/Hdetect/backend/hdetect/yolov9/detect.py --source {FILE} --weights '/home/jitu/Projects/Hdetect/backend/hdetect/yolov9/best.pt'  --save-crop"
    r_c=os.system(command_v)
    h="yolov9/runs/detect/exp2/crops/helmet"
    nh="yolov9/runs/detect/exp2/crops/No-helmet"


    if os.path.exists('yolov9/runs/detect/exp2/crops/No-helmet') or (countf(h)+countf(nh))>2:
        BASE_DIR = 'yolov9/runs/detect/exp2/crops/number-plate'
        if __name__ == '__main__':
            if(os.path.exists(BASE_DIR)):
                for path in os.listdir(BASE_DIR):
                    path = os.path.join(BASE_DIR, path)
                    img = cv2.imread(path, 0)
                    reader = Reader(['en'])
                    number = reader.readtext(img, mag_ratio=3)
                    licensePlate = ""
                    licensePlate = number[0][1] if number else "No number plate found"
                    print('License number is:', licensePlate)

                    if licensePlate not in warnedNums:
                        for index, plate in enumerate(database['Registration']):
                            if licensePlate == plate:
                                database.at[index, 'Due challan'] += 500
                                mail = database['Email'][index]
                                num = database['Phone number'][index]
                                print('mail:',mail)
                                sendMail(mail)
                                print(f"{database['Name'][index]} successfully notified!")
                                warnedNums.append(licensePlate)
                                database.to_csv('database.csv', index=False)
