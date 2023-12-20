seitenlänge = 21

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

def muster_generator(anzahl):
    result = []
    current = 0

    for i in range(anzahl):
        result.append(current)
        current += 1

        if i % 2 == 1:
            current = result[i // 2] + 1

    return result[-1] if result else None

    # Beispielaufruf mit einer Anzahl von 17
    anzahl = 3
    letzte_zahl = letzte_zahl_im_muster(anzahl)
    return letzte_zahl

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