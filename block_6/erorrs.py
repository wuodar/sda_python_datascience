import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

# przykład obsługi inputu od użytkownika, który podaje złe wartości (string zamiast liczby)
def handle_each_of_possible_errors_at_once():
    while True:
        try:
            value1 = input("Podaj liczbe numer 1: ")
            value1 = float(value1)
            value2 = input("Podaj liczbe numer 2: ")
            value2 = float(value2)
            print(value1/value2)
            break
        # blok except wykona się tylko w przypadku, gdy w bloku try wystąpi wyjątek/error
        except (ValueError, ZeroDivisionError): # jeżeli jesteśmy w stanie stwierdzić, jakie wyjątki mogą wystąpić w naszym kodzie, powinniśmy je sprecyzować, tak jak tutaj (ValueError, ZeroDivisionError)
            logger.error("\nPodana wartość jest niepoprawna. Proszę, podaj liczbę rzeczywistą.\n")
        # blok finally wykona się niezaleznie od wystąpienia błędu/wyjątku
        # finally:
        #     print("Blok finally")

def handle_specific_errors_separately():
    while True:
        try:
            value1 = input("Podaj liczbe numer 1: ")
            value1 = float(value1)
            value2 = input("Podaj liczbe numer 2: ")
            value2 = float(value2)
            print(value1/value2)
            break
        # blok except wykona się tylko w przypadku, gdy w bloku try wystąpi wyjątek/error
        except ValueError as e: # jeżeli jesteśmy w stanie stwierdzić, jakie wyjątki mogą wystąpić w naszym kodzie, powinniśmy je sprecyzować, tak jak tutaj ValueError
            logger.error(f"Wiadomosc o błędzie: {e.args[0]}")
            logger.warning("WARNING")
            logger.error("Podana wartość jest niepoprawna. Proszę, podaj liczbę rzeczywistą.")
        except ZeroDivisionError: # jeżeli jesteśmy w stanie stwierdzić, jakie wyjątki mogą wystąpić w naszym kodzie, powinniśmy je sprecyzować, tak jak tutaj ValueError
            logger.error("Wartość numer dwa jest niepoprawna. Proszę, podaj liczbę rzeczywistą, różną od zera.")
        # blok finally wykona się niezaleznie od wystąpienia błędu/wyjątku
        # finally:
        #     print("Blok finally")


def raise_if_val_not_float(value):
    is_value_float = type(value) == float # isinstance(value, float) - zapis alternatywny
    if not is_value_float:
        raise TypeError(f"Podana wartość jest nieprawidłowa!!! Podano wartość='{value}' typu={type(value)}. Powinien być to float.")


class MyCustomException(Exception):
    pass

def raise_my_custom_exception(error_message):
    raise MyCustomException(error_message)

handle_specific_errors_separately()