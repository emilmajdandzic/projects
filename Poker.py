from turtle import*
from random import*
from copy import*
from time import*

# Nimmt X-und Y-Koordinate von angeklickter Karte und markiert diese
def writ(x,y):
    global z1, c1
    z1.append(x)
    c1.append(y)
    cross=Turtle()
    cross.ht()
    cross.pu()
    cross.speed(0)
    cross.shape("circle")
    cross.color("orange")
    cross.turtlesize(1.5)
    cross.goto(x,y)
    cross.st()

# Runde eine Zahl
def match(o):
    o=round(o)
    return(o)


c1=list()
z1=list()

# Blendet alle Karten zum Auswählen ein
setup(1280,1024)
bgcolor("green")
global pn
pn="P:/Downloads/"
for i in range(1,53):
    register_shape(pn+str(i)+".gif")
    a=Turtle()
    a.ht()
    a.speed(0)
    b=Turtle()
    b.ht()
    b.speed(0)
    a.pu()
    a.shape(pn+str(i)+".gif")
    b.pu()
    b.onclick(writ)
    b.color("")
    b.shape("turtle")
    b.turtlesize(5)
    if i < 14:
        a.goto(-420+70*(i-1),300)
        b.goto(-420+70*(i-1),300)
    elif i < 27:
        a.goto(-420+70*(i-14),100)
        b.goto(-420+70*(i-14),100)
    elif i < 40:
        a.goto(-420+70*(i-27),-100)
        b.goto(-420+70*(i-27),-100)
    else:
        a.goto(-420+70*(i-40),-300)
        b.goto(-420+70*(i-40),-300)
    a.st()
    b.st()
    
lal=Turtle()
lal.pu()
lal.ht()
lal.speed(0)
lal.goto(0,450)
lal.pd()
lal.pencolor("white")

# Schrift Spieler 1
while len(z1)<2:
    if len(z1)<1:
        lal.write("Wähle die Karten von Spieler 1: Karte Nr. 1", align="center", font=("Arial",20,"italic"))
        lol=0
    else:
        if lol==0:
            lal.clear()
            lol=1
        lal.write("Wähle die Karten von Spieler 1: Karte Nr. 2", align="center", font=("Arial",20,"italic"))

# Unrechnung der X-/Y-Koordinate zu rechenbarer Form (Herz 2 --> 1,1)
z11=match((z1[0]+490)/70)
z12=match((z1[1]+490)/70)
c11=match((c1[0]+300)/200+1)
c12=match((c1[1]+300)/200+1)


c1=list()
z1=list()

# Schrift Spieler 2
while len(z1)<2:
    if len(z1)<1:
        if lol==1:
            lal.clear()
        lal.write("Wähle die Karten von Spieler 2: Karte Nr. 1", align="center", font=("Arial",20,"italic"))
        lol=0
    else:
        if lol==0:
            lal.clear()
            lol=1
        lal.write("Wähle die Karten von Spieler 2: Karte Nr. 2", align="center", font=("Arial",20,"italic"))

# Unrechnung der X-/Y-Koordinate zu rechenbarer Form (Herz 2 --> 1,1)        
z21=match((z1[0]+490)/70)
z22=match((z1[1]+490)/70)
c21=match((c1[0]+300)/200+1)
c22=match((c1[1]+300)/200+1)


c1=list()
z1=list()

# Schrift Flop    
while len(z1)<3:
    if len(z1)<1:
        if lol==1:
            lal.clear()
        lal.write("Wähle die Karte für den Flop: Karte Nr. 1", align="center", font=("Arial",20,"italic"))
        lol=0
    elif len(z1)<2:
        if lol==0:
            lal.clear()
            lol=1
        lal.write("Wähle die Karten für den Flop: Karte Nr. 2", align="center", font=("Arial",20,"italic"))
    else:
        if lol==1:
            lal.clear()
            lol=2
        lal.write("Wähle die Karten für den Flop: Karte Nr. 3", align="center", font=("Arial",20,"italic"))

# Unrechnung der X-/Y-Koordinate zu rechenbarer Form (Herz 2 --> 1,1)
zflop1=match((z1[0]+490)/70)
zflop2=match((z1[1]+490)/70)
zflop3=match((z1[2]+490)/70)
cflop1=match((c1[0]+300)/200+1)
cflop2=match((c1[1]+300)/200+1)
cflop3=match((c1[2]+300)/200+1)


c1=list()
z1=list()

