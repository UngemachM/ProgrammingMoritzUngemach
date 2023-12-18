
# Größe des Quadrats
seitenlänge = 12

# Zeichen, das verwendet werden soll
zeichen = '*'

# Zeichne die Ränder des Quadrats
for i in range(seitenlänge):
    for j in range(seitenlänge):
        if i == 0 or i == seitenlänge - 1 or j == 0 or j == seitenlänge - 1:
            print(zeichen, end=' ')
        else:
            if i==1:
                print (" ", end=' ')
            if i==2:
                if j<5 or j>5:
                    print(' ', end=' ')
                else:
                    print("^" ,end=' ' )
            if i==3:
                if j<4 or j>6:
                    print(' ', end=' ')
                else:
                    print("^" ,end=' ' )
            if i==4:
                if j<5 or j>5:
                    print(' ', end=' ')
                else:
                    print("^" ,end=' ' )
            if i==5:
                if j<4 or j>6:
                    print(' ', end=' ')
                else:
                    print("^" ,end=' ' )
            if i==6:
                if j<3 or j>7:
                    print(' ', end=' ')
                else:
                    print("^" ,end=' ' )
            if i==7:
                if j<4 or j>6:
                    print(' ', end=' ')
                else:
                    print("^" ,end=' ' )
            if i==8:
                if j<3 or j>7:
                    print(' ', end=' ')
                else:
                    print("^" ,end=' ' )
            if i==9:
                if j<2 or j>8:
                    print(' ', end=' ')
                else:
                    print("^" ,end=' ' )
            if i==10:
                if j<4 or j>6:
                    print(' ', end=' ')
                else:
                    print("^" ,end=' ' )
    print()  # Neue Zeile nach jeder Reihe
