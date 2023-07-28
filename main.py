from tkinter import *
from tkinter import filedialog
import tkinter.scrolledtext as st
from tkinter import ttk
import text2emotion as te
import nltk
import vlc
import pafy
#nltk.download('omw-1.4')
import webbrowser
import sys
import mysql.connector
mysqldb = mysql.connector.connect(host="localhost", user="root",password="", database="chatbot")


import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np

from keras.models import load_model
model = load_model('chatbot_model.h5')
import json
import random
intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))



def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res

def play_button1():
    global media
    global res
    print(res)
    if res[0]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox3.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (happy) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[1]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox3.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (angry) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[2]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox3.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (suprise) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[3]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox3.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (sad) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[4]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox3.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (fear) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
def play_button2():
    global media
    global res
    print(res)
    if res[0]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox4.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (happy) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[1]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox4.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (angry) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[2]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox4.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (suprise) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[3]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox4.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (sad) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[4]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox4.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (fear) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()

def play_button3():
    global media
    global res
    print(res)
    if res[0]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox5.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (happy) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[1]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox5.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (angry) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[2]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox5.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (suprise) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[3]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox5.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (sad) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[4]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox5.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (fear) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()

def play_button4():
    global media
    global res
    print(res)
    if res[0]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox6.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (happy) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[1]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox6.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (angry) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[2]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox6.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (suprise) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[3]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox6.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (sad) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[4]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox6.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (fear) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
def play_button5():
    global media
    global res
    print(res)
    if res[0]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox7.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (happy) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[1]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox7.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (angry) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[2]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox7.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (suprise) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[3]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox7.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (sad) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()
    if res[4]==1.0:
        mycursor = mysqldb.cursor()
        inputValue=EntryBox7.get("1.0","end-1c")
        sdd=str(inputValue)
        sql = "INSERT INTO recentlyplayed (fear) VALUES (%s)"
        val = [(sdd)]
        mycursor.execute(sql, val)
        mysqldb.commit()
        url = inputValue
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.play()   
def rplay_button1():
    global media
    inputValue=EntryBox8.get("1.0","end-1c")
    url = inputValue
    video = pafy.new(url)
    best = video.getbest()
    media = vlc.MediaPlayer(best.url)
    media.play()   
def rplay_button2():
    global media
    inputValue=EntryBox9.get("1.0","end-1c")
    url = inputValue
    video = pafy.new(url)
    best = video.getbest()
    media = vlc.MediaPlayer(best.url)
    media.play()
def rplay_button3():
    global media
    inputValue=EntryBox10.get("1.0","end-1c")
    url = inputValue
    video = pafy.new(url)
    best = video.getbest()
    media = vlc.MediaPlayer(best.url)
    media.play()
def rplay_button4():
    global media
    inputValue=EntryBox11.get("1.0","end-1c")
    url = inputValue
    video = pafy.new(url)
    best = video.getbest()
    media = vlc.MediaPlayer(best.url)
    media.play()
def rplay_button5():
    global media
    inputValue=EntryBox12.get("1.0","end-1c")
    url = inputValue
    video = pafy.new(url)
    best = video.getbest()
    media = vlc.MediaPlayer(best.url)
    media.play()
    

def play_stop():
    global media
    media.stop()
