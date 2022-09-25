from sae_s1_02_etu import resol_sat_force_brute, determine_valuations

formule =   [[-1,-2],[1],[-1]]
list_var = [None, None]

satisfiabilite, var = resol_sat_force_brute(formule, list_var)

print(f"La formule est satisbiable : {satisfiabilite} | {var}")

"""
[False, False, False]
[1,2,-3] -> -3
[-1,-2] -> -1
[-1,3] -> -1
[-1,2,-3] ->
"""