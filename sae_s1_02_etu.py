#import numpy as np
import copy
import time


def evaluer_clause(clause,list_var):
    '''Arguments : une liste d'entiers non nuls traduisant une clause,une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : None ou booléen
    '''
    index = 0
    for _ in range(len(clause)):
        valeur = clause[index]
        if valeur < 0:
            negatif = True
            valeur = -valeur
        else:
            negatif = False
        
        if list_var[valeur - 1] == None:
            index += 1
            continue

        elif list_var[valeur - 1] == True:
            if negatif:
                del clause[index]
                continue
            else:
                return True
        
        else:
            if negatif:
                return True
            else:
                del clause[index]
                continue
    
    if len(clause) > 0:
        return None
    else:
        return False


def evaluer_cnf(formule,list_var):
    '''Arguments : une liste de listes d'entiers non nuls traduisant une formule,une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : None ou booléen
    '''
    for clause in formule:
        if evaluer_clause(clause, list_var) == None:
            return None
        elif evaluer_clause(clause, list_var) == False:
            return False
    return True



def determine_valuations(list_var):
    '''Arguments : une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : La liste de toutes les valuations (sans doublon) envisageables pour les variables de list_var
    '''
    




def resol_sat_force_brute(formule,list_var):
    '''Arguments : une liste de listes d'entiers non nuls traduisant une formule,une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : SAT,l1
    avec SAT : booléen indiquant la satisfiabilité de la formule
          l1 : une liste de valuations rendant la formule vraie ou une liste vide
'''



def init_formule_simpl_for(formule_init,list_var):
    '''
    Renvoie : La formule simplifiée en tenant compte des valeurs logiques renseignées dans list_var
'''


def enlever_litt_for(formule,litteral):
    '''Arguments :
formule : comme précédemment
litteral : un entier non nul traduisant la valeur logique prise par une variable
    Renvoie : la formule simplifiée
'''


def retablir_for(formule_init,list_chgmts):
    '''Arguments : une formule initiale et une liste de changements à apporter sur un ensemble de variables (chaque changement étant une liste [i,bool] avec i l'index qu'occupe la variable dans list_var et bool la valeur logique qui doit lui être assignée) 
    Renvoie : la formule simplifiée en tenant compte de l'ensemble des changements
'''
    

def progress(list_var,list_chgmts):
    '''Arguments : list_var, list_chgmts définies comme précédemment
    Renvoie : l1,l2
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts 
'''
    

def progress_simpl_for(formule,list_var,list_chgmts):
    '''Arguments : formule,list_var, list_chgmts définies comme précédemment
    Renvoie : form,l1,l2
    form : nouvelle formule
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts 
'''
    

def progress_simpl_for_dpll(formule,list_var,list_chgmts,list_sans_retour):
    '''Arguments : list_sans_retour contient l'ensemble des numéros de variables auxquelles on a affecté une valeur logique sur laquelle on ne reviendra pas
    renvoie :form,l1,l2,l3 avec :
    form : la formule simplifiée
    l1 : la liste actualisée des valeurs attribuées aux variables après le changement effectué
    l2 : la liste actualisée de l'ensemble des changements effectués
    l3 : la liste éventuellement actualisée des numéros de variables auxquelles une affectation a été attribuée sur laquelle on ne reviendra pas
    '''
    

def retour(list_var,list_chgmts):
    '''
    renvoie :l1,l2 avec :
    l1 : la liste actualisée des valeurs attribuées aux variables 
    l2 : la liste actualisée de l'ensemble des changements effectués depuis une formule initiale
    
    '''

def retour_simpl_for(formule_init,list_var,list_chgmts):
    '''
Renvoie : form,l1,l2
    form : nouvelle formule
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts 
'''
    

def retour_simpl_for_dpll(formule_init,list_var,list_chgmts,list_sans_retour):
    '''
Renvoie : form,l1,l2,l3
    form : nouvelle formule
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts
    l3 : nouvelle list_sans_retour
'''
    
