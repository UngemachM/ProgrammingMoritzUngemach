seitenlänge = 33
def BaumMalen(seitenlänge):
    zeichen = "*"
    for i in range(seitenlänge):
        for j in range(seitenlänge):
            if i == 0 or i == seitenlänge - 1 or j == 0 or j == seitenlänge - 1:
                print(zeichen, end=" ")
            else:
                if(ist_ungerade(seitenlänge)):
                    ÄsteZeichnenUngerade(i,j,seitenlänge)
        print()  # Neue Zeile nach jeder Reihe
    

def ist_ungerade(zahl):
    return zahl % 2 == 1

def muster_generator(o):
    if(o==1):
        return 0
    elif(o==2):
        return 1
    elif(o==3):
        return 0
    elif(o==4):
        return 1
    elif(o==5):
        return 2
    elif(o==6):
        return 1    
    elif(o==7):
        return 2
    elif(o==8):
        return 3
    elif(o==9):
        return 2
    elif(o==10):
        return 3
    elif(o==11):
        return 4
    elif(o==12):
        return 3
    elif(o==13):
        return 4
    elif(o==14):
        return 5
    elif(o==15):
        return 4
    elif(o==16):
        return 5
    elif(o==17):
        return 6
    elif(o==18):
        return 5
    elif(o==19):
        return 6
    elif(o==20):
        return 7
    elif(o==21):
        return 6
    elif(o==22):
        return 7
    elif(o==23):
        return 8
    elif(o==24):
        return 7
    elif(o==25):
        return 8
    elif(o==26):
        return 9
    elif(o==27):
        return 8
    elif(o==28):
        return 9
    elif(o==29):
        return 10
    elif(o==30):
        return 9
    elif(o==31):
        return 10
    elif(o==32):
        return 11
    elif(o==33):
        return 1




def ÄsteZeichnenUngerade(i,j,seitenlänge):
    i=i-1
    if(i<1):
        print (" ", end=' ')
        return
    s = seitenlänge/2-0.5
    if(j<s-muster_generator(i) or j>s+muster_generator(i)):
        print (" ", end=' ')
    else:
        print("^" ,end=' ' )
       



BaumMalen(seitenlänge)