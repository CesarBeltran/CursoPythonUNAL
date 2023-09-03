'''
- Los años divisibles entre 4  son bisiestos.    * NO todos.....
(año%4)==0

- Los años que son divisibles entre 4 , pero no entre 100, son bisiestos.   *
(año%4)==0 and (año%100)!=0

- Los años divisibles entre 100  y entre 400  son bisiestos         *
(año%100)==0 and (año%400)==0


- Los años divisibles entre 100, pero que no son divisibles entre 400  no son bisiestos.
(año%100)==0 and (año%400)!=0   NO SON BISIESTOS

'''
año=1900


# Evaluación de condiciones y salida del programa por escenario (~ 7-11 líneas).

if (año%4)==0 and (año%100)!=0:
       print("Es un año bisiesto")
else:
    if ((año%100)==0 and (año%400)==0):
        print("Es un año bisiesto")
    else:
        print("No es un año bisiesto")


    