# Schrift Turn
while len(z1)<2:
    if len(z1)<1:
        if lol==2:
            lal.clear()
        lal.write("Wähle die Karte für den Turn.", align="center", font=("Arial",20,"italic"))
        lol=0
    else:
        if lol==0:
            lal.clear()
            lol=1
        lal.write("Wähle die Karte für den River.", align="center", font=("Arial",20,"italic"))

# Unrechnung der X-/Y-Koordinate zu rechenbarer Form (Herz 2 --> 1,1)
zturn=match((z1[0]+490)/70)
zriver=match((z1[1]+490)/70)
cturn=match((c1[0]+300)/200+1)
criver=match((c1[1]+300)/200+1)

clearscreen()
bye()

# Aufdeken der von den Spielern ausgewählten Karten
setup(1280,1024)
bgcolor("green")
r11=Turtle()
r11.ht()
r11.pu()
r11.goto(-300,200)
if c11==4:
    register_shape(pn+str(z11)+".gif")
    r11.shape(pn+str(z11)+".gif")
elif c11==3:
    register_shape(pn+str(z11+13)+".gif")
    r11.shape(pn+str(z11+13)+".gif")
elif c11==2:
    register_shape(pn+str(z11+26)+".gif")
    r11.shape(pn+str(z11+26)+".gif")
else:
    register_shape(pn+str(z11+39)+".gif")
    r11.shape(pn+str(z11+39)+".gif")
r11.st()

r12=Turtle()
r12.ht()
r12.pu()
r12.goto(-200,200)
if c12==4:
    register_shape(pn+str(z12)+".gif")
    r12.shape(pn+str(z12)+".gif")
elif c12==3:
    register_shape(pn+str(z12+13)+".gif")
    r12.shape(pn+str(z12+13)+".gif")
elif c12==2:
    register_shape(pn+str(z12+26)+".gif")
    r12.shape(pn+str(z12+26)+".gif")
else:
    register_shape(pn+str(z12+39)+".gif")
    r12.shape(pn+str(z12+39)+".gif")
r12.st()

r21=Turtle()
r21.ht()
r21.pu()
r21.goto(200,200)
if c21==4:
    register_shape(pn+str(z21)+".gif")
    r21.shape(pn+str(z21)+".gif")
elif c21==3:
    register_shape(pn+str(z21+13)+".gif")
    r21.shape(pn+str(z21+13)+".gif")
elif c21==2:
    register_shape(pn+str(z21+26)+".gif")
    r21.shape(pn+str(z21+26)+".gif")
else:
    register_shape(pn+str(z21+39)+".gif")
    r21.shape(pn+str(z21+39)+".gif")
r21.st()

r22=Turtle()
r22.ht()
r22.pu()
r22.goto(300,200)
if c22==4:
    register_shape(pn+str(z22)+".gif")
    r22.shape(pn+str(z22)+".gif")
elif c22==3:
    register_shape(pn+str(z22+13)+".gif")
    r22.shape(pn+str(z22+13)+".gif")
elif c22==2:
    register_shape(pn+str(z22+26)+".gif")
    r22.shape(pn+str(z22+26)+".gif")
else:
    register_shape(pn+str(z22+39)+".gif")
    r22.shape(pn+str(z22+39)+".gif")
r22.st()

# Definition der Reihe für den Straight
reihe=list()

for i in range(1,6):
        reihe.append(["0"+str(i),"0"+str(i+1),"0"+str(i+2),"0"+str(i+3),"0"+str(i+4)])
reihe.append(['06','07','08','09','10'])
reihe.append(['07','08','09','10','11'])
reihe.append(['08','09','10','11','12'])
reihe.append(['09','10','11','12','13'])
reihe.append(['01','02','03','04','13'])

# Umschreiben der Koordinaten in einfacher rechenbare Zahlen & zusammenfassen der Hand (Spieler 1 und Spieler 2)
c1=str(c11)
if z11<10:
    z1="0"+str(z11)
else:
    z1=str(z11)

c2=str(c12)
if z12<10:
    z2="0"+str(z12)
else:
    z2=str(z12)

h1=[[c1,z1],[c2,z2]]


c1=str(c21)
if z21<10:
    z1="0"+str(z21)
else:
    z1=str(z21)

c2=str(c22)
if z22<10:
    z2="0"+str(z22)
else:
    z2=str(z22)

h2=[[c1,z1],[c2,z2]]