def send():
    global res
    msg = EntryBox1.get("1.0",'end-1c').strip()
    output=te.get_emotion(msg)
    res = list(output.values())
    if res[0]==1.0:
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT happy FROM newplaylist")
        myresult = mycursor.fetchall()
        nplylist=[]
        cnt=1
        for x in myresult:            
            sd = str(x).replace('(','').replace(')','').replace(',','').replace("'", "")
            if sd=="":
                print("empty")
            else:
                if cnt==1:
                    EntryBox3.delete("0.0",END)
                    EntryBox8.delete("0.0",END)
                    EntryBox3.insert(INSERT,sd)
                if cnt==2:
                    EntryBox4.delete("0.0",END)
                    EntryBox9.delete("0.0",END)
                    EntryBox4.insert(INSERT,sd)
                if cnt==3:
                    EntryBox5.delete("0.0",END)
                    EntryBox10.delete("0.0",END)
                    EntryBox5.insert(INSERT,sd)
                if cnt==4:
                    EntryBox6.delete("0.0",END)
                    EntryBox11.delete("0.0",END)
                    EntryBox6.insert(INSERT,sd)
                if cnt==5:
                    EntryBox7.delete("0.0",END)
                    EntryBox12.delete("0.0",END)
                    EntryBox7.insert(INSERT,sd)
                cnt=cnt+1
            mycursor.execute("SELECT happy FROM recentlyplayed")
            rmyresult = mycursor.fetchall()
            rcntplyst = []
            for i in rmyresult:
                if i not in rcntplyst:
                    rcntplyst.append(i)
            ctt=1
            for rx in rcntplyst:            
                rsd = str(rx).replace('(','').replace(')','').replace(',','').replace("'", "")
                if rsd=="":
                    print("empty")
                else:
                    print(rsd)
                    if ctt==1:
                        EntryBox8.delete("0.0",END)
                        EntryBox8.insert(INSERT,rsd)
                    if ctt==2:
                        EntryBox9.delete("0.0",END)
                        EntryBox9.insert(INSERT,rsd)
                    if ctt==3:
                        EntryBox10.delete("0.0",END)
                        EntryBox10.insert(INSERT,rsd)
                    if ctt==4:
                        EntryBox11.delete("0.0",END)
                        EntryBox11.insert(INSERT,rsd)
                    if ctt==5:
                        EntryBox12.delete("0.0",END)
                        EntryBox12.insert(INSERT,rsd)
                    ctt=ctt+1


    if res[1]==1.0:
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT angry FROM newplaylist")
        myresult = mycursor.fetchall()
        nplylist=[]
        cnt=1
        for x in myresult:            
            sd = str(x).replace('(','').replace(')','').replace(',','').replace("'", "")
            if sd=="":
                print("empty")
            else:
                if cnt==1:
                    EntryBox3.delete("0.0",END)
                    EntryBox8.delete("0.0",END)
                    EntryBox3.insert(INSERT,sd)

                if cnt==2:
                    EntryBox4.delete("0.0",END)
                    EntryBox9.delete("0.0",END)
                    EntryBox4.insert(INSERT,sd)

                if cnt==3:
                    EntryBox5.delete("0.0",END)
                    EntryBox10.delete("0.0",END)
                    EntryBox5.insert(INSERT,sd)

                if cnt==4:
                    EntryBox6.delete("0.0",END)
                    EntryBox11.delete("0.0",END)
                    EntryBox6.insert(INSERT,sd)
                    
                if cnt==5:
                    EntryBox7.delete("0.0",END)
                    EntryBox12.delete("0.0",END)
                    EntryBox7.insert(INSERT,sd)

                cnt=cnt+1
            mycursor.execute("SELECT angry FROM recentlyplayed")
            rmyresult = mycursor.fetchall()
            rcntplyst = []
            for i in rmyresult:
                if i not in rcntplyst:
                    rcntplyst.append(i)
            ctt=1
            for rx in rcntplyst:            
                rsd = str(rx).replace('(','').replace(')','').replace(',','').replace("'", "")
                if rsd=="":
                    print("empty")
                else:
                    print(rsd)
                    if ctt==1:
                        EntryBox8.delete("0.0",END)
                        EntryBox8.insert(INSERT,rsd)
                    if ctt==2:
                        EntryBox9.delete("0.0",END)
                        EntryBox9.insert(INSERT,rsd)
                    if ctt==3:
                        EntryBox10.delete("0.0",END)
                        EntryBox10.insert(INSERT,rsd)
                    if ctt==4:
                        EntryBox11.delete("0.0",END)
                        EntryBox11.insert(INSERT,rsd)
                    if ctt==5:
                        EntryBox12.delete("0.0",END)
                        EntryBox12.insert(INSERT,rsd)
                    ctt=ctt+1


    if res[2]==1.0:
        print("Surprise")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT suprise FROM newplaylist")
        myresult = mycursor.fetchall()
        nplylist=[]
        cnt=1
        for x in myresult:            
            sd = str(x).replace('(','').replace(')','').replace(',','').replace("'", "")
            if sd=="":
                print("empty")
            else:
                if cnt==1:
                    EntryBox3.delete("0.0",END)
                    EntryBox8.delete("0.0",END)
                    EntryBox3.insert(INSERT,sd)

                if cnt==2:
                    EntryBox4.delete("0.0",END)
                    EntryBox9.delete("0.0",END)
                    EntryBox4.insert(INSERT,sd)

                if cnt==3:
                    EntryBox5.delete("0.0",END)
                    EntryBox10.delete("0.0",END)
                    EntryBox5.insert(INSERT,sd)

                cnt=cnt+1

            mycursor.execute("SELECT suprise FROM recentlyplayed")
            rmyresult = mycursor.fetchall()
            rcntplyst = []
            for i in rmyresult:
                if i not in rcntplyst:
                    rcntplyst.append(i)
            ctt=1
            for rx in rcntplyst:            
                rsd = str(rx).replace('(','').replace(')','').replace(',','').replace("'", "")
                if rsd=="":
                    print("empty")
                else:
                    print(rsd)
                    if ctt==1:
                        EntryBox8.delete("0.0",END)
                        EntryBox8.insert(INSERT,rsd)
                    if ctt==2:
                        EntryBox9.delete("0.0",END)
                        EntryBox9.insert(INSERT,rsd)
                    if ctt==3:
                        EntryBox10.delete("0.0",END)
                        EntryBox10.insert(INSERT,rsd)
                    ctt=ctt+1
    if res[3]==1.0:
        print("Sad")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT sad FROM newplaylist")
        myresult = mycursor.fetchall()
        nplylist=[]
        cnt=1
        for x in myresult:            
            sd = str(x).replace('(','').replace(')','').replace(',','').replace("'", "")
            if sd=="":
                print("empty")
            else:
                if cnt==1:
                    EntryBox3.delete("0.0",END)
                    EntryBox8.delete("0.0",END)
                    EntryBox3.insert(INSERT,sd)

                if cnt==2:
                    EntryBox4.delete("0.0",END)
                    EntryBox9.delete("0.0",END)
                    EntryBox4.insert(INSERT,sd)

                if cnt==3:
                    EntryBox5.delete("0.0",END)
                    EntryBox10.delete("0.0",END)
                    EntryBox5.insert(INSERT,sd)

                cnt=cnt+1
            mycursor.execute("SELECT sad FROM recentlyplayed")
            rmyresult = mycursor.fetchall()
            rcntplyst = []
            for i in rmyresult:
                if i not in rcntplyst:
                    rcntplyst.append(i)
            ctt=1
            for rx in rcntplyst:            
                rsd = str(rx).replace('(','').replace(')','').replace(',','').replace("'", "")
                if rsd=="":
                    print("empty")
                else:
                    print(rsd)
                    if ctt==1:
                        EntryBox8.delete("0.0",END)
                        EntryBox8.insert(INSERT,rsd)
                    if ctt==2:
                        EntryBox9.delete("0.0",END)
                        EntryBox9.insert(INSERT,rsd)
                    if ctt==3:
                        EntryBox10.delete("0.0",END)
                        EntryBox10.insert(INSERT,rsd)
                    ctt=ctt+1


    if res[4]==1.0:
        print("Fear")
        mycursor = mysqldb.cursor()
        mycursor.execute("SELECT fear FROM newplaylist")
        myresult = mycursor.fetchall()
        nplylist=[]
        cnt=1
        for x in myresult:            
            sd = str(x).replace('(','').replace(')','').replace(',','').replace("'", "")
            if sd=="":
                print("empty")
            else:
                if cnt==1:
                    EntryBox3.delete("0.0",END)
                    EntryBox8.delete("0.0",END)
                    EntryBox3.insert(INSERT,sd)

                if cnt==2:
                    EntryBox4.delete("0.0",END)
                    EntryBox9.delete("0.0",END)
                    EntryBox4.insert(INSERT,sd)
     
                if cnt==3:
                    EntryBox5.delete("0.0",END)
                    EntryBox10.delete("0.0",END)
                    EntryBox5.insert(INSERT,sd)

                cnt=cnt+1
            mycursor.execute("SELECT fear FROM recentlyplayed")
            rmyresult = mycursor.fetchall()
            rcntplyst = []
            for i in rmyresult:
                if i not in rcntplyst:
                    rcntplyst.append(i)
            ctt=1
            for rx in rcntplyst:            
                rsd = str(rx).replace('(','').replace(')','').replace(',','').replace("'", "")
                if rsd=="":
                    print("empty")
                else:
                    print(rsd)
                    if ctt==1:
                        EntryBox8.delete("0.0",END)
                        EntryBox8.insert(INSERT,rsd)
                    if ctt==2:
                        EntryBox9.delete("0.0",END)
                        EntryBox9.insert(INSERT,rsd)
                    if ctt==3:
                        EntryBox10.delete("0.0",END)
                        EntryBox10.insert(INSERT,rsd)
                    ctt=ctt+1
    EntryBox1.delete("0.0",END)
    if msg != '':
        ChatLog.config(state=NORMAL)
        ChatLog.insert(END, "You: " + msg + '\n\n')
        ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
    
        ress = chatbot_response(msg)
        ChatLog.insert(END, "Bot: " + ress + '\n\n')
            
        ChatLog.config(state=DISABLED)
        ChatLog.yview(END)
        
