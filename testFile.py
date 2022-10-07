from sae_s1_02_etu import progress_simpl_for_dpll

form=[[-1,-2],[-1,2,-3,4],[2,3,4],[3],[1,-4],[-1,2],[1,2]]
list_var= [None, None, None, None] 

print(chr(27) + "[2J")

print(form)
print(progress_simpl_for_dpll(form, list_var))

