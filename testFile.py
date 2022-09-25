from sae_s1_02_etu import evaluer_cnf

formule =   [[1,2,-3],[-1,-2],[-1,3],[-1,2,-3]]
list_var = [False, True, None]

retour = evaluer_cnf(formule, list_var)

print(f"La valeur {retour} a été retournée")

"""
[False, True, None]
[1,2,-3] -> 2
[-1,-2] -> -1
[-1,3] -> -1
[-1,2,-3] -> -1 et 2
True
"""