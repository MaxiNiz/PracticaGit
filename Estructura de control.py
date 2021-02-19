variable_1 = 20
variable_2 = 20

def indeterminados ():
    global variable_1
    variable_1 = 0
    variable_2 = 10
    print (variable_1,variable_2)
indeterminados()
print ("Mira como te cambio los valores wachin", variable_1, "y la variable 2", variable_2)