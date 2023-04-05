import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://sbhfaceidhospital-default-rtdb.firebaseio.com/"
})

ref = db.reference('Patients')

data = {
    "1":
        {
            "name": "Sansrita Saha",
            "age": "21",
            "sex": "Female",
            "address": "Beliaghata",
            "phno": "1234567899",
            "weight": "80"
        },
    "2":
        {
            "name": "Debopom Bannerjee",
            "age": "21",
            "sex": "Male",
            "address": "Sealdah",
            "phno": "1234564899",
            "weight": "85"
        },
    "3":
        {
            "name": "Somtirtha",
            "age": "20",
            "sex": "Male",
            "address": "Malda",
            "phno": "1257567899",
            "weight": "75"
        },
    "4":
        {
            "name": "Chayan Dev Bera",
            "age": "20",
            "sex": "Male",
            "address": "Dhapa",
            "phno": "1237617899",
            "weight": "82"
        },
    "5":
        {
            "name": "Urbi Chakraborty",
            "age": "21",
            "sex": "Female",
            "address": "Sodepur",
            "phno": "1234567139",
            "weight": "80"
        },
    "6":
        {
            "name": "Rajdeep Mondal",
            "age": "19",
            "sex": "Male",
            "address": "Birati",
            "phno": "1234516499",
            "weight": "60"
        },
    "7":
        {
            "name": "Sambit Sarkar",
            "age": "20",
            "sex": "Male",
            "address": "Dum Dum",
            "phno": "1234164329",
            "weight": "85"
        }
}

for key, values in data.items():
    ref.child(key).set(values)


def updatertdb(id, address, age, name, phno, sex, weight):
    newdata = {
        f'{id}':
            {
                "address": address,
                "age": age,
                "name": name,
                "phno": phno,
                "sex": sex,
                "weight": weight
            }
    }
    ref.update(newdata)


def creatertdb(id, address, age, name, phno, sex, weight):
    newdata = {
        "address": address,
        "age": age,
        "name": name,
        "phno": phno,
        "sex": sex,
        "weight": weight,
    }
    ref.child(id).set(newdata)


def deletertdb(id):
    ref.child(f'{id}').delete()


# updatertdb('1', 'Sealdah', '25', 'Sanshrita Saha', '9465213872', 'Female', "85")
creatertdb('8', 'Dum Dum Canttonment', '21', 'Ishan Chakraborty', '9465213872', 'Male', "70")
# deletertdb(1)
