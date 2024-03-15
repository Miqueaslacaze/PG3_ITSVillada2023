
def años_bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
       print("El año es bisisesto")
    else:
        print("El año no es bisiesto")


año = int(input("que año deseas inspeccionar")) 

años_bisiesto(año)
  