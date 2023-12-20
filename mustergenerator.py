def letzte_zahl_im_muster(anzahl):
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

