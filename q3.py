import sys

def test (did_pass):
    linenum = sys._getframe(1).f_lineno #se obtiene el numero de línea del programa
    if did_pass:
        msn = "test en linea {0} ok".format(linenum)
    else:
        msn = "test en linea {0} Fallo".format(linenum)
    print(msn)
    
def only_num (cadena):
    textonuevo = ""
    for i in cadena:
        if i in "1234567890":
            textonuevo += i
    return textonuevo

def banco_pruebas ():
    test ( only_num ("Yo tengo 35 perritos ") == "35")
    test(only_num("El 3 de Marzo vienen 13 pax ") == "313")
    test(only_num("2x3 =6 y 5 -8= -3") == "236583" )
    test(only_num('a1s2d3f4g5h2j14k647') == "12345214647")


banco_pruebas()
    
    