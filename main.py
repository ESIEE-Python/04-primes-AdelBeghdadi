#main.py
"""
author = adel.beghdadi@edu.esiee.fr
"""

def isprime(p):
    """
    Retourne si p est un nombre entier ou non

    Args:
        p: Valeur entière positive

    Returns:
        isprime(p) : True or False
    """
    if p in (0, 1):
        return False
    for i in range(2,p):
        if p % i == 0:
            return False
    return True

def main():
    """
    Fonction principale qui va tester les nombres de 0 à 100 
    et écrire dans la sortie les nombres premiers

    Args: 

    Returns:
        main() : Null
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()
if __name__ == "__main__":
    main()
