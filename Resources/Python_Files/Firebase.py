from firebase import firebase 
import csv

def setUpApp():
    global firebase
    firebase = firebase.FirebaseApplication("https://lc-project-d2adc.firebaseio.com/", None)
    sendData()

def getData():
    data =[ ]
    with open ("../Data_Files/polarbears.csv","r") as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
           data.append(dict(row))
    return data
    
def sendData():
    data= getData()
    print(data)
    result = firebase.post('/lc-project-d2adc/polarbears', data)
    print(result)



setUpApp()
