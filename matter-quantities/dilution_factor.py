# Dilution factor equation
#
#       F = tmother / tchild
#
#         = Cmother / Cchild
#
#         = Vchild / Vmother
#

def from_mass_concentration(tmother:float, tchild:float):
    return tmother / tchild
    
def from_molar_concentration(Cmother:float, Cchild:float):
    return Cmother / Cchild
    
def from_volume(Vchild:float, Vmother:float):
    return Vchild / Vmother