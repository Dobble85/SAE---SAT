#import numpy as np
import copy
import time


def evaluer_clause(clause,list_var):
    '''Arguments : une liste d'entiers non nuls traduisant une clause,une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : None ou booléen
    '''
    nbNons = 0
    for valeur in clause:
        if valeur < 0:
            negatif = True
            valeur = -valeur
        else:
            negatif = False
        
        if list_var[valeur - 1] == None:
            continue

        elif list_var[valeur - 1] == True:
            if negatif:
                nbNons += 1
            else:
                return True
        
        else:
            if negatif:
                return True
            else:
                nbNons += 1
    
    if len(clause) == nbNons:
        return False
    else:
        return None


def evaluer_cnf(formule,list_var):
    '''Arguments : une liste de listes d'entiers non nuls traduisant une formule,une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : None ou booléen
    '''
    noneEval = False

    if [] in formule :
        return False

    for index, clause in enumerate(formule):
        if len(clause) == 1:
            for clause2 in formule[index+1:]:
                if len(clause2) == 1 and clause2[0] == -clause[0]:
                    return False
    
        if evaluer_clause(clause, list_var) == None:
            noneEval = True
        elif evaluer_clause(clause, list_var) == False:
            return False
    
    if noneEval:
        return None
    else:
        return True


def determine_valuations(list_var):
    '''Arguments : une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : La liste de toutes les valuations (sans doublon) envisageables pour les variables de list_var
    '''
    def Desimbriquer(listPoss):
        if type(listPoss[0][0]) == list:
            nvListe = [item for l in listPoss for item in l]
            return Desimbriquer(nvListe)
        else:
            return listPoss
    
    if None not in list_var:
        return list_var
    
    list_possibilities = list()

    for index, var in enumerate(list_var):
        if var != None:
            continue

        else:
            possibilite1 = list_var[:index]
            possibilite1.append(False)
            possibilite1.extend(list_var[index+1:])
            list_possibilities.append(determine_valuations(possibilite1))
            
            possibilite2 = list_var[:index]
            possibilite2.append(True)
            possibilite2.extend(list_var[index+1:])
            list_possibilities.append(determine_valuations(possibilite2))
            break

    list_possibilities = Desimbriquer(list_possibilities)
    return list_possibilities

def resol_sat_force_brute(formule,list_var):
    '''Arguments : une liste de listes d'entiers non nuls traduisant une formule,une liste de booléens informant de valeurs logiques connues (ou None dans le cas contraire) pour un ensemble de variables
    Renvoie : SAT,l1
    avec SAT : booléen indiquant la satisfiabilité de la formule
          l1 : une liste de valuations rendant la formule vraie ou une liste vide
    '''
    listVarPossibles = determine_valuations(list_var)
    for var in listVarPossibles:
        if evaluer_cnf(formule, var) == True:
            return True, var
    return False, []


def enlever_litt_for(formule,litteral):
    '''Arguments :
formule : comme précédemment
litteral : un entier non nul traduisant la valeur logique prise par une variable
    Renvoie : la formule simplifiée
'''
    return [[item for item in clause if item != -litteral] for clause in formule if litteral not in clause]
    nvFormule = []
    for clause in formule:
        if litteral not in clause:
            clauseTemp = []
            for item in clause:
                if item != -litteral:
                    clauseTemp.append(item)
            nvFormule.append(clauseTemp)
    return nvFormule



def retablir_for(formule_init,list_chgmts):
    '''Arguments : une formule initiale et une liste de changements à apporter sur un ensemble de variables (chaque changement étant une liste [i,bool] avec i l'index qu'occupe la variable dans list_var et bool la valeur logique qui doit lui être assignée) 
    Renvoie : la formule simplifiée en tenant compte de l'ensemble des changements
    '''
    for index, bool in list_chgmts:
        if bool == True:
            formule_init = enlever_litt_for(formule_init, (index + 1))
        elif bool == False:
            formule_init = enlever_litt_for(formule_init, -(index + 1))
    return formule_init


def init_formule_simpl_for(formule_init,list_var):
    '''
    Renvoie : La formule simplifiée en tenant compte des valeurs logiques renseignées dans list_var
    '''
    for index, variable in enumerate(list_var):
        if variable == True:
            formule_init = enlever_litt_for(formule_init, (index+1))
        elif variable == False:
            formule_init = enlever_litt_for(formule_init, -(index+1))
    return formule_init


