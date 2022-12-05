from sae_s1_02_etu import *
# ! resol_parcours_arbre_simpl_for_dpll -> echanger formule et formule_init dans progress et retour


def test(mess,eval,res):
    print(mess,(eval==res)*'OK'+(eval!=res)*'Try again')
def test_determine_valuations(mess,list_var,res):
    test=mess+'Ok'
    list_testee=determine_valuations(list_var)
    for el in list_testee :
        if el not in res:
            test=mess+'Try again'
            return test
    for el in res:
        if el not in list_testee :
            test=mess+'Try again'
            return test
    for i in range(len(list_testee)-1):
        if list_testee[i] in list_testee[i+1:]:
            test=mess+'wowowow y a du doublon là-dedans'
            return test
    return test  
def test_for(mess,formu,res_for):
    res=True
    for el1 in formu:
        for el2 in res_for:
            res=(set(el1)==set(el2))
            if res :
                break
        if not res :
            print(mess+'Try again !')
            return
    for el2 in res_for:
        for el1 in formu:
            res=(set(el2)==set(el1))
            if res :
                break
        if not res :
            print(mess+'Try again !')
            return
    res=False
    for i in range(len(formu)-1):
        for el in formu[i+1:]:
            if set(formu[i])==set(el):
                print(mess+'wowowow y a du doublon là-dedans')
                return 
    print(mess+'Ok')

list_var_fin=[False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, True, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, True, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, True, False, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, False, False, False, False, False, False, True, False, False, False, False, True, False, False, False, False, False, False, False, False, False, True, False, False, False, False]
cor_grille_final=[9, 3, 2, 6, 1, 5, 4, 7, 8, 5, 8, 6, 2, 4, 7, 1, 9, 3, 1, 7, 4, 3, 8, 9, 2, 5, 6, 6, 9, 1, 8, 5, 4, 7, 3, 2, 7, 2, 5, 1, 6, 3, 9, 8, 4, 8, 4, 3, 7, 9, 2, 5, 6, 1, 3, 5, 9, 4, 2, 8, 6, 1, 7, 4, 6, 8, 5, 7, 1, 3, 2, 9, 2, 1, 7, 9, 3, 6, 8, 4, 5]
test("essai creer_grille_final : ",creer_grille_final(list_var_fin,3),cor_grille_final)