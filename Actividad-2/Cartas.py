class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta
#constantes
DIAMONDS = "Diamantes"
HEARTS = "Corazones"
CLUBS = "Tréboles"
PIKES = "Picas"

carta1 = Carta("As", PIKES)
carta2 = Carta("10", HEARTS)

print("Carta 1 - Valor:", carta1.valor, "Pinta:", carta1.pinta)
print("Carta 2 - Valor:", carta2.valor, "Pinta:", carta2.pinta)
