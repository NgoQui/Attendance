from email import message

from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from login.models import Student,Class
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import easygui
import tkinter as tk
import sqlite3
f=0

import ctypes  # An included library with Python install.

def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)


@csrf_protect
def signup(request):
    return render(request, 'signup.html')


@csrf_protect
def save(request):
    try:
        uname=request.POST.get('Username')
        passw=request.POST.get('password')
        a= Student.objects.all()
        for a1 in a:
            if a1.Username==uname:
                Mbox('popup','Username is already present',1)
                f = 0
                return render(request,'login.html')

            else:
                f =1
            if  f==1:


                if (len(uname)>=3 and len(uname)<16 and len(passw)>=6 and len(passw)<16):
                    print(request.POST)
                    print("yes")
                    sign_up = Student(Username=request.POST.get('Username'),
                                      email=request.POST.get('email'),
                                      # Course=request.POST.get('Course'),
                                      password=request.POST.get('password'),

                                      )
                    sign_up.save()
                    print("Successful")
                    return render(request, 'login.html')
                elif(len(passw)>=6 and len(passw)<16):
                    Mbox('popup', 'Username must be in 3 to 15 digit.', 1)
                    return render(request, 'signup.html')
                elif(len(uname)>=3 and len(uname)<16):
                    Mbox('popup', 'Password must be in 6 to 15 digit.', 1)
                    return render(request, 'signup.html')
                else:
                    Mbox('popup', 'Username must be in 3 to 15 digits and Password must be in 6 to 15 digit.', 1)
                    return render(request, 'signup.html')
    except Exception as ex:
        print("Exception is:", ex)
        return render(request, 'fail.html')


def login(request):
    return render(request, 'login.html')


def mainpage(request):
    students = Student.objects.all()
    flag = 0
    try:
        if(not students):
            Mbox('popup', 'Please Register', 1)
            return render(request, 'signup.html')
        else:
            for student in students:
                username = student.Username
                password = student.password
                if username == request.POST.get('Username') and password == request.POST.get('password'):
                    return render(request, 'mainpage.html')
                # else:
                # return render(request,'fail.html')
                else:
                    flag = 1
            if flag == 1:
                Mbox('popup','Enter the details correctly',1)
                return render(request,'login.html')

    except:
        print('NOTHING')
        return render(request, 'login.html')



def IT(request):
    return render(request, 'it.html')


def Comp(request):
    return render(request, 'comp.html')


def Mech(request):
    return render(request, 'mech.html')


def Elect(request):
    return render(request, 'elect.html')


def Eandtc(request):
    return render(request, 'eandtc.html')


def Civil(request):
    return render(request, 'civil.html')


# ******************************************************************
# Year templates
# first year

def ITfirstyear(request):
    return render(request, 'firstyear/ityear.html')


def Compfirstyear(request):
    return render(request, 'firstyear/compyear.html')


def Mechfirstyear(request):
    return render(request, 'firstyear/mechyear.html')


def Electfirstyear(request):
    return render(request, 'firstyear/electyear.html')


def Eandtcfirstyear(request):
    return render(request, 'firstyear/eandtcyear.html')


def Civilfirstyear(request):
    return render(request, 'firstyear/civilyear.html')



# second year
def ITsecondyear(request):
    return render(request, 'secondyear/ityear.html')


def Compsecondyear(request):
    return render(request, 'secondyear/compyear.html')


def Mechsecondyear(request):
    return render(request, 'secondyear/mechyear.html')


def Electsecondyear(request):
    return render(request, 'secondyear/electyear.html')


def Eandtcsecondyear(request):
    return render(request, 'secondyear/eandtcyear.html')


def Civilsecondyear(request):
    return render(request, 'secondyear/civilyear.html')

# third year

def ITthirdyear(request):
    return render(request, 'thirdyear/ityear.html')


def Compthirdyear(request):
    return render(request, 'thirdyear/compyear.html')


def Mechthirdyear(request):
    return render(request, 'thirdyear/mechyear.html')


def Electthirdyear(request):
    return render(request, 'thirdyear/electyear.html')


def Eandtcthirdyear(request):
    return render(request, 'thirdyear/eandtcyear.html')


def Civilthirdyear(request):
    return render(request, 'thirdyear/civilyear.html')

# fourth year
def ITfourthyear(request):
    return render(request, 'fourthyear/ityear.html')


def Compfourthyear(request):
    return render(request, 'fourthyear/compyear.html')


def Mechfourthyear(request):
    return render(request, 'fourthyear/mechyear.html')


def Electfourthyear(request):
    return render(request, 'fourthyear/electyear.html')


def Eandtcfourthyear(request):
    return render(request, 'fourthyear/eandtcyear.html')


def Civilfourthyear(request):
    return render(request, 'fourthyear/civilyear.html')
#five year
def ITfiveyear(request):
    return render(request, 'fiveyear/ityear.html')
# Create your views here.
# Enrollment
def ITfirstyearEnroll(request):
    return render(request,'firstyear/firtyearenroll/itfirstyearenroll.html')

def ITfiveyearEnroll(request):
    return render(request,'firstyear/itfiveyearenroll/itfiveyearenroll.html')

def CompfirstyearEnroll(request):
    return render(request,'firstyear/firtyearenroll/compfirstyearenroll.html')

def MechfirstyearEnroll(request):
    return render(request,'firstyear/firtyearenroll/mechfirstyearenroll.html')

def ElectfirstyearEnroll(request):
    return render(request,'firstyear/firtyearenroll/electfirstyearenroll.html')

def EandtcfirstyearEnroll(request):
    return render(request,'firstyear/firtyearenroll/eandtcfirstyearenroll.html')

def CivilfirstyearEnroll(request):
    return render(request,'firstyear/firtyearenroll/civilfirstyearenroll.html')

# secondyear

def ITsecondyearEnroll(request):
    return render(request,'secondyear/secondyearenroll/itsecondyearenroll.html')

def CompsecondyearEnroll(request):
    return render(request,'secondyear/secondyearenroll/compsecondyearenroll.html')

def MechsecondyearEnroll(request):
    return render(request,'secondyear/secondyearenroll/mechsecondyearenroll.html')

def ElectsecondyearEnroll(request):
    return render(request,'secondyear/secondyearenroll/electsecondyearenroll.html')

