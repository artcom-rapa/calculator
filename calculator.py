import logging
logging.basicConfig(level=logging.DEBUG)

def calculator(a, b):
    if operation == "1":
        addition = a + b
        logging.info("Dodaję %s i %s" % (a, b))
        print("Wynik to: %s" % addition)
    elif operation == "2":
        subtraction = a - b
        logging.info("Odejmuję %s i %s" % (a, b))
        print("Wynik to: %s" % subtraction)
    elif operation == "3":
        multiplication = a * b
        logging.info("Mnożę %s i %s" % (a, b))
        print("Wynik to: %s" % multiplication)
    elif operation == "4":
        devision = a / b
        logging.info("Dzielę %s i %s" % (a, b))
        print("Wynik to: %s" % devision)
    else:
        exit(1)

if __name__ == "__main__":
    operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    a = float(input("Podaj składnik 1: "))
    b = float(input("Podaj składnik 2: "))
    calculator(a, b)