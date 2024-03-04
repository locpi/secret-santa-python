


from secretsanta.Gift import Gift
from secretsanta.Player import Player


class SecretSanta:
     __players:Player;
     def __init__(self,players:Player):
        self.__players=players;
    
     def start(self):
        if(len(self.__players)>2):
           self.searchPlayerForGift();
           self.printResult();
        else:
           print("Le jeu ne peu pas fonctionner avec un nombre de joueurs inferieur à 3")
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
            

    