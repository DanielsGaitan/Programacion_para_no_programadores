import sys
def conv_divi(l, d):
  valor = 0
  for i in l:
    if d == 'dolar':
      valor = i / 3760.00
    elif d == 'euro':
      valor = i / 4453.10
    elif d == 'yen':
      valor = i / 34.19
    elif d == 'libra':
      valor = i / 5183.63
    else:
      valor = "No es una moneda válida"
    #print(f"{i} COP = {valor} {d}")
conv_divi( [10000, 150000, 202000, 50000, 750000], "yen")
def par (m):
  if m % 2 == 0:
    return True
  else:
    return False





def test(didPass):
  linenum = sys._getframe(1).f_lineno
  if didPass:
    msn = "test en línea {0} ok".format(linenum)
  else:
    msn = "test en línea {0} Fallo".format(linenum)
  print(msn)

def diasem(dia):
  if dia == "domingo":
    return 0
  elif dia == "lunes":
    return 1
  elif dia == "martes":
    return 2
  elif dia == "miercoles":
    return 3
  elif dia == "jueves":
    return 4
  elif dia == "viernes":
    return 5
  elif dia == "sabado":
    return 6
  else:
    return None
def primo(num):
  for i in range(2,num):
    if num % i == 0:
      return False
  return True
def farenheit(c):
  return round((1.8 * c) + 32)
def banco_pruebas():
  test(farenheit(0) == 32)
  test(farenheit(100) == 212)
  test(farenheit(-40) == -40)
  test(farenheit(12) == 54)
  test(farenheit(18) == 64)
  test(farenheit(-48) == -54)
banco_pruebas()