def EandtcsecondyearEnroll(request):
    return render(request,'secondyear/secondyearenroll/eandtcsecondyearenroll.html')

def CivilsecondyearEnroll(request):
    return render(request,'secondyear/secondyearenroll/civilsecondyearenroll.html')
# third

def ITthirdyearEnroll(request):
    return render(request,'thirdyear/thirdyearenroll/itthirdyearenroll.html')

def CompthirdyearEnroll(request):
    return render(request,'thirdyear/thirdyearenroll/compthirdyearenroll.html')

def MechthirdyearEnroll(request):
    return render(request,'thirdyear/thirdyearenroll/mechthirdyearenroll.html')

def ElectthirdyearEnroll(request):
    return render(request,'thirdyear/thirdyearenroll/electthirdyearenroll.html')

def EandtcthirdyearEnroll(request):
    return render(request,'thirdyear/thirdyearenroll/eandtcthirdyearenroll.html')

def CivilthirdyearEnroll(request):
    return render(request,'thirdyear/thirdyearenroll/civilthirdyearenroll.html')

# fourth
def ITfourthyearEnroll(request):
    return render(request,'fourthyear/fourthyearenroll/itfourthyearenroll.html')

def CompfourthyearEnroll(request):
    return render(request,'fourthyear/fourthyearenroll/compfourthyearenroll.html')

def MechfourthyearEnroll(request):
    return render(request,'fourthyear/fourthyearenroll/mechfourthyearenroll.html')

def ElectfourthyearEnroll(request):
    return render(request,'fourthyear/fourthyearenroll/electfourthyearenroll.html')

def EandtcfourthyearEnroll(request):
    return render(request,'fourthyear/fourthyearenroll/eandtcfourthyearenroll.html')

def CivilfourthyearEnroll(request):
    return render(request,'fourthyear/fourthyearenroll/civilfourthyearenroll.html')

#
def ITfiveyearEnroll(request):
    return render(request,'fiveyear/fiveyearenroll/itfiveyearenroll.html')

# Code****************************************************************************

def itfyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[1].split(".")[2])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    if(not(os.path.exists('templates/firstyear/firtyearenroll/it/StudentDetails/StudentDetails.csv'))):
        fileName = 'templates/firstyear/firtyearenroll/it/StudentDetails/StudentDetails.csv'
        col_names = ['Id', 'Name','Class']
        attendance = pd.DataFrame(columns=col_names)
        attendance.to_csv(fileName, index=False)
    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    lop = (request.POST.get('Class'))
    numberImage = (request.POST.get('photo'))

    con = sqlite3.connect("db.sqlite3") # change to 'sqlite:///your_filename.db'
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Class (
                        Id          INTEGER,
                        Name        VARCHAR (255) ,
                        Class       VARCHAR (255) ,
                        NumberImage VARCHAR (255) ,
                        PRIMARY KEY(Name,Class)
                    );""")
    a = cur.execute("select count(*) from Class where name = ? and class = ?",(name,lop)).fetchall()
    if(a[0][0] < 1):
        cur.execute("INSERT INTO Class (Id,Name,Class,NumberImage) VALUES(?,?,?,?)",(Id,name,lop,numberImage))
    else:
        b = cur.execute("select NumberImage from Class where name = ? and class = ?",(name,lop)).fetchall()
        if(int(b[0][0]) < int(numberImage)):
            cur.execute("UPDATE Class SET NumberImage = ? WHERE name = ? and class = ?",(numberImage,name,lop))
        else:
            easygui.msgbox("Hãy nhập số ảnh lớn hơn " + b[0][0] + " Vì đã có " + b[0][0] + " ảnh của sinh viên này", title="simple gui")
            return ITfirstyearEnroll(request)
    con.commit()
    con.close()

    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        eyeycascadePath = "templates/haarcascade_eye.xml"
        eye_cascade = cv2.CascadeClassifier(eyeycascadePath)
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret,img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray,minNeighbors=15)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    sampleNum = sampleNum + 1
                    if(not(os.path.exists("templates/firstyear/firtyearenroll/it/TrainingImage/"+lop+"." + name + "." + Id + '.' + str(sampleNum) + ".jpg"))):
                        cv2.imwrite("templates/firstyear/firtyearenroll/it/TrainingImage/"+lop+"." + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h , x:x + w ])
                    cv2.imshow('frame', img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif (sampleNum + 2) > int(numberImage) :
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name + "Lop : " + lop
        row = [Id, name,lop]
        with open('templates/firstyear/firtyearenroll/it/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        df = pd.read_csv('templates/firstyear/firtyearenroll/it/StudentDetails/StudentDetails.csv', usecols=['Id', 'Name','Class']).drop_duplicates(keep='first')
        df.to_csv('templates/firstyear/firtyearenroll/it/StudentDetails/StudentDetails.csv', index=False)
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        #message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    #recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/firstyear/firtyearenroll/it/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/firstyear/firtyearenroll/it/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)


    return render(request,'save.html')
def getImageNumber(request):
    name = (request.POST.get('name'))
    lop = (request.POST.get('Class'))
    con = sqlite3.connect("db.sqlite3") # change to 'sqlite:///your_filename.db'
    cur = con.cursor()
    return cur.execute("select NumberImgae from Class where name = ? and class = ?",(name,lop)).fetchall()
def compfyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting comp to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[1].split(".")[2])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/firstyear/firtyearenroll/comp/TrainingImage/ " + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/firstyear/firtyearenroll/comp/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/firstyear/firtyearenroll/comp/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/firstyear/firtyearenroll/comp/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')
def mechfyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting mech to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/firstyear/firtyearenroll/mech/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/firstyear/firtyearenroll/mech/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/firstyear/firtyearenroll/mech/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/firstyear/firtyearenroll/mech/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')
def electfyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting elect to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/firstyear/firtyearenroll/elect/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/firstyear/firtyearenroll/elect/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/firstyear/firtyearenroll/elect/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/firstyear/firtyearenroll/elect/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)

    return render(request, 'save.html')
def eandtcfyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting eandtc to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.spleandtc(imagePath)[-1].spleandtc(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids

    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/firstyear/firtyearenroll/eandtc/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/firstyear/firtyearenroll/eandtc/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/firstyear/firtyearenroll/eandtc/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/firstyear/firtyearenroll/eandtc/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')
def civilfyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting civil to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/firstyear/firtyearenroll/civil/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.writeKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/firstyear/firtyearenroll/civil/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/firstyear/firtyearenroll/civil/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/firstyear/firtyearenroll/civil/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)

    return render(request, 'save.html')
# second year enrollment************************************

def itsyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[1].split(".")[2])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            passfirst

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    if(not(os.path.exists('templates/secondyear/secondyearenroll/it/StudentDetails/StudentDetails.csv'))):
        fileName = 'templates/secondyear/secondyearenroll/it/StudentDetails/StudentDetails.csv'
        col_names = ['Id', 'Name','Class']
        attendance = pd.DataFrame(columns=col_names)
        attendance.to_csv(fileName, index=False)
    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    lop = (request.POST.get('Class'))
    numberImage = (request.POST.get('photo'))
    
    con = sqlite3.connect("db.sqlite3") # change to 'sqlite:///your_filename.db'
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Class (
                        Id          INTEGER,
                        Name        VARCHAR (255) ,
                        Class       VARCHAR (255) ,
                        NumberImage VARCHAR (255) ,
                        PRIMARY KEY(Name,Class)
                    );""")
    a = cur.execute("select count(*) from Class where name = ? and class = ?",(name,lop)).fetchall()
    if(a[0][0] < 1):
        cur.execute("INSERT INTO Class (Id,Name,Class,NumberImage) VALUES(?,?,?,?)",(Id,name,lop,numberImage))
    else:
        b = cur.execute("select NumberImage from Class where name = ? and class = ?",(name,lop)).fetchall()
        if(int(b[0][0]) < int(numberImage)):
            cur.execute("UPDATE Class SET NumberImage = ? WHERE name = ? and class = ?",(numberImage,name,lop))
        else:
            easygui.msgbox("Hãy nhập số ảnh lớn hơn " + b[0][0] + " Vì đã có " + b[0][0] + " ảnh của sinh viên này", title="simple gui")
            return ITsecondyearEnroll(request)
    con.commit()
    con.close()
    
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        eyeycascadePath = "templates/haarcascade_eye.xml"
        eye_cascade = cv2.CascadeClassifier(eyeycascadePath)
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret,img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray,minNeighbors=15)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    sampleNum = sampleNum + 1
                    if(not(os.path.exists("templates/secondyear/secondyearenroll/it/TrainingImage/"+lop+ '.' + name + "." + Id + '.' + str(sampleNum) + ".jpg"))):
                        cv2.imwrite("templates/secondyear/secondyearenroll/it/TrainingImage/"+lop+ '.' + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                    cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif (sampleNum + 2) > int(numberImage) :
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name + "Lop : " + lop
        row = [Id, name,lop]
        with open('templates/secondyear/secondyearenroll/it/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        df = pd.read_csv('templates/secondyear/secondyearenroll/it/StudentDetails/StudentDetails.csv', usecols=['Id', 'Name','Class']).drop_duplicates(keep='first')
        df.to_csv('templates/secondyear/secondyearenroll/it/StudentDetails/StudentDetails.csv', index=False)
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/secondyear/secondyearenroll/it/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/secondyear/secondyearenroll/it/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)


    return render(request,'save.html')

def compsyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting comp to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/secondyear/secondyearenroll/comp/TrainingImage/ " + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/secondyear/secondyearenroll/comp/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/secondyear/secondyearenroll/comp/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/secondyear/secondyearenroll/comp/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')
def mechsyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting mech to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/secondyear/secondyearenroll/mech/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/secondyear/secondyearenroll/mech/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/secondyear/secondyearenroll/mech/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/secondyear/secondyearenroll/mech/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request,'save.html')

def electsyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting elect to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/secondyear/secondyearenroll/elect/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/secondyear/secondyearenroll/elect/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/secondyear/secondyearenroll/elect/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/secondyear/secondyearenroll/elect/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')

def eandtcsyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting eandtc to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.spleandtc(imagePath)[-1].spleandtc(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids

    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/secondyear/secondyearenroll/eandtc/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/secondyear/secondyearenroll/eandtc/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/secondyear/secondyearenroll/eandtc/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/secondyear/secondyearenroll/eandtc/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')
def civilsyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting civil to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/secondyear/secondyearenroll/civil/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.writeKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/secondyear/secondyearenroll/civil/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/secondyear/secondyearenroll/civil/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/secondyear/secondyearenroll/civil/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')
def ittyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[1].split(".")[2])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    if(not(os.path.exists('templates/thirdyear/thirdyearenroll/it/StudentDetails/StudentDetails.csv'))):
        fileName = 'templates/thirdyear/thirdyearenroll/it/StudentDetails/StudentDetails.csv'
        col_names = ['Id', 'Name','Class']
        attendance = pd.DataFrame(columns=col_names)
        attendance.to_csv(fileName, index=False)
    
    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    lop = (request.POST.get('Class'))

    numberImage = (request.POST.get('photo'))

    con = sqlite3.connect("db.sqlite3") # change to 'sqlite:///your_filename.db'
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Class (
                        Id          INTEGER,
                        Name        VARCHAR (255) ,
                        Class       VARCHAR (255) ,
                        NumberImage VARCHAR (255) ,
                        PRIMARY KEY(Name,Class)
                    );""")
    a = cur.execute("select count(*) from Class where name = ? and class = ?",(name,lop)).fetchall()
    if(a[0][0] < 1):
        cur.execute("INSERT INTO Class (Id,Name,Class,NumberImage) VALUES(?,?,?,?)",(Id,name,lop,numberImage))
    else:
        b = cur.execute("select NumberImage from Class where name = ? and class = ?",(name,lop)).fetchall()
        if(int(b[0][0]) < int(numberImage)):
            cur.execute("UPDATE Class SET NumberImage = ? WHERE name = ? and class = ?",(numberImage,name,lop))
        else:
            easygui.msgbox("Hãy nhập số ảnh lớn hơn " + b[0][0] + " Vì đã có " + b[0][0] + " ảnh của sinh viên này", title="simple gui")
            return ITthirdyearEnroll(request)
    con.commit()
    con.close()

    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        eyeycascadePath = "templates/haarcascade_eye.xml"
        eye_cascade = cv2.CascadeClassifier(eyeycascadePath)
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret,img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray,minNeighbors=15)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    sampleNum = sampleNum + 1
                    if(not(os.path.exists("templates/thirdyear/thirdyearenroll/it/TrainingImage/"+lop+ '.' + name + "." + Id + '.' + str(sampleNum) + ".jpg"))):
                        cv2.imwrite("templates/thirdyear/thirdyearenroll/it/TrainingImage/"+lop+ '.' + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                    cv2.imshow('frame', img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif (sampleNum + 2) > int(numberImage) :
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name + "Lop : " + lop
        row = [Id, name,lop]
        with open('templates/thirdyear/thirdyearenroll/it/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        df = pd.read_csv('templates/thirdyear/thirdyearenroll/it/StudentDetails/StudentDetails.csv', usecols=['Id', 'Name','Class']).drop_duplicates(keep='first')
        df.to_csv('templates/thirdyear/thirdyearenroll/it/StudentDetails/StudentDetails.csv', index=False)
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/thirdyear/thirdyearenroll/it/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/thirdyear/thirdyearenroll/it/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)


    return render(request,'save.html')

def comptyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting comp to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/thirdyear/thirdyearenroll/comp/TrainingImage/ " + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/thirdyear/thirdyearenroll/comp/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/thirdyear/thirdyearenroll/comp/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/thirdyear/thirdyearenroll/comp/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')
def mechtyenroll(request):

    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting mech to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/thirdyear/thirdyearenroll/mech/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/thirdyear/thirdyearenroll/mech/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/thirdyear/thirdyearenroll/mech/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/thirdyear/thirdyearenroll/mech/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')
def electtyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting elect to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/thirdyear/thirdyearenroll/elect/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/thirdyear/thirdyearenroll/elect/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/thirdyear/thirdyearenroll/elect/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/thirdyear/thirdyearenroll/elect/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')

def eandtctyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting eandtc to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.spleandtc(imagePath)[-1].spleandtc(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids

    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/thirdyear/thirdyearenroll/eandtc/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/thirdyear/thirdyearenroll/eandtc/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/thirdyear/thirdyearenroll/eandtc/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/thirdyear/thirdyearenroll/eandtc/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')
def civiltyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting civil to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/thirdyear/thirdyearenroll/civil/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.writeKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/thirdyear/thirdyearenroll/civil/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/thirdyear/thirdyearenroll/civil/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/thirdyear/thirdyearenroll/civil/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')

def itlyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[1].split(".")[2])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    if(not(os.path.exists('templates/fourthyear/fourthyearenroll/it/StudentDetails/StudentDetails.csv'))):
        fileName = 'templates/fourthyear/fourthyearenroll/it/StudentDetails/StudentDetails.csv'
        col_names = ['Id', 'Name','Class']
        attendance = pd.DataFrame(columns=col_names)
        attendance.to_csv(fileName, index=False)
    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    lop = (request.POST.get('Class'))

    numberImage = (request.POST.get('photo'))

    con = sqlite3.connect("db.sqlite3") # change to 'sqlite:///your_filename.db'
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Class (
                        Id          INTEGER,
                        Name        VARCHAR (255) ,
                        Class       VARCHAR (255) ,
                        NumberImage VARCHAR (255) ,
                        PRIMARY KEY(Name,Class)
                    );""")
    a = cur.execute("select count(*) from Class where name = ? and class = ?",(name,lop)).fetchall()
    if(a[0][0] < 1):
        cur.execute("INSERT INTO Class (Id,Name,Class,NumberImage) VALUES(?,?,?,?)",(Id,name,lop,numberImage))
    else:
        b = cur.execute("select NumberImage from Class where name = ? and class = ?",(name,lop)).fetchall()
        if(int(b[0][0]) < int(numberImage)):
            cur.execute("UPDATE Class SET NumberImage = ? WHERE name = ? and class = ?",(numberImage,name,lop))
        else:
            easygui.msgbox("Hãy nhập số ảnh lớn hơn " + b[0][0] + " Vì đã có " + b[0][0] + " ảnh của sinh viên này", title="simple gui")
            return ITfourthyearEnroll(request)
    con.commit()
    con.close()

    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        eyeycascadePath = "templates/haarcascade_eye.xml"
        eye_cascade = cv2.CascadeClassifier(eyeycascadePath)
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret,img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray,minNeighbors=15)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    sampleNum = sampleNum + 1
                    if(not(os.path.exists("templates/fourthyear/fourthyearenroll/it/TrainingImage/"+lop+ '.' + name + "." + Id + '.' + str(sampleNum) + ".jpg"))):
                        cv2.imwrite("templates/fourthyear/fourthyearenroll/it/TrainingImage/"+lop+ '.' + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                    cv2.imshow('frame', img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif (sampleNum + 2) > int(numberImage) :
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name + " Lop : " + lop
        row = [Id, name,lop]
        with open('templates/fourthyear/fourthyearenroll/it/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        df = pd.read_csv('templates/fourthyear/fourthyearenroll/it/StudentDetails/StudentDetails.csv', usecols=['Id', 'Name','Class']).drop_duplicates(keep='first')
        df.to_csv('templates/fourthyear/fourthyearenroll/it/StudentDetails/StudentDetails.csv', index=False)
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/fourthyear/fourthyearenroll/it/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/fourthyear/fourthyearenroll/it/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    conn = sqlite3.connect('db.sqlite3')
    cur = conn.cursor() 
    time = datetime.datetime.now()

    return render(request,'save.html')

def complyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting comp to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/fourthyear/fourthyearenroll/comp/TrainingImage/ " + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/fourthyear/fourthyearenroll/comp/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/fourthyear/fourthyearenroll/comp/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/fourthyear/fourthyearenroll/comp/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')

def mechlyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting mech to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/fourthyear/fourthyearenroll/mech/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/fourthyear/fourthyearenroll/mech/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/fourthyear/fourthyearenroll/mech/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/fourthyear/fourthyearenroll/mech/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')

def electlyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting elect to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/fourthyear/fourthyearenroll/elect/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/fourthyear/fourthyearenroll/elect/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/fourthyear/fourthyearenroll/elect/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/fourthyear/fourthyearenroll/elect/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')

def eandtclyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting eandtc to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.spleandtc(imagePath)[-1].spleandtc(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids

    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/fourthyear/fourthyearenroll/eandtc/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg",
                                gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/fourthyear/fourthyearenroll/eandtc/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/fourthyear/fourthyearenroll/eandtc/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/fourthyear/fourthyearenroll/eandtc/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)
    return render(request, 'save.html')
def civillyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting civil to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[-1].split(".")[1])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False


    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)

                sampleNum = sampleNum + 1

                cv2.imwrite("templates/fourthyear/fourthyearenroll/civil/TrainingImage/" + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])

                cv2.imshow('frame', img)

            if cv2.writeKey(100) & 0xFF == ord('q'):
                break

            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name
        row = [Id, name]
        with open('templates/fourthyear/fourthyearenroll/civil/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/fourthyear/fourthyearenroll/civil/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/fourthyear/thirdyearenroll/civil/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)

    return render(request, 'save.html')



def itfytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    if(os.path.exists("templates/firstyear/firtyearenroll/it/TrainingImageLabel/Trainner.yml")):
        recognizer.read("templates/firstyear/firtyearenroll/it/TrainingImageLabel/Trainner.yml")
        harcascadePath = "login/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);
        df = pd.read_csv("templates/firstyear/firtyearenroll/it/StudentDetails/StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', 'Name','Class', 'Date', 'Time']
        attendance = pd.DataFrame(columns=col_names)
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
                Id, conf = recognizer.predict(gray[y:y + h , x:x + w])
                if (conf < 40):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['Id'] == Id]['Name'].values
                    lop = df.loc[df['Id'] == Id]['Class'].values
                    tt = str(Id) + "-" + aa
                    attendance.loc[len(attendance)] = [Id, aa[0],lop[0], date, timeStamp]

                else:
                    Id = 'Unknown'
                    tt = str(Id)
                if (conf > 75):
                    noOfFile = len(os.listdir("ImagesUnknown")) + 1
                    cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
                cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
            attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
            cv2.imshow('im', im)
            if (cv2.waitKey(1) == ord('q')):
                break
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")
        fileName = "templates/firstyear/firtyearenroll/it/Attendance/Attendance_IT_FY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
        attendance.to_csv(fileName, index=False)
        cam.release()
        cv2.destroyAllWindows()
        # print(attendance)
        res = attendance
        # message2.configure(text=res)
        con = sqlite3.connect("db.sqlite3") # change to 'sqlite:///your_filename.db'
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS DiemDanh (Id int,Name varchar,Class varchar,Date datetime,Time varchar,PRIMARY KEY(Name,Class,Date))""")
        with open(fileName,'r') as fin: # `with` statement available in 2.5+
            # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin) # comma is default delimiter
            to_db = [(i['Id'], i['Name'],i['Class'],i['Date'],i['Time']) for i in dr]
        for i in to_db:
            print(i[1], i[3])
            a = cur.execute("select count(*) from DiemDanh where name = ? and date = ? and class = ?",(i[1],i[3],i[2])).fetchall()
            if(a[0][0] < 1):
                cur.execute("INSERT INTO DiemDanh (Id,Name,Class,Date,Time) VALUES(?,?,?,?,?)",i)
            else:
                easygui.msgbox("Da diem danh sinh vien "+ i[1] +" nay", title="simple gui")
                continue
        con.commit()
        con.close()
        return render(request,'save.html')
    else:
        easygui.msgbox("Chua co file model tranning vui long enroll sinh vien", title="simple gui")
        return render(request, 'fail.html')

def compfytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/firstyear/firtyearenroll/comp/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/firstyear/firtyearenroll/comp/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/firstyear/firtyearenroll/comp/Attendance/Attendance_Comp_FY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request,'save.html')
def mechfytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/firstyear/firtyearenroll/mech/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/firstyear/firtyearenroll/mech/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/firstyear/firtyearenroll/mech/Attendance/Attendance_Mech_FY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request,'save.html')

def electfytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/firstyear/firtyearenroll/elect/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/firstyear/firtyearenroll/elect/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/firstyear/firtyearenroll/elect/Attendance/Attendance_Elect_FY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request,'save.html')

def eandtcfytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/firstyear/firtyearenroll/eandtc/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/firstyear/firtyearenroll/eandtc/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/firstyear/firtyearenroll/eandtc/Attendance/Attendance_EandTC_FY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request, 'save.html')
def civilfytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/firstyear/firtyearenroll/civil/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/firstyear/firtyearenroll/civil/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/firstyear/firtyearenroll/civil/Attendance/Attendance_Civil_FY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request,'save.html')

def itsytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    if(os.path.exists("templates/secondyear/secondyearenroll/it/TrainingImageLabel/Trainner.yml")):
        recognizer.read("templates/secondyear/secondyearenroll/it/TrainingImageLabel/Trainner.yml")
        harcascadePath = "login/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);
        df = pd.read_csv("templates/secondyear/secondyearenroll/it/StudentDetails/StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', 'Name','Class', 'Date', 'Time']
        attendance = pd.DataFrame(columns=col_names)
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
                Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['Id'] == Id]['Name'].values
                    lop = df.loc[df['Id'] == Id]['Class'].values
                    tt = str(Id) + "-" + aa
                    attendance.loc[len(attendance)] = [Id, aa[0],lop[0], date, timeStamp]

                else:
                    Id = 'Unknown'
                    tt = str(Id)
                if (conf > 75):
                    noOfFile = len(os.listdir("ImagesUnknown")) + 1
                    cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
                cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
            attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
            cv2.imshow('im', im)
            if (cv2.waitKey(1) == ord('q')):
                break
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")
        fileName = "templates/secondyear/secondyearenroll/it/Attendance/Attendance_IT_SY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
        attendance.to_csv(fileName, index=False)
        cam.release()
        cv2.destroyAllWindows()
        # print(attendance)
        res = attendance
        # message2.configure(text=res)
        con = sqlite3.connect("db.sqlite3") # change to 'sqlite:///your_filename.db'
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS DiemDanh (Id int,Name varchar,Class varchar,Date datetime,Time varchar,PRIMARY KEY(Name,Class,Date))""")
        with open(fileName,'r') as fin: # `with` statement available in 2.5+
            # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin) # comma is default delimiter
            to_db = [(i['Id'], i['Name'],i['Class'],i['Date'],i['Time']) for i in dr]
        for i in to_db:
            print(i[1], i[3])
            a = cur.execute("select count(*) from DiemDanh where name = ? and date = ? and class = ?",(i[1],i[3],i[2])).fetchall()
            if(a[0][0] < 1):
                cur.execute("INSERT INTO DiemDanh (Id,Name,Class,Date,Time) VALUES(?,?,?,?,?)",i)
            else:
                easygui.msgbox("Da diem danh sinh vien "+ i[1] +"  nay", title="simple gui")
                continue
        con.commit()
        con.close()
        return render(request,'save.html')
    else:
        easygui.msgbox("Chua co file model tranning vui long enroll sinh vien", title="simple gui")
        return render(request, 'fail.html')
def compsytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/secondyear/secondyearenroll/comp/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/secondyear/secondyearenroll/comp/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/secondyear/secondyearenroll/comp/Attendance/Attendance_Comp_SY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request,'save.html')

def mechsytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/secondyear/secondyearenroll/mech/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/secondyear/secondyearenroll/mech/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/secondyear/secondyearenroll/mech/Attendance/Attendance_Mech_SY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request,'save.html')
def electsytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/secondyear/secondyearenroll/elect/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/secondyear/secondyearenroll/elect/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/secondyear/secondyearenroll/elect/Attendance/Attendance_Elect_SY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)
    return render(request, 'save.html')
def eandtcsytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/secondyear/secondyearenroll/eandtc/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/secondyear/secondyearenroll/eandtc/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/secondyear/secondyearenroll/eandtc/Attendance/Attendance_EandTC_SY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request,'save.html')

def civilsytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/secondyear/secondyearenroll/covil/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/secondyear/secondyearenroll/civil/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/secondyear/secondyearenroll/civil/Attendance/Attendance_Civil_SY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request,'save.html')

def ittytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    if(os.path.exists("templates/thirdyear/thirdyearenroll/it/TrainingImageLabel/Trainner.yml")):
        recognizer.read("templates/thirdyear/thirdyearenroll/it/TrainingImageLabel/Trainner.yml")
        harcascadePath = "login/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);
        df = pd.read_csv("templates/thirdyear/thirdyearenroll/it/StudentDetails/StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', 'Name','Class', 'Date', 'Time']
        attendance = pd.DataFrame(columns=col_names)
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
                Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['Id'] == Id]['Name'].values
                    lop = df.loc[df['Id'] == Id]['Class'].values
                    tt = str(Id) + "-" + aa
                    attendance.loc[len(attendance)] = [Id, aa[0],lop[0], date, timeStamp]

                else:
                    Id = 'Unknown'
                    tt = str(Id)
                if (conf > 75):
                    noOfFile = len(os.listdir("ImagesUnknown")) + 1
                    cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
                cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
            attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
            cv2.imshow('im', im)
            if (cv2.waitKey(1) == ord('q')):
                break
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")
        fileName = "templates/thirdyear/thirdyearenroll/it/Attendance/Attendance_IT_TY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
        attendance.to_csv(fileName, index=False)
        cam.release()
        cv2.destroyAllWindows()
        # print(attendance)
        res = attendance
        # message2.configure(text=res)
        con = sqlite3.connect("db.sqlite3") # change to 'sqlite:///your_filename.db'
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS DiemDanh (Id int,Name varchar,Class varchar,Date datetime,Time varchar,PRIMARY KEY(Name,Class,Date))""")
        with open(fileName,'r') as fin: # `with` statement available in 2.5+
            # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin) # comma is default delimiter
            to_db = [(i['Id'], i['Name'],i['Class'],i['Date'],i['Time']) for i in dr]
        for i in to_db:
            print(i[1], i[3])
            a = cur.execute("select count(*) from DiemDanh where name = ? and date = ? and class = ? ",(i[1],i[3],i[2])).fetchall()
            if(a[0][0] < 1):
                cur.execute("INSERT INTO DiemDanh (Id,Name,Class,Date,Time) VALUES(?,?,?,?,?)",i)
            else:
                easygui.msgbox("Da diem danh sinh vien "+ i[1] +" nay", title="simple gui")
                continue
        con.commit()
        con.close()
        return render(request,'save.html')
    else:
        easygui.msgbox("Chua co file model tranning vui long enroll sinh vien", title="simple gui")
        return render(request, 'fail.html')

def comptytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/thirdyear/thirdyearenroll/comp/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/thirdyear/thirdyearenroll/comp/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/thirdyear/thirdyearenroll/comp/Attendance/Attendance_Comp_TY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request, 'save.html')

def mechtytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/thirdyear/thirdyearenroll/mech/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/thirdyear/thirdyearenroll/mech/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/thirdyear/thirdyearenroll/mech/Attendance/Attendance_Mech_TY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request,'save.html')

def electtytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/thirdyear/thirdyearenroll/elect/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/thirdyear/thirdyearenroll/elect/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/thirdyear/thirdyearenroll/elect/Attendance/Attendance_Elect_TY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)
    return render(request,'save.html')

def eandtctytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/thirdyear/thirdyearenroll/eandtc/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/thirdyear/thirdyearenroll/eandtc/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/secondyear/thirdyearenroll/eandtc/Attendance/Attendance_EandTC_TY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request,'save.html')

def civiltytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/thirdyear/thirdyearenroll/civil/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/thirdyear/thirdyearenroll/civil/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/thirdyear/thirdyearenroll/civil/Attendance/Attendance_Civil_TY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request,'save.html')

def itlytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    if(os.path.exists("templates/fourthyear/fourthyearenroll/it/TrainingImageLabel/Trainner.yml")):
        recognizer.read("templates/fourthyear/fourthyearenroll/it/TrainingImageLabel/Trainner.yml")
        harcascadePath = "login/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);
        df = pd.read_csv("templates/fourthyear/fourthyearenroll/it/StudentDetails/StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', 'Name','Class', 'Date', 'Time']
        attendance = pd.DataFrame(columns=col_names)
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
                Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['Id'] == Id]['Name'].values
                    lop = df.loc[df['Id'] == Id]['Class'].values
                    tt = str(Id) + "-" + aa
                    attendance.loc[len(attendance)] = [Id, aa[0],lop[0], date, timeStamp]

                else:
                    Id = 'Unknown'
                    tt = str(Id)
                if (conf > 75):
                    noOfFile = len(os.listdir("ImagesUnknown")) + 1
                    cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
                cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
            attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
            cv2.imshow('im', im)
            if (cv2.waitKey(1) == ord('q')):
                break
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")
        fileName = "templates/fourthyear/fourthyearenroll/it/Attendance/Attendance_IT_lY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
        attendance.to_csv(fileName, index=False)
        cam.release()
        cv2.destroyAllWindows()
        # print(attendance)
        res = attendance
        # message2.configure(text=res)
        con = sqlite3.connect("db.sqlite3") # change to 'sqlite:///your_filename.db'
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS DiemDanh (Id int,Name varchar,Class varchar,Date datetime,Time varchar,PRIMARY KEY(Name,Class,Date))""")
        with open(fileName,'r') as fin: # `with` statement available in 2.5+
            # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin) # comma is default delimiter
            to_db = [(i['Id'], i['Name'],i['Class'],i['Date'],i['Time']) for i in dr]
        for i in to_db:
            print(i[1], i[3])
            a = cur.execute("select count(*) from DiemDanh where name = ? and date = ? and class = ?",(i[1],i[3],i[2])).fetchall()
            if(a[0][0] < 1):
                cur.execute("INSERT INTO DiemDanh (Id,Name,Class,Date,Time) VALUES(?,?,?,?,?)",i)
            else:
                easygui.msgbox("Da diem danh sinh vien "+ i[1] +" nay", title="simple gui")
                continue
        con.commit()
        con.close()
        return render(request,'save.html')
    else:
        easygui.msgbox("Chua co file model tranning vui long enroll sinh vien", title="simple gui")
        return render(request, 'fail.html')

def complytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/fourthyear/fourthyearenroll/comp/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/fourthyear/fourthyearenroll/comp/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/fourthyear/fourthyearenroll/comp/Attendance/Attendance_Comp_lY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request, 'save.html')
def mechlytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/fourthyear/fourthyearenroll/mech/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/fourthyear/fourthyearenroll/mech/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/fourthyear/fourthyearenroll/mech/Attendance/Attendance_Mech_lY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request,'save.html')

def electlytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/fourthyear/fourthyearenroll/elect/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/fourthyear/fourthyearenroll/elect/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/fourthyear/fourthyearenroll/elect/Attendance/Attendance_Elect_lY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)

    return render(request,'save.html')

def eandtclytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/fourthyear/fourthyearenroll/eandtc/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    df = pd.read_csv("templates/fourthyear/fourthyearenroll/eandtc/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/fourthyear/fourthyearenroll/eandtc/Attendance/Attendance_EandTC_lY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)
    return render(request,'save.html')

def civillytrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    recognizer.read("templates/fourthyear/fourthyearenroll/civil/TrainingImageLabel/Trainner.yml")
    harcascadePath = "login/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    df = pd.read_csv("templates/fourthyear/fourthyearenroll/civil/StudentDetails/StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ['Id', 'Name', 'Date', 'Time']
    attendance = pd.DataFrame(columns=col_names)
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf < 50):
                ts = time.time()
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa = df.loc[df['Id'] == Id]['Name'].values
                tt = str(Id) + "-" + aa
                attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

            else:
                Id = 'Unknown'
                tt = str(Id)
            if (conf > 75):
                noOfFile = len(os.listdir("ImagesUnknown")) + 1
                cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
            cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
        attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
        cv2.imshow('im', im)
        if (cv2.waitKey(1) == ord('q')):
            break
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour, Minute, Second = timeStamp.split(":")
    fileName = "templates/fourthyear/fourthyearenroll/civil/Attendance/Attendance_Civil_lY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
    attendance.to_csv(fileName, index=False)
    cam.release()
    cv2.destroyAllWindows()
    # print(attendance)
    res = attendance
    # message2.configure(text=res)
    return render(request,'save.html')

