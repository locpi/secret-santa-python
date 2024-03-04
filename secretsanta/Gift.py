

from secretsanta import Player


class Gift:
    __playerOffer:Player;
    __playerReceive:Player;
    def __init__(self, playerOffer:Player,playerReceive:Player):
        self.__playerOffer=playerOffer
        self.__playerReceive=playerReceive

    def getPlayerReceive(self):
        return self.__playerReceive;
    
    def getPlayerOffer(self):
        return self.getPlayerOffer;

    def validate(self):
        if(self.playerHaveAGift()):
            return False;
        if(self.haveReciprocityBetweenPlayer()):
            return False;
        if(self.isSamePlayer()):
            return False;
        if(self.__playerOffer.isLinkToAnotherPlayer(self.__playerReceive)):
            return False;
        return True;

    def playerHaveAGift(self):
        return self.__playerReceive.get_gift_to_receive()!=None

    def isSamePlayer(self):
        return self.__playerOffer.get_name()==self.__playerReceive.get_name()

    def haveReciprocityBetweenPlayer(self):
        if(self.__playerReceive.get_gift_to_offer()):
            giftToOffer=self.__playerReceive.get_gift_to_offer();
            if(giftToOffer.getPlayerReceive().get_name()==self.__playerOffer.get_name()):
                return True;
        return False;