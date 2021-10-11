#función que reciba 2 enteros y verifique si el 1ero es divisible en el segundo
def divisible(a, b):
    if a % b == 0:
        return True
    else:
        return False
def primo(c):
    if c != 2:
        for i in range(2, c):
            if c % i == 0:
                return "False"
            else:
                return "True"
    else:
        return "True"
def nota(note):
    if note >= 75:
        return "Excelente"
    elif note >= 70 and note < 75:
        return "Bueno"
    elif note >= 60 and note < 70:
        return "Ok"
    elif note >= 50 and note < 60:
        return "Regular"
    elif note >= 45 and note < 50:
        return "Mal"
    elif note >= 40 and note < 45:
        return "Pésimo"
    elif note < 40:
        return "Perverso"
    else:
        return "No es una nota válida"
evaluaciones = [83, 75, 74.9, 70, 69.9, 65]
resul = []
for i in evaluaciones:
     resul.append(nota(i))
print (resul)