def progress(list_var,list_chgmts):
    '''Arguments : list_var, list_chgmts définies comme précédemment
    Renvoie : l1,l2
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts 
    '''
    for index, valeur in enumerate(list_var):
        if valeur == None:
            nvListVar = list_var[:index]
            nvListVar.append(True)
            nvListVar.extend(list_var[index+1:])

            list_chgmts.append([index, True])

            return nvListVar, list_chgmts
    return list_var, list_chgmts
    

def progress_simpl_for(formule,list_var,list_chgmts):
    '''Arguments : formule,list_var, list_chgmts définies comme précédemment
    Renvoie : form,l1,l2
    form : nouvelle formule
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts 
    '''
    for index, valeur in enumerate(list_var):
        if valeur == None:
            nvListVar = list_var[:index]
            nvListVar.append(True)
            nvListVar.extend(list_var[index+1:])

            list_chgmts.append([index, True])

            formule = enlever_litt_for(formule, index+1)

            return formule, nvListVar, list_chgmts
    return formule, list_var, list_chgmts


def progress_simpl_for_dpll(formule,list_var,list_chgmts = [],list_sans_retour = []):
    '''Arguments : list_sans_retour contient l'ensemble des numéros de variables auxquelles on a affecté une valeur logique sur laquelle on ne reviendra pas
    renvoie :form,l1,l2,l3 avec :
    form : la formule simplifiée
    l1 : la liste actualisée des valeurs attribuées aux variables après le changement effectué
    l2 : la liste actualisée de l'ensemble des changements effectués
    l3 : la liste éventuellement actualisée des numéros de variables auxquelles une affectation a été attribuée sur laquelle on ne reviendra pas
    '''

    """ TEST CLAUSE UNITAIRE + CALCUL LITERAL PUR """
    dico = {}
    for index, valeur in enumerate(formule):
        if len(valeur) == 1:
            nvListVar = list_var[:abs(valeur[0])-1]
            nvListVar.append(valeur[0] > 0)
            nvListVar.extend(list_var[abs(valeur[0]):])

            list_chgmts.append([abs(valeur[0])-1, valeur[0] > 0])
            list_sans_retour.append(abs(valeur[0])-1)

            formule = enlever_litt_for(formule, valeur[0])

            return formule, nvListVar, list_chgmts, list_sans_retour
        
        else:
            for valu in valeur:
                if valu < 0:
                    if -valu in dico.keys():
                        dico[-valu][1] += 1
                    else:
                        dico[-valu] = [0, 1]
                else:
                    if valu in dico.keys():
                        dico[valu][0] += 1
                    else:
                        dico[valu] = [1, 0]
    
    """ TEST LITERAL PUR """
    for cle, valeur in dico.items():
        if valeur[0] == 0:
            nvListVar = list_var[:cle-1]
            nvListVar.append(False)
            nvListVar.extend(list_var[cle:])

            list_chgmts.append([cle-1, False])
            list_sans_retour.append(cle-1)

            formule = enlever_litt_for(formule, -cle)

            return formule, nvListVar, list_chgmts, list_sans_retour

        elif valeur[1] == 0:
            nvListVar = list_var[:cle-1]
            nvListVar.append(True)
            nvListVar.extend(list_var[cle:])

            list_chgmts.append([cle-1, True])
            list_sans_retour.append(cle-1)

            formule = enlever_litt_for(formule, cle)

            return formule, nvListVar, list_chgmts, list_sans_retour
    
    """ PAR DEFAUT """

    for index, valeur in enumerate(list_var):
        if valeur == None:
            nvListVar = list_var[:index]
            nvListVar.append(True)
            nvListVar.extend(list_var[index+1:])

            list_chgmts.append([index, True])

            formule = enlever_litt_for(formule, index+1)

            return formule, nvListVar, list_chgmts, list_sans_retour
    return formule, list_var, list_chgmts, list_sans_retour
    
    

def retour(list_var,list_chgmts):
    '''
    renvoie :l1,l2 avec :
    l1 : la liste actualisée des valeurs attribuées aux variables 
    l2 : la liste actualisée de l'ensemble des changements effectués depuis une formule initiale
    '''
    if len(list_chgmts) == 0:
        return list_var, list_chgmts
    
    index = len(list_chgmts) - 1
    for _ in range(len(list_chgmts)):
        changement = list_chgmts[index]
        if changement[1] == False:
            del list_chgmts[index]
            index -= 1
            list_var[changement[0]] = None

        elif changement[1] == True:
            list_chgmts[index] = [changement[0], False]
            list_var[changement[0]] = False
            break
    return list_var, list_chgmts


