


from operator import attrgetter
from random import shuffle
from secretsanta.Gift import Gift
from secretsanta.Player import Player


class SecretSanta:
     __players:Player;
     def __init__(self,players:Player):
        self.__players=players;
     
     def checkStartCondition(self):
        cptCouple=0;
        for p in self.__players:
           if(p.is_in_couple()):
              cptCouple+=1
        if(len(self.__players)<2):
           print("Le jeu ne peu pas fonctionner avec un nombre de joueurs inferieur à 3")
           return False;
        if (cptCouple/2==1 and len(self.__players)==3):
           print("Le jeu ne peu pas fonctionner avec un couple et 3 joueurs")
           return False;
        return True;
     def start(self):
        if(self.checkStartCondition()):
           shuffle(self.__players)
           self.__players= sorted(self.__players,  key=lambda employee:employee.couple,reverse=True)   
           self.searchPlayerForGift();
           self.printResult();
     
     def printResult(self):
        print("------ TIRAGE ------")
        for player in self.__players:
           print(player.get_name()+" --> "+player.get_gift_to_offer().getPlayerReceive().get_name())
        print("-----------")
     
     def getNextPlayer(self,actual):
         total=len(self.__players);
         index = self.__players.index(actual)
         if(index<total):
            index+=1
         if(index==total):
            index= 0;
         return self.__players[index]

     def searchPlayerForGift(self):
        for player in self.__players:
         playerToOffer = self.getNextPlayer(player)
         gift=Gift(player,playerToOffer);
         while gift.validate()==False:
            playerToOffer = self.getNextPlayer(playerToOffer)
            gift=Gift(player,playerToOffer);
         player.offer(gift)
         playerToOffer.receive(gift)
            

    