# Umschreiben der Koordinaten in einfacher rechenbare Zahlen & zusammenfassen des Flops
c1=str(cflop1)
if zflop1<10:
    z1="0"+str(zflop1)
else:
    z1=str(zflop1)

c2=str(cflop2)
if zflop2<10:
    z2="0"+str(zflop2)
else:
    z2=str(zflop2)

c3=str(cflop3)
if zflop3<10:
    z3="0"+str(zflop3)
else:
    z3=str(zflop3)

Flop=[[c1,z1],[c2,z2],[c3,z3]]


# Umschreiben der Koordinaten in einfacher rechenbare Zahlen & zusammenfassen des Turns
c1=str(cturn)
if zturn<10:
    z1="0"+str(zturn)
else:
    z1=str(zturn)

Turn=[[c1,z1]]


# Umschreiben der Koordinaten in einfacher rechenbare Zahlen & zusammenfassen des River
c1=str(criver)
if zriver<10:
    z1="0"+str(zriver)
else:
    z1=str(zriver)

River=[[c1,z1]]



# Verfügbare Karten für Flop, Turn, River (also ohne Hand von Spieler 1 und 2)
a=[]

for i in range(1,5):
    for j in range(1,10):
        if [str(i),"0"+str(j)] not in (h1+h2):
            a.append([str(i),"0"+str(j)])
    for j in range(10,14):
        if [str(i),str(j)] not in (h1+h2):
            a.append([str(i),str(j)])


# Definitionen der verschiedenen Blätter
def kickerhighcard(cards):
    zahl=[cards[i][1] for i in range(5)]
    zahl.sort()
    return(int(zahl[4]+zahl[3]+zahl[2]+zahl[1]+zahl[0]))

def pair(cards):
    zahl=[cards[i][1] for i in range(5)]
    sz=set(zahl)
    if len(sz)==4:
        return(True)
    else:
        return(False)

def kickerpair(cards):
    zahl=[cards[i][1] for i in range(5)]
    zahl.sort()
    for i in range(len(zahl)):
        if zahl.count(zahl[i])==2:
            break
    pairzahl=zahl[i]
    zahl.remove(zahl[i])
    zahl.remove(zahl[i])
    return(int(pairzahl+zahl[2]+zahl[1]+zahl[0]))

def twopairs(cards):
    zahl=[cards[i][1] for i in range(5)]
    zahl.sort()
    sz=set(zahl)
    if len(sz)==3:
        if zahl.count(zahl[0])==2:
           if zahl.count(zahl[2])==2 or zahl.count(zahl[3])==2:
               return(True)
        elif zahl.count(zahl[1])==2 and zahl.count(zahl[3])==2:
            return(True)
        else:
            return(False)
    else:
        return(False)

def kickertwopairs(cards):
    zahl=[cards[i][1] for i in range(5)]
    zahl.sort()
    if zahl.count(zahl[0])==1:
        return(int(zahl[4]+zahl[1]+zahl[0]))
    elif zahl.count(zahl[2])==1:
        return(int(zahl[4]+zahl[0]+zahl[2]))
    else:
        return(int(zahl[2]+zahl[0]+zahl[4]))

def threeofakind(cards):
    zahl=[cards[i][1] for i in range(5)]
    zahl.sort()
    sz=set(zahl)
    if len(sz)==3 and (zahl.count(zahl[1])==3 or zahl.count(zahl[3])==3):
        return(True)
    else:
        return(False)

def kickerthreeofakind(cards):
    zahl=[cards[i][1] for i in range(5)]
    zahl.sort()
    if zahl.count(zahl[0])==3:
        return(int(zahl[0]+zahl[4]+zahl[3]))
    elif zahl.count(zahl[1])==3:
        return(int(zahl[1]+zahl[4]+zahl[0]))
    else:
        return(int(zahl[2]+zahl[1]+zahl[0]))

def straight(cards):
    zahl=[cards[i][1] for i in range(5)]
    zahl.sort()
    if zahl in reihe:
        return(True)
    else:
        return(False)

def kickerstraight(cards):
    zahl=[cards[i][1] for i in range(5)]
    zahl.sort()
    if zahl==['01','02','03','04','13']:
        return(int(zahl[3]))
    else:
        return(int(zahl[4]))

def flush(cards):
    color=[cards[i][0] for i in range(5)]
    if len(set(color))==1:
        return(True)
    else:
        return(False)

def kickerflush(cards):
    zahl=[cards[i][1] for i in range(5)]
    zahl.sort()
    return(int(zahl[4]))

