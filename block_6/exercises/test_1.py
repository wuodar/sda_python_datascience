"""
Napisz test funkcji hide_password przy użyciu biblioteki unittest
"""

def hide_password(password):
    """Ukrywa co trzecia litere w hasle password.

    :param password: haslo z gwiazdkami co trzecia litere.
    :return: napis z czesciowo ukrytym haslem.

    """
    signs = list(password)

    for i, sign in enumerate(signs):
        if i > 1 and (i+1) % 3 == 0:
            signs[i] = "*"

    return "".join(signs)

