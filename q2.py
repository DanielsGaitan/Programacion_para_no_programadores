#Daniel Santiago Gaitán
import sys
def test(didPass):
  linenum = sys._getframe(1).f_lineno
  if didPass:
    msn = "Test en línea {0} pasó".format(linenum)
  else:
    msn = "Test en línea {0} falló".format(linenum)
  print(msn)

def prod_div(n, x):
  multiplicacion = 1
  for i in range(1, n+1):
    if i * x <= n:
      multiplicacion *= i*x

  return multiplicacion

def testsuite():
  test(prod_div(19, 5) == 750)
  test(prod_div(10, 2) == 3840)
  test(prod_div(96, 27) == 118098)
  test(prod_div(12, 3) == 1944)
testsuite()
