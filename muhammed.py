import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('firebase.json')

firebase_admin.initialize_app(cred,{
'databaseURL': "https://raspberrypi-84de0.firebaseio.com/"
})

ref = db.reference('status')
ref.push({
"student":{
    'emp1':{"firstName":"John", "lastName":"Doe"}, 
    'emp2':{"firstName":"Anna", "lastName":"Smith"},
    'emp3':{"firstName":"Peter", "lastName":"Jones"}
}
})
