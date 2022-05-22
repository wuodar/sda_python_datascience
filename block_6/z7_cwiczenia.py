while True:
    try:
        value = input("Podaj liczbe: ")
        value = float(value)
        print(value/3)
        break

    except:
        print("Podana wartość jest niepoprawna. Proszę, podaj liczbę rzeczywistą.")
        print("Blok except")


    finally:
        print("Blok finally")