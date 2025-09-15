def f1 () :
    return 42
def f2 (x):
    return 2 * x
print ( f1 () ) #appel la fonction f1 qui renvoie 42 donc va print 42
print ( f2 (5) + f1 () )#ajoute le résultat de la fonction f2 avec comme argument 5 (donc 2*5 = 10) et ajoute à la fonction f1 et print donc affiche 52