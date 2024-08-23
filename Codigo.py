intentos = int(input("¿Cuántos vehículos quieres identificar? :"))

for x in range(intentos):
    ruedas = int(input("¿Cuántas ruedas tiene? :"))
    motor = input("¿El vehículo tiene motor? si/no :")

    if ruedas == 4 and motor == "si":
        print("Tienes un coche")
    elif ruedas == 4 and motor == "no":
        print("Tienes una carreta")
    elif ruedas == 2 and motor == "si":
        print("Tienes una motocicleta")
    elif ruedas == 2 and motor == "no":
        print("Tienes una bicicleta")
    else:
        print("Respuesta Incorrecta")



            