def retour_simpl_for(formule_init,list_var,list_chgmts):
    '''
    Renvoie : form,l1,l2
    form : nouvelle formule
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts 
    '''
    list_var, list_chgmts = retour(list_var,list_chgmts)
    formule = retablir_for(formule_init, list_chgmts)
    return formule, list_var, list_chgmts
    

def retour_simpl_for_dpll(formule_init,list_var,list_chgmts,list_sans_retour):
    '''
    Renvoie : form,l1,l2,l3
    form : nouvelle formule
    l1 : nouvelle list_var 
    l2 : nouvelle list_chgmts
    l3 : nouvelle list_sans_retour
    '''
    if len(list_chgmts) == 0:
        return formule_init, list_var, list_chgmts, list_sans_retour
    
    index = len(list_chgmts) - 1
    for _ in range(len(list_chgmts)):
        changement = list_chgmts[index]
        if changement[0] in list_sans_retour:

            del list_chgmts[index]
            list_sans_retour.remove(changement[0])
            index -= 1
            list_var[changement[0]] = None

        else:
            if changement[1] == False:
                del list_chgmts[index]
                index -= 1
                list_var[changement[0]] = None
            elif changement[1] == True:
                list_chgmts[index] = [changement[0], False]
                list_var[changement[0]] = False
                break

    formule = retablir_for(formule_init, list_chgmts)
    return formule, list_var, list_chgmts, list_sans_retour
    
def resol_parcours_arbre(formule_init,list_var,list_chgmts):
    '''Renvoie : SAT,l1
    avec SAT : booléen indiquant la satisfiabilité de la formule
          l1 : une liste de valuations rendant la formule vraie ou une liste vide'''
    evalCnf = evaluer_cnf(formule_init, list_var)
    if evalCnf == True:
        return True, list_var
    elif evalCnf == False:
        nvListVar, nvListChgmts = retour(list_var,list_chgmts)
        if len(nvListChgmts) == 0:
            return False, []
        return resol_parcours_arbre(formule_init, nvListVar, nvListChgmts)
    else:
        nvListVar, nvListChgmts = progress(list_var, list_chgmts)
        return resol_parcours_arbre(formule_init, nvListVar, nvListChgmts)
    

def resol_parcours_arbre_simpl_for(formule_init,formule,list_var,list_chgmts):#la même distinction peut être faite entre formule et formule_init
    '''
    Renvoie SAT,l1 avec :
    SAT=True ou False
    l1=une liste de valuations rendant la formule vraie ou une liste vide
    '''     
    evalCnf = evaluer_cnf(formule, list_var)
    if evalCnf == True:
        return True, list_var
    elif evalCnf == False:
        nvFormule, nvListVar, nvListChgmts = retour_simpl_for(formule_init, list_var, list_chgmts)
        if len(nvListChgmts) == 0:
            return False, []
        return resol_parcours_arbre_simpl_for(formule_init, nvFormule, nvListVar, nvListChgmts)
    else:
        nvFormule, nvListVar, nvListChgmts = progress_simpl_for(formule, list_var, list_chgmts)
        return resol_parcours_arbre_simpl_for(formule_init, nvFormule, nvListVar, nvListChgmts)
        


def resol_parcours_arbre_simpl_for_dpll(formule_init : list,formule : list,list_var : list,list_chgmts : list,list_sans_retour : list):
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide
'''
    evalCnf = evaluer_cnf(formule, list_var)
    if evalCnf == True:
        return True, list_var

    elif evalCnf == False:
        nvFormule, nvListVar, nvListChgmts, nvListSansRetour = retour_simpl_for_dpll(formule_init, list_var, list_chgmts, list_sans_retour)
        if len(nvListChgmts) == 0:
            return False, []
        return resol_parcours_arbre_simpl_for_dpll(formule_init, nvFormule, nvListVar, nvListChgmts, nvListSansRetour)

    else:
        nvFormule, nvListVar, nvListChgmts, nvListSansRetour = progress_simpl_for_dpll(formule, list_var, list_chgmts, list_sans_retour)
        return resol_parcours_arbre_simpl_for_dpll(formule_init, nvFormule, nvListVar, nvListChgmts, nvListSansRetour)

        
def ultim_resol(formule_init,list_var):
    '''
    Renvoie SAT,l1 avec :
    SAT=True ou False
    l1=une liste de valuations rendant la formule vraie ou une liste vide

    Affichage possible du temps mis pour la résolution
    '''
    return resol_parcours_arbre(formule_init,list_var, [])


def ultim_resol_simpl_for(formule_init,list_var):
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide

    Affichage possible du temps mis pour la résolution
'''
    formule = init_formule_simpl_for(formule_init,list_var)
    return resol_parcours_arbre_simpl_for(formule_init, formule, list_var, [])