def itfiveyenroll(request):
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]

        faces = []

        Ids = []
        # now looping through all the image paths and loading the Ids and the images
        for imagePath in imagePaths:
            # loading the image and converting it to gray scale
            pilImage = Image.open(imagePath).convert('L')
            # Now we are converting the PIL image into numpy array
            imageNp = np.array(pilImage, 'uint8')
            # getting the Id from the image
            Id = int(os.path.split(imagePath)[1].split(".")[2])
            # extract the face from the training image sample
            faces.append(imageNp)
            Ids.append(Id)
        return faces, Ids
    def clear():
        request.POST.get('ID').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def clear2():
        request.POST.get('name').delete(0, 'end')
        res = ""
        message.configure(text=res)

    def is_number(s):
        try:
            float(s)
            return True
        except ValueError:
            pass

        try:
            import unicodedata
            unicodedata.numeric(s)
            return True
        except (TypeError, ValueError):
            pass

        return False

    if(not(os.path.exists('templates/fiveyear/fiveyearenroll/it/StudentDetails/StudentDetails.csv'))):
        fileName = 'templates/fiveyear/fiveyearenroll/it/StudentDetails/StudentDetails.csv'
        col_names = ['Id', 'Name','Class']
        attendance = pd.DataFrame(columns=col_names)
        attendance.to_csv(fileName, index=False)
    Id = (request.POST.get('ID'))
    name = (request.POST.get('name'))
    lop = (request.POST.get('Class'))

    numberImage = (request.POST.get('photo'))

    con = sqlite3.connect("db.sqlite3") # change to 'sqlite:///your_filename.db'
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS Class (
                        Id          INTEGER,
                        Name        VARCHAR (255) ,
                        Class       VARCHAR (255) ,
                        NumberImage VARCHAR (255) ,
                        PRIMARY KEY(Name,Class)
                    );""")
    a = cur.execute("select count(*) from Class where name = ? and class = ?",(name,lop)).fetchall()
    if(a[0][0] < 1):
        cur.execute("INSERT INTO Class (Id,Name,Class,NumberImage) VALUES(?,?,?,?)",(Id,name,lop,numberImage))
    else:
        b = cur.execute("select NumberImage from Class where name = ? and class = ?",(name,lop)).fetchall()
        if(int(b[0][0]) < int(numberImage)):
            cur.execute("UPDATE Class SET NumberImage = ? WHERE name = ? and class = ?",(numberImage,name,lop))
        else:
            easygui.msgbox("Hãy nhập số ảnh lớn hơn " + b[0][0] + " Vì đã có " + b[0][0] + " ảnh của sinh viên này", title="simple gui")
            return ITfiveyearEnroll(request)
    con.commit()
    con.close()

    if (is_number(Id) and name != ''):
        cam = cv2.VideoCapture(0)
        harcascadePath = "templates/haarcascade_frontalface_default.xml"
        eyeycascadePath = "templates/haarcascade_eye.xml"
        eye_cascade = cv2.CascadeClassifier(eyeycascadePath)
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret,img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray,minNeighbors=15)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    sampleNum = sampleNum + 1
                    if(not(os.path.exists("templates/fiveyear/fiveyearenroll/it/TrainingImage/"+lop+"." + name + "." + Id + '.' + str(sampleNum) + ".jpg"))):
                        cv2.imwrite("templates/fiveyear/fiveyearenroll/it/TrainingImage/"+lop+"." + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                    cv2.imshow('frame', img)
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break

            elif (sampleNum + 2) > int(numberImage) :
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for ID : " + Id + " Name : " + name + "Lop : " + lop
        row = [Id, name,lop]
        with open('templates/fiveyear/fiveyearenroll/it/StudentDetails/StudentDetails.csv', 'a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        df = pd.read_csv('templates/fiveyear/fiveyearenroll/it/StudentDetails/StudentDetails.csv', usecols=['Id', 'Name','Class']).drop_duplicates(keep='first')
        df.to_csv('templates/fiveyear/fiveyearenroll/it/StudentDetails/StudentDetails.csv', index=False)
        # message.configure(text=res)
    elif (is_number(Id)):
        res = "Enter Numeric Id"
        #message.configure(text=res)
        easygui.msgbox("Enter Alphabetical Name", title="simple gui")

        if name == '':
            easygui.msgbox("Name field is empty", title="simple gui")

    elif (name.isalpha()):
        res = "Enter Alphabetical Name"
        message.configure(text=res)
        easygui.msgbox("Enter Numaric Id", title="simple gui")
        if Id == '':
            easygui.msgbox("Id is empty", title="simple gui")
    elif Id == '':
        easygui.msgbox("Id is empty", title="simple gui")
    elif name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    elif Id == '' and name == '':
        easygui.msgbox("Name field is empty", title="simple gui")
    else:
        easygui.msgbox("Invalid fields", title="simple gui")

    recognizer = cv2.face_LBPHFaceRecognizer.create()  # recognizer = cv2.face.LBPHFaceRecognizer_create()#$cv2.createLBPHFaceRecognizer()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(harcascadePath)
    faces, Id = getImagesAndLabels("templates/fiveyear/fiveyearenroll/it/TrainingImage")
    recognizer.train(faces, np.array(Id))
    recognizer.save("templates/fiveyear/fiveyearenroll/it/TrainingImageLabel/Trainner.yml")
    print('images trained')
    res = "Image Trained"  # +",".join(str(f) for f in Id)
    # message.configure(text=res)


    return render(request,'save.html')

def itfiveyeartrack(request):
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
    if(os.path.exists("templates/fiveyear/fiveyearenroll/it/TrainingImageLabel/Trainner.yml")):
        check = recognizer.read("templates/fiveyear/fiveyearenroll/it/TrainingImageLabel/Trainner.yml")
        harcascadePath = "login/haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath);
        df = pd.read_csv("templates/fiveyear/fiveyearenroll/it/StudentDetails/StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', 'Name','Class', 'Date', 'Time']
        attendance = pd.DataFrame(columns=col_names)
        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(im,(x+15,y+10),(x+w+15,y+h+27),(225,0,0),2)
                Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
                if (conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['Id'] == Id]['Name'].values
                    lop = df.loc[df['Id'] == Id]['Class'].values
                    tt = str(Id) + "-" + aa
                    attendance.loc[len(attendance)] = [Id, aa[0],lop[0], date, timeStamp]

                else:
                    Id = 'Unknown'
                    tt = str(Id)
                if (conf > 75):
                    noOfFile = len(os.listdir("ImagesUnknown")) + 1
                    cv2.imwrite("ImagesUnknown\Image" + str(noOfFile) + ".jpg", im[y:y + h, x:x + w])
                cv2.putText(im, str(tt), (x, y + h), font, 1, (255, 255, 255), 2)
            attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
            cv2.imshow('im', im)
            if (cv2.waitKey(1) == ord('q')):
                break
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")
        fileName = "templates/fiveyear/fiveyearenroll/it/Attendance/Attendance_IT_FY_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
        attendance.to_csv(fileName, index=False)
        cam.release()
        cv2.destroyAllWindows()
        # print(attendance)
        res = attendance
        # message2.configure(text=res)
        con = sqlite3.connect("db.sqlite3") # change to 'sqlite:///your_filename.db'
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS DiemDanh (Id int,Name varchar,Class varchar,Date datetime,Time varchar,PRIMARY KEY(Name,Class,Date))""")
        with open(fileName,'r') as fin: # `with` statement available in 2.5+
            # csv.DictReader uses first line in file for column headings by default
            dr = csv.DictReader(fin) # comma is default delimiter
            to_db = [(i['Id'], i['Name'],i['Class'],i['Date'],i['Time']) for i in dr]
        for i in to_db:
            print(i[1], i[3])
            a = cur.execute("select count(*) from DiemDanh where name = ? and date = ? and class = ?",(i[1],i[3],i[2])).fetchall()
            if(a[0][0] < 1):
                cur.execute("INSERT INTO DiemDanh (Id,Name,Class,Date,Time) VALUES(?,?,?,?,?)",i)
            else:
                easygui.msgbox("Da diem danh sinh vien "+ i[1] +" nay", title="simple gui")
                continue
        con.commit()
        con.close()
        return render(request,'save.html')
    else:
        easygui.msgbox("Chua co file model tranning vui long enroll sinh vien", title="simple gui")
        return render(request, 'fail.html')