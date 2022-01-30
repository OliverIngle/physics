# Mass concentation formula
#
#       t = m / V
#
#   >   t = n * M / V
#
#   >   t = n / V * M
#
#   >   t = C * M
#

def concentration(m: float, V: float):
    return m / V

def mass(t: float, V: float):
    return t * V

def volume(t: float, m: float):
    return m / t

def concentratio_from_molar_mass(C: float, M: float):
    return C * M