import RPi.GPIO as GPIO
import time

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('firebase.json')

firebase_admin.initialize_app(cred,{
'databaseURL': "https://raspberrypi-84de0.firebaseio.com/"
})

ref = db.reference('status')


while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    print "LED on"
    ref.push({
        "status":"LED on" 
    })

    GPIO.output(18,GPIO.HIGH)
    time.sleep(4)
    print "LED off"
    ref.push({
         "status":"LED off" 
    })
    GPIO.output(18,GPIO.LOW)
    time.sleep(3)
