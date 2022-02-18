import unittest

from translator import englishToFrench,frenchToEnglish

class Testfr2eng(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') 
        self.assertNotEqual(frenchToEnglish('Bonjour'), 'potato') 

class Testeng2fr(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') 
        self.assertNotEqual(englishToFrench('Hello'), 'bonbon') 

unittest.main()
