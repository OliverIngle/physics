# Molar volume formula
#
#       V = n * Vm
#
#       Vm = V / n
#

def molar_volume(n: float, V: float):
    return V / n

def volume(n: float, Vm: float):
    return n * Vm

def moles(V: float, Vm: float):
    return V / Vm