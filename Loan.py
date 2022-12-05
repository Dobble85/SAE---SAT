def for_conj_sudoku(n):
    '''
    Renvoie : la formule (liste de listes) associée à une grille de sudoku de taille n selon les attentes formulées dans le sujet
    '''
    formule=[]
    for ligne in range(n**2):
        for valeur in range(n**2):
            clause=[]
            for case in range(n**2):
                clause.append(ligne*n**4+case*n**2+valeur+1)
            formule.append(clause)

    for colonne in range(n**2):
        for valeur in range(n**2):
            clause=[]
            for case in range(n**2):
                clause.append(colonne*n**2+case*n**4+valeur+1)
            formule.append(clause)
    
    for region_ligne in range(n):
        for region_colonne in range(n):
            for valeur in range(n**2):
                clause=[]
                for ligne in range(n):
                    for colonne in range(n):
                        clause.append(region_ligne*n**5+region_colonne*n**3+ligne*n**4+colonne*n**2+valeur+1)
                formule.append(clause)
    
    for ligne in range(n**2):
        for case in range(n**2):
            for valeur1 in range(n**2-1):
                for valeur2 in range(n**2):
                    if valeur2>valeur1:
                        formule.append([-(ligne*n**4+case*n**2+valeur1+1),-(ligne*n**4+case*n**2+valeur2+1)])

    for ligne in range(n**2):
        for valeur in range(n**2):
            for case1 in range(n**2-1):
                for case2 in range(n**2):
                    if case2>case1:
                        formule.append([-(n**4*ligne+n**2*case1+valeur+1),-(n**4*ligne+n**2*case2+valeur+1)])
    
    for colonne in range(n**2):
        for valeur in range(n**2):
            for case1 in range(n**2-1):
                for case2 in range(n**2):
                    if case2>case1:
                        formule.append([-(n**2*colonne+n**4*case1+valeur+1),-(n**2*colonne+n**4*case2+valeur+1)])

    for region_ligne in range(n):
        for region_colonne in range(n):
            for valeur in range(n**2):
                for ligne_case1 in range(n):
                    for colonne_case1 in range(n):
                        for ligne_case2 in range(n):
                            for colonne_case2 in range(n):
                                if ligne_case2<ligne_case1 and colonne_case2!=colonne_case1:
                                    formule.append([-(n**5*region_ligne+n**4*ligne_case1+n**3*region_colonne+n**2*colonne_case1+valeur+1),-(n**5*region_ligne+n**4*ligne_case2+n**3*region_colonne+n**2*colonne_case2+valeur+1)])

    return formule
