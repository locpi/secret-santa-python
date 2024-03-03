
import Gift as Gift;

class Player:
    __name:str;
    __link= None
    __giftToOffer:Gift=None;
    __giftToReceive:Gift=None;

    def __init__(self,name:str):
        self.__name=name;
    def get_name(self):
        return self.__name
    
    def get_gift_to_offer(self):
        return self.__giftToOffer;

    def get_gift_to_receive(self):
        return self.__giftToReceive;

    def linkTo(self,player):
        self.__link=player

    def isLinkToAnotherPlayer(self,player):
        if self.__link != None:
            return self.__link.get_name()==player.get_name()
        return False;

    def offer(self,gift:Gift):
        self.__giftToOffer = gift;
    
    def receive(self,gift:Gift):
        self.__giftToReceive = gift;