def add_song():
    gr=comboa1.get()
    inp = EntryBox2.get(1.0, "end-1c")
    print(type(inp))

    if(gr=="angry"):
        mycursor = mysqldb.cursor()
        sql= "INSERT INTO newplaylist (angry) VALUES (%s)"
        val = [(inp)]
        mycursor.execute(sql,val)
        mysqldb.commit()
    if(gr=="happy"):
        mycursor = mysqldb.cursor()
        sql= "INSERT INTO newplaylist (happy) VALUES (%s)"
        val = [(inp)]
        mycursor.execute(sql,val)
        mysqldb.commit()
    if(gr=="sad"):
        mycursor = mysqldb.cursor()
        sql= "INSERT INTO newplaylist (sad) VALUES (%s)"
        val = [(inp)]
        mycursor.execute(sql,val)
        mysqldb.commit()
    if(gr=="suprise"):
        mycursor = mysqldb.cursor()
        sql= "INSERT INTO newplaylist (suprise) VALUES (%s)"
        val = [(inp)]
        mycursor.execute(sql,val)
        mysqldb.commit()
    if(gr=="fear"):
        mycursor = mysqldb.cursor()
        sql= "INSERT INTO newplaylist (fear) VALUES (%s)"
        val = [(inp)]
        mycursor.execute(sql,val)
        mysqldb.commit()
