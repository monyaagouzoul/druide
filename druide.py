def possible(n):
    """
      Affiche si une corde à n noeuds est une corde de druide.
    """
    for hypo in range(1,n-2):
        for cote1 in range (1,hypo):
            cote2=(n-1)-hypo-cote1
            if 0<cote2<hypo and hypo**2==cote2**2+cote1**2:
                print(cote1,cote2,hypo)
                return 1
        return 0
    for i in range(13):
        if possible(i)==0:
            print("impo avec",i,"noeuds")
        else:
            print("possible avec",i,"noeuds")
i=14
nb=0
while nb<10:
    if possible(i)==1:
        print("on peut construire une corde à ",i,"noeuds")
        nb+=1
    i+=1