def ultim_resol_simpl_for_dpll(formule_init,list_var):
    '''
    Renvoie SAT,l1 avec :
SAT=True ou False
l1=une liste de valuations rendant la formule vraie ou une liste vide

    Affichage possible du temps mis pour la résolution
'''
    formule = init_formule_simpl_for(formule_init,list_var)
    return resol_parcours_arbre_simpl_for_dpll(formule_init, formule, list_var, [], [])





def creer_grille_init(list,n):
    '''Arguments : une liste de listes(contenant les coordonnées à renseigner et le nombre correspondant) et un entier donnant la taille de la grille
        Renvoie : une liste (list_grille_complete) avec les valeurs qui devront s'afficher dans la grille en la parcourant ligne après ligne de haut en bas et de gauche à droite
    '''
    tab = [0]* n**4
    for coords in list:
        y,x,val = coords
        tab[x-1 + (y-1)*n**2] = val
    return tab
    

def afficher_grille(grille,n):
    """test 1212"""
    newTab = np.reshape(grille, (n**2,n**2))

    for indexLigne, ligne in enumerate(newTab):
        if indexLigne % n == 0 and indexLigne != 0:
            print('-'*(len(txt)+1))

        txt = ''
        for indexColonne, val in enumerate(ligne):
            if indexColonne % n == 0 and indexColonne != 0:
                txt += ' |'
            txt += f' {val%(n+1)**2}'
        print(txt)

        



def for_conj_sudoku(n):
    '''
    Renvoie : la formule (liste de listes) associée à une grille de sudoku de taille n selon les attentes formulées dans le sujet
    '''
    tab = [[i*n**2 + temp for temp in range(1,(n**2)+1)] for i in range(n**4)]

    reg = []
    for i in range(n**2):
        reg.append([])
        for j in range(n):
            for k in range(n):
                reg[i].append(k + (j*n**2) + (i*n))
    
    lignes = [[i+j*n**2 for i in range(n**2)]for j in range(n**2)]
    colonnes = [[j+i*n**2 for i in range(n**2)]for j in range(n**2)]

    formule = []
    for indexCase, case in enumerate(tab):
        for indexVar, variable in enumerate(case):
            form = [variable]
            for ligne in lignes:
                if indexCase in ligne:
                    for var in ligne:
                        valVar = tab[var][indexVar]
                        if valVar != variable:
                            formule.append(form + [-(tab[var][indexVar])])
                    break
                else:
                    continue

            for col in colonnes:
                if indexCase in col:
                    for var in col:
                        valVar = tab[var][indexVar]
                        if valVar != variable:
                            formule.append(form + [-(tab[var][indexVar])])
                    break
                else:
                    continue

            for sousReg in reg:
                if indexCase in sousReg:
                    for var in sousReg:
                        valVar = tab[var][indexVar]
                        if valVar != variable:
                            formule.append(form + [-(tab[var][indexVar])])
                    break
                else:
                    continue
            
            for _, nombre in enumerate(case):
                if nombre != variable:
                    form.append(-nombre)
            formule.append(form)
        formule.append(case)
            
    return formule


def init_list_var(list_grille_complete,n):
    '''
    Renvoie : une liste list_var initialisant une valuation tenant compte des valeurs non nulles déjà renseignées dans list_grille_complete
'''
    listVar = []
    for val in list_grille_complete:
        if val == 0:
            listVar += [None] * n**2
        else:
            listVar += [False] * (val-1) + [True] + [False] * (n**2 - val)
    return listVar



def creer_grille_final(list_var,n):
    '''
    Renvoie : une liste (list_grille_complete) avec les valeurs qui devront s'afficher dans la grille (en fonction des valeurs logiques prises par les variables de list_var) en la parcourant ligne après ligne de haut en bas et de gauche à droite
    '''
    tab = []
    for index in range(n**4):
        val = list_var[index*n**2:(index+1)*n**2].index(True)
        tab.append(val+1)
    return tab

