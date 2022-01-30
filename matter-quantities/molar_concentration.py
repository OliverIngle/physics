# Molar concentation formula
#
#       C = n / V
#


def concentration(n: float, V: float):
    return n / V

def moles(C: float, V: float):
    return C * V

def volume(C: float, n: float):
    return n / C