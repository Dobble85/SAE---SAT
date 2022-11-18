from sae_s1_02_etu import init_list_var, creer_grille_init, for_conj_sudoku

print(chr(27) + "[2J")

i = 2
print(len(init_list_var(creer_grille_init([[1,2,1],[2,1,4],[2,2,2],[3,3,2],[4,2,3]], i), i)))
#print(for_conj_sudoku(i))

"""
[[-4], [2]]

2: 15
3: 33

[[-4], [2]] [False, None, True, None] [[2, True], [0, False]] [2]
"""