def resol_parcours_arbre(formule_init,list_var,list_chgmts):
    '''Renvoie : SAT,l1
    avec SAT : booléen indiquant la satisfiabilité de la formule
          l1 : une liste de valuations rendant la formule vraie ou une liste vide'''
    
    

def resol_parcours_arbre_simpl_for(formule_init,formule,list_var,list_chgmts):#la même distinction peut être faite entre formule et formule_init
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide
''' 
        


def resol_parcours_arbre_simpl_for_dpll(formule_init,formule,list_var,list_chgmts,list_sans_retour):
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide
'''

        
def ultim_resol(formule_init,list_var):
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide

    Affichage possible du temps mis pour la résolution
'''

def ultim_resol_simpl_for(formule_init,list_var):
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide

    Affichage possible du temps mis pour la résolution
'''

def ultim_resol_simpl_for_dpll(formule_init,list_var):
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide

    Affichage possible du temps mis pour la résolution
'''

def creer_grille_init(list,n):
    '''Arguments : une liste de listes(contenant les coordonnées à renseigner et le nombre correspondant) et un entier donnant la taille de la grille
        Renvoie : une liste (list_grille_complete) avec les valeurs qui devront s'afficher dans la grille en la parcourant ligne après ligne de haut en bas et de gauche à droite
'''
    
def creer_grille_final(list_var,n):
    '''
    Renvoie : une liste (list_grille_complete) avec les valeurs qui devront s'afficher dans la grille (en fonction des valeurs logiques prises par les variables de list_var) en la parcourant ligne après ligne de haut en bas et de gauche à droite
'''

def afficher_grille(grille,n):
    """test"""

def for_conj_sudoku(n):
    '''
    Renvoie : la formule (liste de listes) associée à une grille de sudoku de taille n selon les attentes formulées dans le sujet
    '''
    


def init_list_var(list_grille_complete,n):
    '''
    Renvoie : une liste list_var initialisant une valuation tenant compte des valeurs non nulles déjà renseignées dans list_grille_complete
'''


'''#test enlever_litt_for
for=[[1,-2,3],[2,-3],[-1]]
print(enlever_litt_for(fofor,1))'''

'''#test evaluer_cnf
for1=[[1,2],[2,-3,4],[-1,-2],[-1,-2,-3],[1]]
list_var_for1_test1=[True,False,False,None]
print('test1 : ',evaluer_cnf(for1,list_var_for1_test1))
list_var_for1_test2=[None,False,False,None]
print('test2 : ',evaluer_cnf(for1,list_var_for1_test2))
list_var_for1_test3=[True,False,True,False]
print('test3 : ',evaluer_cnf(for1,list_var_for1_test3))'''

'''# test retour(list_var,list_chgmts)
Cas 1 :
list_var= [False, False, True, True, None] 
list_chgmts= [[0, False], [1, False], [2, True], [3, True]]
Cas 2 :
list_var= [False, False, True, False, False] 
list_chgmts= [[0, False], [1, False], [2, True], [3, False], [4, False]]
'''

'''#test resol_sat_force_brute
for1=[[1,2],[2,-3,4],[-1,-2],[-1,-2,-3],[1],[-1,2,3]]
list_var_for1=[None,None,None,None]
boo1,resul1=resol_sat_force_brute(for1,list_var_for1)
print('boo1=',boo1)
print('resul1=',resul1)


for2=[[1,4,-5],[-1,-5],[2,-3,5],[2,-4],[2,4,5],[-1,-2],[-1,2,-3],[-2,4,-5],[1,-2]]
list_var_for2=[None,None,None,None,None]
boo2,resul2=resol_sat_force_brute(for2,list_var_for2)
print('boo2=',boo2)
print('resul2=',resul2)