def fullhouse(cards):
    zahl=[cards[i][1] for i in range(5)]
    zahl.sort()
    sz=set(zahl)
    if len(sz)==2 and (zahl.count(zahl[1])==3 or zahl.count(zahl[3])==3):
        return(True)
    else:
        return(False)

def kickerfullhouse(cards):
    zahl=[cards[i][1] for i in range(5)]
    zahl.sort()
    if zahl.count(zahl[1])==3:
        return(int(zahl[1]+zahl[3]))
    else:
        return(int(zahl[3]+zahl[1]))

def fourofakind(cards):
    zahl=[cards[i][1] for i in range(5)]
    zahl.sort()
    sz=set(zahl)
    if len(sz)==2 and (zahl.count(zahl[0])==4 or zahl.count(zahl[4])==4):
        return(True)
    else:
        return(False)

def kickerfourofakind(cards):
    zahl=[cards[i][1] for i in range(5)]
    zahl.sort()
    if zahl.count(zahl[0])==4:
        return(int(zahl[0]))
    else:
        return(int(zahl[4]))

def straightflush(cards):
    color=[cards[i][0] for i in range(5)]
    zahl=[cards[i][1] for i in range(5)]
    if len(set(color))==1:
        zahl.sort()
        if zahl in reihe:
            return(True)
        else:
            return(False)
    else:
        return(False)    

def kickerstraightflush(cards):
    zahl=[cards[i][1] for i in range(5)]
    zahl.sort()
    if zahl==['01','02','03','04','13']:
        return(int(zahl[3]))
    else:
        return(int(zahl[4]))

# Anzahl der Simulationen
total=1000

# Definition der Turtle
sp1text=Turtle()
sp1text.ht()
sp1text.speed(0)
sp1text.pu()
sp1text.goto(-400,-250)
sp1text.pd()
sp1text.pencolor("white")

sp11=Turtle()
sp11.ht()
sp11.speed(0)
sp11.pu()
sp11.goto(-400,-300)
sp11.pd()
sp11.pencolor("white")

sp12=Turtle()
sp12.ht()
sp12.speed(0)
sp12.pu()
sp12.goto(-400,-350)
sp12.pd()
sp12.pencolor("white")

sp13=Turtle()
sp13.ht()
sp13.speed(0)
sp13.pu()
sp13.goto(-400,-400)
sp13.pd()
sp13.pencolor("white")

sp2text=Turtle()
sp2text.ht()
sp2text.speed(0)
sp2text.pu()
sp2text.goto(400,-250)
sp2text.pd()
sp2text.pencolor("white")

sp21=Turtle()
sp21.ht()
sp21.speed(0)
sp21.pu()
sp21.goto(400,-300)
sp21.pd()
sp21.pencolor("white")

sp22=Turtle()
sp22.ht()
sp22.speed(0)
sp22.pu()
sp22.goto(400,-350)
sp22.pd()
sp22.pencolor("white")

sp23=Turtle()
sp23.ht()
sp23.speed(0)
sp23.pu()
sp23.goto(400,-400)
sp23.pd()
sp23.pencolor("white")

stext=Turtle()
stext.ht()
stext.speed(0)
stext.pu()
stext.goto(0,-250)
stext.pd()
stext.pencolor("white")

s1=Turtle()
s1.ht()
s1.speed(0)
s1.pu()
s1.goto(0,-300)
s1.pd()
s1.pencolor("white")

s2=Turtle()
s2.ht()
s2.speed(0)
s2.pu()
s2.goto(0,-350)
s2.pd()
s2.pencolor("white")

s3=Turtle()
s3.ht()
s3.speed(0)
s3.pu()
s3.goto(0,-400)
s3.pd()
s3.pencolor("white")

flop1=Turtle()
flop1.ht()
flop1.speed(0)
flop1.pu()
flop1.goto(-200,-100)
flop1.pd()
flop1.pencolor("white")

flop2=Turtle()
flop2.ht()
flop2.speed(0)
flop2.pu()
flop2.goto(-100,-100)
flop2.pd()
flop2.pencolor("white")

flop3=Turtle()
flop3.ht()
flop3.speed(0)
flop3.pu()
flop3.goto(0,-100)
flop3.pd()
flop3.pencolor("white")

flöp=[flop1,flop2,flop3]

türn=Turtle()
türn.ht()
türn.speed(0)
türn.pu()
türn.goto(100,-100)
türn.pd()
türn.pencolor("white")

