import random
from tkinter import *
class Counter:
    def __init__(self):
        self.count = 0
    def inc(self):
        self.count = self.count+1
class Word:
    def __init__(self):
        self.colors = ['red','blue','white','black','yellow','gray' ,'orange' , 'green' ,'pink' , 'purple','bronze','brown','cyan','violet','lilac','ruby','silver','indigo']
        self.animals = ['rabbit' , 'lion' , 'turtle' , 'mouse' , 'cat' , 'dog' , 'tiger' , 'bird' , 'horse' , 'bat','goose','jellyfish','octopus','kangaroo','parrot','pig','wolf','fox']
        self.countries = ['egypt' , 'canada' , 'germany' , 'argentina' , 'qatar' , 'france' , 'england'  ,'greece' ,'brazil' , 'italy','norway','poland','russia','belgium','india','mexico','finland','oman','ireland','malta','thailand','tunisia']
        self.cities = ['cairo','berlin','london','barcelona','rome','milan','paris','athens','toronto','amsterdam','oslo','copenhagen','kiev','montreal','prague','tokyo','chicago','sydney','dublin','dubai','vienna','belgrade','bucharest','budapest','brasilia']

    def getWord(self,i , j):
        if(i ==1):
            return self.colors[j]
        elif i ==2:
            return self.animals[j]
        elif i ==3:
            return self.cities[j]
        else:
            return self.countries[j]

class Score:
    def __init__(self):
        self.score = 0
    def inc(self,x):
        self.score = self.score +x

class Keyboard:
    def __init__(self):
        self.list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']
        self.activeList = []
        i = 0
        while i<27:
            i+=1
            self.activeList.append('a')
def displayWord(word , list):
    i = 0
    out = ''
    while i< len(word):
        if(list[i] == 'n'):
            out = out + '_'
        else:
            out  = out+str(word[i])
        i+=1
    print(out)




k = Keyboard()
c = Counter()
w = Word()
s = Score()

while c.count < 6:
    k.activeList = []
    i = 0
    while i < 27:
        i += 1
        k.activeList.append('a')

    i = random.randint(1, 4)
    j = random.randint(0, 9)
    word = w.getWord(i, j)
    wordList = []
    co = 0
    while co < len(word):
        wordList.append('n')
        co+=1
    leng = len(word)
    print()
    if (i == 1):
        print('It is a color')
    elif i == 2:
        print('It is an animal')
    elif i == 3:
        print('It is a city')
    else:
        print('It is a country')
    while c.count < 6 and not leng == 0:
        displayWord(word, wordList)
        inp = input('enter a letter')
        x = 0
        while (x < len(k.list)):

            if (k.list[x] == inp):
                break
            x = x + 1
        if not k.activeList[x] == 'a':
            print('you have used this letter before')
        else:
            numOfOcc = word.count(inp)
            leng = leng - numOfOcc
            k.activeList[x] = 'n'
            if(numOfOcc == 0):
                c.inc()
            else:
                mente = 0
                while mente < len(word):
                    if(word[mente] == inp):
                        wordList[mente] = 'a'
                    mente+=1
        print()            
        print('you have ' + str(6-c.count) + ' chances left')
        print()

    print()    
    if(leng == 0):
        print(word)
    if(c.count<6):
        s.inc(len(word))
print()
print('the word is ' + str(word))
print('game over')

print('your score is ' + str(s.score))
root = Tk()
lab = Label(root ,text='Game over')
lab.pack()
root.mainloop()
root.maxsize
























