import logging # paczka pythonowa służąca do logowania przebiegu programu
# from some_other_logger import some_function


# DEBUG - służy do debugowania kodu, jest najniższym poziomem logowania
# INFO - info służy do logowania nieco mniej szczegółowych informacji na temat wykonywania się programu
# WARNING - służy do ostrzegania przed potęcjalnymi niezgodnościami/błędami w programie
# ERROR - służy do logowania wyjątków w naszym programie
# CRITICAL - używany zazwyczaj do logowania błędów powodujących zatrzymanie działania programu, bądź potencjalne uszkodzenie naszeych komponentów (np. bazy danych)


# FORMAT = '%(name)s - %(levelname)s - %(message)s'
# logowanie do stdout, czyli w konsoli
# logging.basicConfig(level=logging.DEBUG, format='%(name)s-%(levelname)s-%(message)s') # basicConfig pozwala na ustawienie konfiguracji loggera, np. poziom loggingu
# logowanie do pliku
# logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# logger = logging.getLogger("some name") # getLogger zwraca logger o nazwie podanej jako parametr
# some_function("SOME ANOTHER VALUE")
# logger.debug("This is some logger message.")
# logging.debug("This is debug message")
# logging.info("This is info message")
# logging.warning("This is warning message")
# logging.error("This is error message")
# logging.critical("This is critical message")