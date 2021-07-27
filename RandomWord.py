import json
import random
import pymongo
import sys

from random_word import RandomWords
import time
import nltk

start_time = time.time()
totalWord = 12
password = ""
characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "~"]
randChar = characters[random.randrange(0, len(characters)-1)]

rand1Len = str(random.randrange(3, 5))
totalWord = totalWord - int(rand1Len)

# nltk.download('averaged_perceptron_tagger')

with open(rand1Len +'LetterVerb.json') as f:
    data = json.load(f)

rand1 = str(random.randrange(0, len(data)-1))

password = password + randChar + data.get(rand1).capitalize()
if(rand1Len == "3"):
    rand2Len = str(random.randrange(4, 5))
else:
    rand2Len = str(random.randrange(3, 5))

totalWord = totalWord - int(rand2Len)

with open(rand2Len +'LetterAdj.json') as f:
    data1 = json.load(f)

rand2 = str(random.randrange(0, len(data1)-1))


password = password + data1.get(rand2).capitalize()



if(totalWord<=3):
    rand3len = 3

else:
    rand3len = str(totalWord)

with open(rand3len +'LetterNoun.json') as f:
    data2 = json.load(f)

rand3 = str(random.randrange(0, len(data2)-1))

password = password + data2.get(rand3).capitalize()


randInt1 = str(random.randrange(0, 9))
randInt2 = str(random.randrange(0, 9))
randInt3 = str(random.randrange(0, 9))
randInt4 = str(random.randrange(0, 9))

password = password + randInt1 + randInt2 + randInt3

if(len(password)<3):
    password = password + randInt4
print(password)
print("time elapsed: {:.2f}s".format(time.time() - start_time))


myclient = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
mydb = myclient["Project"]
mycol = mydb["Passwords"]

URL = sys.argv[1]
PasswordInfo = sys.argv[2]

mydict = {
    "URL": URL,
    "Password": password,
    "Password Info": PasswordInfo
}

x = mycol.insert_one(mydict)