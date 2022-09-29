from sae_s1_02_etu import retour_simpl_for, retablir_for

form=[[-1,-2],[-1,2,-3,4],[2,3,4],[3],[1,-4],[-1,2],[1,2]]
list_var= [True, None, True, None] 
list_chgmts= [[0, True]]

print(form)
print(retablir_for(form, list_chgmts))
print(retour_simpl_for(form, list_var, list_chgmts)[0])