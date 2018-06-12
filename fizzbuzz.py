# bucle del 1 al 100
for x in range(1, 101): # iniciamos un for  donde  "x" este dentro del rango del 1 al 101
    a = ((x%3)==0) # la variable "a" va a buscar multiplo de 3 en el rango del 1 al 101
    b = ((x%5)==0) # la variable "b" va a buscar multiplo de 5 en el rango del 1 al 101
    if a or b: print "Fizz" * a + "Buzz" * b # si el valor de la variable "a"  es multiplo de 3 se imprime la palabra fizz
    #si la variable"b"es multiplo de 5 imprime buzz 
    else: print x# imprime en la pantalla el valor de la variable "x"

