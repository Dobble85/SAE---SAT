from sae_s1_02_etu import creer_grille_final, init_list_var, creer_grille_init
print(chr(27) + "[2J")

i = 2
print(creer_grille_final(init_list_var(creer_grille_init([[1,2,1],[2,1,4],[2,2,2],[3,3,2],[4,2,3]], i), i), i))

"""
[[-4], [2]]

2: 15
3: 33

[[-4], [2]] [False, None, True, None] [[2, True], [0, False]] [2]
"""