rivér=Turtle()
rivér.ht()
rivér.speed(0)
rivér.pu()
rivér.goto(200,-100)
rivér.pd()
rivér.pencolor("white")


# Definition um weiterzugehen
def weiter(x,y):
        global goon
        goon=1337
        
bb=Turtle()
bb.ht()
bb.speed(0)
bb.pu()
bb.goto(0,400)
bb.fillcolor("")
bb.pd()
bb.pencolor("white")
bb.shape("square")
bb.turtlesize(200)
bb.onclick(weiter)

press=Turtle()
press.speed(0)
press.pu()
press.goto(0,100)
press.turtlesize(200)
press.fillcolor("")
press.shape("square")
press.pencolor("")
press.onclick(weiter)


# Simulation für: Pre-Flop, Flop, Turn und River
for t in range(3):
    p1=0
    p2=0

    #Flop aufdecken
    if t==1:
        print("Flop:",Flop)
        for i in range(3):
                c=int(Flop[i][0])
                z=int(Flop[i][1])
                if c==4:
                    register_shape(pn+str(z)+".gif")
                    flöp[i].st()
                    flöp[i].shape(pn+str(z)+".gif")
                elif c==3:
                    register_shape(pn+str(z+13)+".gif")
                    flöp[i].st()
                    flöp[i].shape(pn+str(z+13)+".gif")
                elif c==2:
                    register_shape(pn+str(z+26)+".gif")
                    flöp[i].st()
                    flöp[i].shape(pn+str(z+26)+".gif")
                else:
                    register_shape(pn+str(z+39)+".gif")
                    flöp[i].st()
                    flöp[i].shape(pn+str(z+39)+".gif")


        bb.clear()
        goon=0
        while goon==0:
                bb.write("Der Flop wurde aufgedeckt, drücke unten, um die Wahrscheinlichkeiten neu zu berechnen.", align="center", font=("Arial",20,"italic"))
               
        for i in range(3):
            a.remove(Flop[i])

    #Turn aufdecken        
    if t==2:
        print("Flop: ",Flop)
        print("Turn: ",Turn)
        
        c=int(Turn[0][0])
        z=int(Turn[0][1])
        if c==4:
            register_shape(pn+str(z)+".gif")
            türn.st()
            türn.shape(pn+str(z)+".gif")
        elif c==3:
            register_shape(pn+str(z+13)+".gif")
            türn.st()
            türn.shape(pn+str(z+13)+".gif")
        elif c==2:
            register_shape(pn+str(z+26)+".gif")
            türn.st()
            türn.shape(pn+str(z+26)+".gif")
        else:
            register_shape(pn+str(z+39)+".gif")
            türn.st()
            türn.shape(pn+str(z+39)+".gif")
    
        bb.clear()
        goon=0
        while goon==0:
                bb.write("Der Turn wurde aufgedeckt, drücke unten, um die Wahrscheinlichkeiten neu zu berechnen.", align="center", font=("Arial",20,"italic"))
                
        a.remove(Turn[0])
        
    print("Es wird gerade",total," Mal simuliert. Bitte warten...")
    bb.clear()
    bb.write("Es wird gerade "+str(total)+" Mal simuliert. Bitte warten...", align="center", font=("Arial",20,"italic"))

    # Generation von Zufallszahlen für Flop, Turn und River
    for u in range(total):
        shuffle(a)
        if t==0:
            flop=a[0:3]
        if t<2:
            turn=a[3:4]
        river=a[4:5]
        if t==1:
            flop=Flop
        if t==2:
            turn=Turn

        mx1=1
        mx2=1
        kicker1=0
        kicker2=0
        # Wegnehmen von zwei Karten, sodass es fünf sind, am Ende der Simulation kommen sie wieder dazu und es werden andere weggenommen
        for i in range(6):
            crr1=h1+flop+turn+river
            crr2=h2+flop+turn+river
            crr1.pop(i)
            crr2.pop(i)
            for j in range(1,6):
                cr1=deepcopy(crr1)
                cr2=deepcopy(crr2)
                cr1.pop(j)
                cr2.pop(j)
                # Prüfen des Blattes von Spieler 1
                if straightflush(cr1):
                    mx1=9
                    kicker1=max(kickerstraightflush(cr1),kicker1)
                    
                elif mx1<9 and fourofakind(cr1):
                    if mx1==8:
                        kicker1=max(kickerfourofakind(cr1),kicker1)
                    else:
                        kicker1=kickerfourofakind(cr1)
                    mx1=8
                    
                elif mx1<8 and fullhouse(cr1):
                    if mx1==7:
                        kicker1=max(kickerfullhouse(cr1),kicker1)
                    else:
                        kicker1=kickerfullhouse(cr1)
                    mx1=7
                    kicker1=max(kickerfullhouse(cr1),kicker1)
                    
                elif mx1<7 and flush(cr1):
                    if mx1==6:
                        kicker1=max(kickerflush(cr1),kicker1)
                    else:
                        kicker1=kickerflush(cr1)
                    mx1=6

                elif mx1<6 and straight(cr1):
                    if mx1==5:
                        kicker1=max(kickerstraight(cr1),kicker1)
                    else:
                        kicker1=kickerstraight(cr1)
                    mx1=5

                elif mx1<5 and threeofakind(cr1):
                    if mx1==4:
                        kicker1=max(kickerthreeofakind(cr1),kicker1)
                    else:
                        kicker1=kickerthreeofakind(cr1)
                    mx1=4

                elif mx1<4 and twopairs(cr1):
                    if mx1==3:
                        kicker1=max(kickertwopairs(cr1),kicker1)
                    else:
                        kicker1=kickertwopairs(cr1)
                    mx1=3

                elif mx1<3 and pair(cr1):
                    if mx1==2:
                        kicker1=max(kickerpair(cr1),kicker1)
                    else:
                        kicker1=kickerpair(cr1)
                    mx1=2

                elif mx1==1:
                    kicker1=max(kickerhighcard(cr1),kicker1)


                #Prüfen des Blattes von Spieler 2
                if straightflush(cr2):
                    mx2=9
                    kicker2=max(kickerstraightflush(cr2),kicker2)
                    
                elif mx2<9 and fourofakind(cr2):
                    if mx2==8:
                        kicker2=max(kickerfourofakind(cr2),kicker2)
                    else:
                        kicker2=kickerfourofakind(cr2)
                    mx2=8
                    
                elif mx2<8 and fullhouse(cr2):
                    if mx2==7:
                        kicker2=max(kickerfullhouse(cr2),kicker2)
                    else:
                        kicker2=kickerfullhouse(cr2)
                    mx2=7
                    kicker2=max(kickerfullhouse(cr2),kicker2)
                    
                elif mx2<7 and flush(cr2):
                    if mx2==6:
                        kicker2=max(kickerflush(cr2),kicker2)
                    else:
                        kicker2=kickerflush(cr2)
                    mx2=6

                elif mx2<6 and straight(cr2):
                    if mx2==5:
                        kicker2=max(kickerstraight(cr2),kicker2)
                    else:
                        kicker2=kickerstraight(cr2)
                    mx2=5

                elif mx2<5 and threeofakind(cr2):
                    if mx2==4:
                        kicker2=max(kickerthreeofakind(cr2),kicker2)
                    else:
                        kicker2=kickerthreeofakind(cr2)
                    mx2=4

                elif mx2<4 and twopairs(cr2):
                    if mx2==3:
                        kicker2=max(kickertwopairs(cr2),kicker2)
                    else:
                        kicker2=kickertwopairs(cr2)
                    mx2=3

                elif mx2<3 and pair(cr2):
                    if mx2==2:
                        kicker2=max(kickerpair(cr2),kicker2)
                    else:
                        kicker2=kickerpair(cr2)
                    mx2=2

                elif mx2==1:
                    kicker2=max(kickerhighcard(cr2),kicker2)
                    

        if mx1>mx2:
            p1=p1+1

        elif mx2>mx1:
            p2=p2+1

        else:
            if kicker1>kicker2:
                p1=p1+1

            if kicker2>kicker1:
                p2=p2+1


    print("Gewinnwahrscheinlichkeit Spieler 1:",p1/total)
    print("Gewinnwahrscheinlichkeit Spieler 2:",p2/total)
    print("Wahrscheinlichkeit Split Pot:",(total-p1-p2)/total)
    sp1text.write("Gewinnwahrsch. Spieler 1:", align="center", font=("Arial",20,"italic"))
    sp2text.write("Gewinnwahrsch. Spieler 2:", align="center", font=("Arial",20,"italic"))
    stext.write("Wahrsch. Split Pot:", align="center", font=("Arial",20,"italic"))

    if t==0:
        sp11.write(str(p1/total), align="center", font=("Arial",20,"italic"))
        sp21.write(str(p2/total), align="center", font=("Arial",20,"italic"))
        s1.write(str((total-p1-p2)/total), align="center", font=("Arial",20,"italic"))
        bb.clear()
        goon=0
        bb.clear()
        while goon==0:
            bb.write("Drücke unten um den Flop aufzudecken.", align="center", font=("Arial",20,"italic"))

    if t==1:
        sp12.write(str(p1/total), align="center", font=("Arial",20,"italic"))
        sp22.write(str(p2/total), align="center", font=("Arial",20,"italic"))
        s2.write(str((total-p1-p2)/total), align="center", font=("Arial",20,"italic"))
        bb.clear()
        goon=0
        bb.clear()
        while goon==0:
                bb.write("Drücke unten um den Turn aufzudecken.", align="center", font=("Arial",20,"italic"))

    if t==2:
        sp13.write(str(p1/total), align="center", font=("Arial",20,"italic"))
        sp23.write(str(p2/total), align="center", font=("Arial",20,"italic"))
        s3.write(str((total-p1-p2)/total), align="center", font=("Arial",20,"italic"))
        bb.clear()
        goon=0
        bb.clear()
        while goon==0:
                bb.write("Drücke unten um die letzte Karte aufzudecken.", align="center", font=("Arial",20,"italic"))
        print("Flop: ",Flop)
        print("Turn: ",Turn)
        print("River: ",River)


