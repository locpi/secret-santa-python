import unittest
from secretsanta.Gift import Gift
from secretsanta.Player import Player
from secretsanta.SecretSanta import SecretSanta

class SecretSantaTest(unittest.TestCase):


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