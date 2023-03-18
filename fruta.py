frutas = {'Plátano':1700.0, 'Manzana':3900.0, 'Pera':2200.0, 'Naranja':2500.0, 'Banano':4500.0, 'Fresa':8400.0, 'Uva':19900.0, 'Limon':8500.0}
fruta = input('¿Qué fruta quieres? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg, 'kilos de', fruta, 'valen', frutas[fruta]*kg, '$')
else: 
    print("Lo siento, la fruta", fruta, "no se encuentra disponible.")