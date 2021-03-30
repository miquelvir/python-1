# RECORDA ANAR A MAIN.PY PER CAMBIAR L'EXERCICI QUE S'EXECUTA AL CLICAR LA FLETXA VERDA

"""
Fins ara has après:
    - print() per imprimir missatges
    - les strings/texts van sempre entre cometes
    - input() per fer preguntes a l'usuari
    - les variables per guardar la resposta o qualsevol informació

Ara aprendràs a cambiar parts de texts:
"""

text = "thas as some long text"

# a la variable text les 'a' haurien de ser 'i'!
# podem usar la següent funció per cambiar les lletres equivocades:

fixed_text = text.replace('a', 'i')  # cambiarà totes les 'a' per 'i'
print(fixed_text)

# EXERCISE - 3 MARKS
# 1. Pregunta a l'usuari un text.
# 2. Imprimeix el text que ha dit.
# 3. Imprimeix el text que ha dit, però cambia totes les 'a' per 'i'.

src = input()
print(src)
print(src.replace('a', 'i'))