import sys
from SecretSanta import SecretSanta 
from Player import Player 


COUPLES = [("Florent", "Jessica"), ("Coline", "Emilien")]
PEOPLE = ["Florent", "Jessica", "Coline", "Emilien", "Ambroise", "Bastien"]
PEOPLE_OBJECT:Player=[];
def getByName(name:str):
    for p in PEOPLE_OBJECT:
        if p.get_name()==name:
            return p;

def main():
    for p in PEOPLE:
        PEOPLE_OBJECT.append(Player(p))

    for c in COUPLES:
        cp1=getByName(c[0]);
        cp2=getByName(c[1]);   
        cp1.linkTo(cp2)
        cp2.linkTo(cp1)
    secretSanta=SecretSanta(PEOPLE_OBJECT)
    secretSanta.start()
if __name__ == '__main__':
    main();
    sys.exit(0)  # next section explains the use of sys.exit