def exit_main():
    master.destroy()

    


master = Tk()
master.title('CHATBOT SONG RECOMMENDATION SYSTEM')
master.geometry('1920x1080')

Label(master,text='CHATBOT SONG RECOMMENDATION SYSTEM',foreground="red",font=('Verdana',25)).pack(side=TOP,pady=10)

l1=Label(master,text='RECENTLY PLAYED',foreground="red",font=('Verdana',13,'bold'))
l1.place(x=30,y=100)


StopButton = Button(master, font=("Verdana",12,'bold'), text="Stop Song", width="12", height=5,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command= play_stop)
StopButton.place(height=100,width=150,x=30,y=640)

ExitButton = Button(master, font=("Verdana",12,'bold'), text="Exit", width="12", height=5,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command= exit_main)
ExitButton.place(height=100,width=150,x=285,y=640)


l2=Label(master,text='CHAT BOT',foreground="red",font=('Verdana',13,'bold'))
l2.place(x=555,y=100)



ChatLog = Text(master, bd=0, bg="white", height="20", width="40", font="Arial",)
ChatLog.place(x=555,y=150)

scrollbar = Scrollbar(master, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = scrollbar.set
scrollbar.place(x=980,y=150, height=465)

EntryBox1 = Text(master, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox1.place(height=100,width=270,x=555,y=640)

SendButton = Button(master, font=("Verdana",12,'bold'), text="Send", width="12", height=5,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command= send)
SendButton.place(height=100,width=150,x=830,y=640)

l3=Label(master,text='TRENDING SONG',foreground="red",font=('Verdana',13,'bold'))
l3.place(x=1080,y=100)



#######add song########

##EntryBox2 = Text(master, bd=0, bg="white",width="29", height="5", font="Arial")
##EntryBox2.place(height=50,width=250,x=1080,y=690)
##
##n1=StringVar()
##comboa1=ttk.Combobox(master,font =('Verdana',12,'bold'),foreground='red',state='readonly',textvariable=n1)
##comboa1['values']=('happy','sad','fear','angry','suprise')
##comboa1.current(0)
##comboa1.place(height=40,width=250,x=1080,y=640)
##
##AddButton = Button(master, font=("Verdana",12,'bold'), text="Add Song", width="12", height=5,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command= add_song)
##AddButton.place(height=100,width=150,x=1340,y=640)




EntryBox3 = Text(master, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox3.place(height=50,width=270,x=1080,y=150)

playbutton3 = Button(master, font=("Verdana",12,'bold'), text="PLAY", width="12", height=5,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command= play_button1)
playbutton3.place(height=50,width=100,x=1380,y=150)

EntryBox4 = Text(master, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox4.place(height=50,width=270,x=1080,y=250)

playbutton4 = Button(master, font=("Verdana",12,'bold'), text="PLAY", width="12", height=5,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command= play_button2)
playbutton4.place(height=50,width=100,x=1380,y=250)

EntryBox5 = Text(master, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox5.place(height=50,width=270,x=1080,y=350)

playbutton5 = Button(master, font=("Verdana",12,'bold'), text="PLAY", width="12", height=5,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command= play_button3)
playbutton5.place(height=50,width=100,x=1380,y=350)


EntryBox6 = Text(master, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox6.place(height=50,width=270,x=1080,y=450)

playbutton6 = Button(master, font=("Verdana",12,'bold'), text="PLAY", width="12", height=5,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command= play_button4)
playbutton6.place(height=50,width=100,x=1380,y=450)

EntryBox7 = Text(master, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox7.place(height=50,width=270,x=1080,y=550)

playbutton7 = Button(master, font=("Verdana",12,'bold'), text="PLAY", width="12", height=5,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command= play_button5)
playbutton7.place(height=50,width=100,x=1380,y=550)



EntryBox8 = Text(master, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox8.place(height=50,width=270,x=30,y=150)

playbutton8 = Button(master, font=("Verdana",12,'bold'), text="PLAY", width="12", height=5,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command= rplay_button1)
playbutton8.place(height=50,width=100,x=330,y=150)

EntryBox9 = Text(master, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox9.place(height=50,width=270,x=30,y=250)

playbutton9 = Button(master, font=("Verdana",12,'bold'), text="PLAY", width="12", height=5,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command= rplay_button2)
playbutton9.place(height=50,width=100,x=330,y=250)

EntryBox10 = Text(master, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox10.place(height=50,width=270,x=30,y=350)

playbutton10 = Button(master, font=("Verdana",12,'bold'), text="PLAY", width="12", height=5,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command= rplay_button3)
playbutton10.place(height=50,width=100,x=330,y=350)

EntryBox11 = Text(master, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox11.place(height=50,width=270,x=30,y=450)

playbutton11 = Button(master, font=("Verdana",12,'bold'), text="PLAY", width="12", height=5,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command= rplay_button4)
playbutton11.place(height=50,width=100,x=330,y=450)

EntryBox12 = Text(master, bd=0, bg="white",width="29", height="5", font="Arial")
EntryBox12.place(height=50,width=270,x=30,y=550)

playbutton12 = Button(master, font=("Verdana",12,'bold'), text="PLAY", width="12", height=5,bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff',command= rplay_button5)
playbutton12.place(height=50,width=100,x=330,y=550)


mainloop()
 