# River wird aufgedeckt
c=int(River[0][0])
z=int(River[0][1])

if c==4:
    register_shape(pn+str(z)+".gif")
    rivér.st()
    rivér.shape(pn+str(z)+".gif")
elif c==3:
    register_shape(pn+str(z+13)+".gif")
    rivér.st()
    rivér.shape(pn+str(z+13)+".gif")
elif c==2:
    register_shape(pn+str(z+26)+".gif")
    rivér.st()
    rivér.shape(pn+str(z+26)+".gif")
else:
    register_shape(pn+str(z+39)+".gif")
    rivér.st()
    rivér.shape(pn+str(z+39)+".gif")
    
mx1=1
mx2=1
kicker1=0
kicker2=0
# Macht eine letzte Simulation mit den vorliegenden Karten, um den Gewinner zu bestimmen
for i in range(6):
    crr1=h1+Flop+Turn+River
    crr2=h2+Flop+Turn+River
    crr1.pop(i)
    crr2.pop(i)
    for j in range(1,6):
        cr1=deepcopy(crr1)
        cr2=deepcopy(crr2)
        cr1.pop(j)
        cr2.pop(j)
        
        if straightflush(cr1):
            mx1=9
            kicker1=max(kickerstraightflush(cr1),kicker1)
            if cr1==[['1','09',],['1', '10'],['1', '11'],['1', '12'],['1', '13']] or cr1==[['2','09',],['2', '10'],['2', '11'],['2', '12'],['2', '13']] or cr1==[['3','09',],['3', '10'],['3', '11'],['3', '12'],['3', '13']] or cr1==[['4','09',],['4', '10'],['4', '11'],['4', '12'],['4', '13']]:
                reason1="Royal Flush"
            else:
                reason1="Straight Flush"
            
        elif mx1<9 and fourofakind(cr1):
            if mx1==8:
                kicker1=max(kickerfourofakind(cr1),kicker1)
            else:
                kicker1=kickerfourofakind(cr1)
            mx1=8
            reason1="Four Of A Kind"
            
        elif mx1<8 and fullhouse(cr1):
            if mx1==7:
                kicker1=max(kickerfullhouse(cr1),kicker1)
            else:
                kicker1=kickerfullhouse(cr1)
            mx1=7
            kicker1=max(kickerfullhouse(cr1),kicker1)
            reason1="Full House"
            
        elif mx1<7 and flush(cr1):
            if mx1==6:
                kicker1=max(kickerflush(cr1),kicker1)
            else:
                kicker1=kickerflush(cr1)
            mx1=6
            reason1="Flush"
            
        elif mx1<6 and straight(cr1):
            if mx1==5:
                kicker1=max(kickerstraight(cr1),kicker1)
            else:
                kicker1=kickerstraight(cr1)
            mx1=5
            reason1="Straight"
            
        elif mx1<5 and threeofakind(cr1):
            if mx1==4:
                kicker1=max(kickerthreeofakind(cr1),kicker1)
            else:
                kicker1=kickerthreeofakind(cr1)
            mx1=4
            reason1="Three Of A Kind"
            
        elif mx1<4 and twopairs(cr1):
            if mx1==3:
                kicker1=max(kickertwopairs(cr1),kicker1)
            else:
                kicker1=kickertwopairs(cr1)
            mx1=3
            reason1="Two Pairs"
            
        elif mx1<3 and pair(cr1):
            if mx1==2:
                kicker1=max(kickerpair(cr1),kicker1)
            else:
                kicker1=kickerpair(cr1)
            mx1=2
            reason1="Pair"
            
        elif mx1==1:
            kicker1=max(kickerhighcard(cr1),kicker1)
            reason1="High Card"
            

        if straightflush(cr2):
            mx2=9
            kicker2=max(kickerstraightflush(cr2),kicker2)
            if cr2==[['1','09',],['1', '10'],['1', '11'],['1', '12'],['1', '13']] or cr2==[['2','09',],['2', '10'],['2', '11'],['2', '12'],['2', '13']] or cr2==[['3','09',],['3', '10'],['3', '11'],['3', '12'],['3', '13']] or cr2==[['4','09',],['4', '10'],['4', '11'],['4', '12'],['4', '13']]:
                reason2="Royal Flush"
            else:
                reason2="Straight Flush"
            
        elif mx2<9 and fourofakind(cr2):
            if mx2==8:
                kicker2=max(kickerfourofakind(cr2),kicker2)
            else:
                kicker2=kickerfourofakind(cr2)
            mx2=8
            reason2="Four Of A Kind"
            
        elif mx2<8 and fullhouse(cr2):
            if mx2==7:
                kicker2=max(kickerfullhouse(cr2),kicker2)
            else:
                kicker2=kickerfullhouse(cr2)
            mx2=7
            kicker2=max(kickerfullhouse(cr2),kicker2)
            reason2="Full House"
            
        elif mx2<7 and flush(cr2):
            if mx2==6:
                kicker2=max(kickerflush(cr2),kicker2)
            else:
                kicker2=kickerflush(cr2)
            mx2=6
            reason2="Flush"
            
        elif mx2<6 and straight(cr2):
            if mx2==5:
                kicker2=max(kickerstraight(cr2),kicker2)
            else:
                kicker2=kickerstraight(cr2)
            mx2=5
            reason2="Straight"
            
        elif mx2<5 and threeofakind(cr2):
            if mx2==4:
                kicker2=max(kickerthreeofakind(cr2),kicker2)
            else:
                kicker2=kickerthreeofakind(cr2)
            mx2=4
            reason2="Three Of A Kind"
            
        elif mx2<4 and twopairs(cr2):
            if mx2==3:
                kicker2=max(kickertwopairs(cr2),kicker2)
            else:
                kicker2=kickertwopairs(cr2)
            mx2=3
            reason2="Two Pairs"
            
        elif mx2<3 and pair(cr2):
            if mx2==2:
                kicker2=max(kickerpair(cr2),kicker2)
            else:
                kicker2=kickerpair(cr2)
            mx2=2
            reason2="Pair"
            
        elif mx2==1:
            kicker2=max(kickerhighcard(cr2),kicker2)
            reason2="High Card"
        
bb.clear()

if mx1>mx2 or (mx1==mx2 and kicker1>kicker2):
    print("Spieler 1 hat gewonnen: "+reason1)
    bb.write("Spieler 1 hat gewonnen: "+reason1, align="center", font=("Arial",20,"italic"))

elif mx2>mx1 or (mx1==mx2 and kicker2>kicker1):
    print("Spieler 2 hat gewonnen: "+reason2)
    bb.write("Spieler 2 hat gewonnen: "+reason2, align="center", font=("Arial",20,"italic"))

else:
    print("Split Pot: Zwei Mal ", reason1)
    bb.write("Split Pot: Zwei Mal: "+reason1, align="center", font=("Arial",20,"italic"))

sleep(3)
bb.clear()
bb.write("Drücke unten um fortzufahren.", align="center", font=("Arial",20,"italic"))


fin=Turtle()
fin.ht()
fin.speed(0)
fin.pu()
fin.pd()
fin.pencolor("white")
fin.fillcolor("")


def end(x,y):
        clearscreen()
        bgcolor("green")
        fin.write("Danke fürs Spielen & auf Wiedersehen.", align="center", font=("Arial",20,"italic"))
        sleep(2)
        clearscreen()
        bye()

bb.onclick(end)
press.onclick(end)
