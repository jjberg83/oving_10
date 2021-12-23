#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 14:12:04 2021

@author: jjberg

Skriv en enhetstest for klassen Sporsmaal, som tester i alle fall metodene 
sjekk_svar og korrekt_svar_tekst
"""

import unittest
from quiz import MultipleChoice

class TestMultipleChoice(unittest.TestCase):
    
    def test_sjekk_svar(self):
        return True
        
    def test_korrekt_svar_tekst(self):
        return True
    
if __name__ == '__main__':
    unittest.main()