
#Avogadro's number
avogadro = 6.02 * (10 ** 23)

#basic conversions
def moles_to_particles(n: float):
    N = avogadro * n
    return N

def particles_to_moles(N: int):
    n = N / avogadro
    return n

#
    