for3=[[-1,-2],[-1,2,-3,4],[2,3,4],[3],[1,-4],[-1,2],[1,2]]
list_var_for3=[None,None,None,None]
boo3,resul3=resol_sat_force_brute(for3,list_var_for3)
print('boo3=',boo3)
print('resul3=',resul3)
'''

'''#test ultim_resol
for2=[[1,4,-5],[-1,-5],[2,-3,5],[2,-4],[2,4,5],[-1,-2],[-1,2,-3],[-2,4,-5],[1,-2]]
list_var_for2=[None,None,None,None,None]
boo_for2,lilifor2=ultim_resol(for2,list_var_for2)
print('boo_for2 : ',boo_for2)
print('lilifor2 : ',lilifor2)'''


'''#test for_conj_sudoku
#Cas grille Taille 2
formul_sudok2=for_conj_sudoku(2)
print("formul_sudok taille 2: \n",formul_sudok2)

#Cas grille Taille 3
formul_sudok3=for_conj_sudoku(3)
print("formul_sudok taille 3: \n",formul_sudok3)'''

'''test creer_grille_init & init_list_var cas2
list_grille2=[[1,2,1],[2,1,4],[2,2,2],[3,3,2],[4,2,3]]
grille2=creer_grille_init(list_grille2,2)
list_var_grille2=init_list_var(grille2,2)
'''

'''#test ultim_resol_simpl_for
#Cas grille Taille 2
formul_sudok2=for_conj_sudoku(2)
list_grille2=[[1,2,1],[2,1,4],[2,2,2],[3,3,2],[4,2,3]]
list_grille2_f=[[1,2,4],[2,1,4],[2,2,2],[3,3,2],[4,2,3]]
grille2=creer_grille_init(list_grille2,2)
afficher_grille(grille2,2)
list_var_grille2=init_list_var(grille2,2)
boo_2,lili2=ultim_resol_simpl_for(formul_sudok2,list_var_grille2)
#corrigé lili2=[False, False, True, False, True, False, False, False, False, False, False, True, False, True, False, False, False, False, False, True, False, True, False, False, False, False, True, False, True, False, False, False, True, False, False, False, False, False, False, True, False, True, False, False, False, False, True, False, False, True, False, False, False, False, True, False, True, False, False, False, False, False, False, True]
if boo_2:
    afficher_grille(creer_grille_final(lili2,2),2)
grille2f=creer_grille_init(list_grille2_f,2)
afficher_grille(grille2f,2)
list_var_grille2f=init_list_var(grille2f,2)
boo_2f,lili2f=ultim_resol_simpl_for(formul_sudok2,list_var_grille2f)
if boo_2f:
    afficher_grille(creer_grille_final(lili2f,2),2)'''


'''#test ultim_resol_simpl_for
#Cas grille Taille 3
formul_sudok=for_conj_sudoku(3)
list_grille3=[[1,3,2],[1,6,5],[2,5,4],[2,8,9],[2,9,3],[3,2,7],[3,9,6],[4,3,1],[4,4,8],[4,8,3],[5,1,7],[5,2,2],[5,5,6],[5,8,8],[5,9,4],[6,2,4],[6,6,2],[6,7,5],[7,1,3],[7,8,1],[8,1,4],[8,2,6],[8,5,7],[9,4,9],[9,7,8]]
grille1=creer_grille_init(list_grille3,3)
afficher_grille(grille3,3)
list_var_grille3=init_list_var(grille3,3)
boo_3,lili3=ultim_resol_simpl_for(formul_sudok,list_var_grille3)
if boo_3:
    afficher_grille(creer_grille_final(lili3,3),3)
'''



'''#test ultim_resol_simpl_for_dpll cas3
formul_sudok=for_conj_sudoku(3)
list_grille3=[[1,3,2],[1,6,5],[2,5,4],[2,8,9],[2,9,3],[3,2,7],[3,9,6],[4,3,1],[4,4,8],[4,8,3],[5,1,7],[5,2,2],[5,5,6],[5,8,8],[5,9,4],[6,2,4],[6,6,2],[6,7,5],[7,1,3],[7,8,1],[8,1,4],[8,2,6],[8,5,7],[9,4,9],[9,7,8]]
grille3=creer_grille_init(list_grille3,3)
afficher_grille(grille3,3)
list_var_grille3=init_list_var(grille3,3)
boo_3,lili3=ultim_resol_simpl_for_dpll(formul_sudok,list_var_grille3)
if boo_3:
    afficher_grille(creer_grille_final(lili3,3),3)'''




