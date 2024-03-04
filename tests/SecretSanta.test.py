import unittest
from secretsanta.Gift import Gift
from secretsanta.Player import Player
from secretsanta.SecretSanta import SecretSanta

class SecretSantaTest(unittest.TestCase):

    def test_false_if_person_offer_gift(self):
        loic=Player("loic")
        paul=Player("Paul")

        giftLoicPaul=Gift(loic,paul)
        giftPaulLoic=Gift(paul,loic)
        self.assertEqual(giftLoicPaul.validate(),True)
        loic.offer(giftLoicPaul)
        self.assertEqual(giftPaulLoic.validate(),False)
    
    def test_false_if_person_is_linked_to_another_person(self):
        loic=Player("loic")
        lucie=Player("Lucie")
        loic.linkTo(lucie)
        lucie.linkTo(loic)
        gift=Gift(loic,lucie)
        self.assertEqual(gift.validate(),False)

    def test_each_person_receive_one_gift_with_two_couple(self):
        loic=Player("Loic")
        lucie=Player("Lucie")
        bruno=Player("Bruno")
        marie=Player("Marie")
        loic.linkTo(lucie)
        lucie.linkTo(loic)

        bruno.linkTo(marie)
        marie.linkTo(bruno)
        
        peoples=[loic,lucie,bruno,marie]

        secretSanta= SecretSanta(peoples);
        secretSanta.start();

        self.assertIsNotNone(loic.get_gift_to_offer())
        self.assertIsNotNone(lucie.get_gift_to_offer())
        self.assertIsNotNone(bruno.get_gift_to_offer())
        self.assertIsNotNone(marie.get_gift_to_offer())
    
    def test_each_person_receive_one_gift_with_two_couple_and_one_single(self):
        loic=Player("Loic")
        lucie=Player("Lucie")
        bruno=Player("Bruno")
        marie=Player("Marie")
        bob=Player("Bob")

        loic.linkTo(lucie)
        lucie.linkTo(loic)

        bruno.linkTo(marie)
        marie.linkTo(bruno)
        
        peoples=[loic,lucie,bruno,marie,bob]

        secretSanta= SecretSanta(peoples);
        secretSanta.start();

        self.assertIsNotNone(loic.get_gift_to_offer())
        self.assertIsNotNone(lucie.get_gift_to_offer())
        self.assertIsNotNone(bruno.get_gift_to_offer())
        self.assertIsNotNone(marie.get_gift_to_offer())
        self.assertIsNotNone(bob.get_gift_to_offer())

    def test_each_person_receive_one_gift(self):
        loic=Player("Loic")
        lucie=Player("Lucie")
        paul=Player("Paul")
        bruno=Player("Bruno")
        marie=Player("Marie")
        vincent=Player("Vincent")
        tom=Player("Tom")

        loic.linkTo(lucie)
        lucie.linkTo(loic)

        bruno.linkTo(marie)
        marie.linkTo(bruno)
        
        peoples=[loic,lucie,paul,bruno,marie,vincent,tom]

        secretSanta= SecretSanta(peoples);
        secretSanta.start();


        self.assertIsNotNone(loic.get_gift_to_offer())
        self.assertIsNotNone(paul.get_gift_to_offer())
        self.assertIsNotNone(lucie.get_gift_to_offer())
        self.assertIsNotNone(bruno.get_gift_to_offer())
        self.assertIsNotNone(marie.get_gift_to_offer())
        self.assertIsNotNone(vincent.get_gift_to_offer())
        self.assertIsNotNone(tom.get_gift_to_offer())

    def test_each_person_receive_one_gift_2(self):
        loic=Player("Loic")
        lucie=Player("Lucie")
        paul=Player("Paul")
      
       

        loic.linkTo(lucie)
        lucie.linkTo(loic)

       
        
        peoples=[loic,lucie,paul]

        secretSanta= SecretSanta(peoples);
        secretSanta.start();


        self.assertIsNone(loic.get_gift_to_offer())
        self.assertIsNone(paul.get_gift_to_offer())
        self.assertIsNone(lucie.get_gift_to_offer())
      
    

if __name__ == '__main__':
    unittest.main()