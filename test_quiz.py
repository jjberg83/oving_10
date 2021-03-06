#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 14:12:04 2021

@author: jjberg

"""

import unittest
from quiz import *

class TestMultipleChoice(unittest.TestCase):
    
    def test_answer_check(self):
        liste_med_alle_instansene = read_the_document()

        # Question 1
        self.assertFalse(liste_med_alle_instansene[0].answer_check(1))
        self.assertFalse(liste_med_alle_instansene[0].answer_check(2))
        self.assertFalse(liste_med_alle_instansene[0].answer_check(4))
        self.assertTrue(liste_med_alle_instansene[0].answer_check(3))
        
        # Question 2
        self.assertFalse(liste_med_alle_instansene[1].answer_check(1))
        self.assertFalse(liste_med_alle_instansene[1].answer_check(3))
        self.assertFalse(liste_med_alle_instansene[1].answer_check(4))
        self.assertTrue(liste_med_alle_instansene[1].answer_check(2))
        
        # Question 3
        self.assertFalse(liste_med_alle_instansene[2].answer_check(2))
        self.assertFalse(liste_med_alle_instansene[2].answer_check(3))
        self.assertFalse(liste_med_alle_instansene[2].answer_check(4))
        self.assertTrue(liste_med_alle_instansene[2].answer_check(1))
        
        # Question 4
        self.assertFalse(liste_med_alle_instansene[3].answer_check(1))
        self.assertFalse(liste_med_alle_instansene[3].answer_check(2))
        self.assertFalse(liste_med_alle_instansene[3].answer_check(4))
        self.assertTrue(liste_med_alle_instansene[3].answer_check(3))
        
        # Question 5
        self.assertFalse(liste_med_alle_instansene[4].answer_check(1))
        self.assertFalse(liste_med_alle_instansene[4].answer_check(3))
        self.assertFalse(liste_med_alle_instansene[4].answer_check(4))
        self.assertTrue(liste_med_alle_instansene[4].answer_check(2))
        
        # Question 6
        self.assertFalse(liste_med_alle_instansene[5].answer_check(1))
        self.assertFalse(liste_med_alle_instansene[5].answer_check(3))
        self.assertFalse(liste_med_alle_instansene[5].answer_check(4))
        self.assertFalse(liste_med_alle_instansene[5].answer_check(5))
        self.assertTrue(liste_med_alle_instansene[5].answer_check(2))
        
        # Question 7
        self.assertFalse(liste_med_alle_instansene[6].answer_check(1))
        self.assertFalse(liste_med_alle_instansene[6].answer_check(2))
        self.assertFalse(liste_med_alle_instansene[6].answer_check(3))
        self.assertFalse(liste_med_alle_instansene[6].answer_check(5))
        self.assertTrue(liste_med_alle_instansene[6].answer_check(4))
        
        # Question 8
        self.assertFalse(liste_med_alle_instansene[7].answer_check(1))
        self.assertTrue(liste_med_alle_instansene[7].answer_check(2))
        
    def test_korrekt_svar_tekst(self):
        liste_med_alle_instansene = read_the_document()
        
        # Question 1
        self.assertFalse(liste_med_alle_instansene[0].korrekt_svar_tekst()=='RAM')
        self.assertFalse(liste_med_alle_instansene[0].korrekt_svar_tekst()=='Harddisk')
        self.assertFalse(liste_med_alle_instansene[0].korrekt_svar_tekst()=='Sekund??rlager')
        self.assertTrue(liste_med_alle_instansene[0].korrekt_svar_tekst()=='CPU')
        
        # Question 2
        self.assertFalse(liste_med_alle_instansene[1].korrekt_svar_tekst()=='bit')
        self.assertFalse(liste_med_alle_instansene[1].korrekt_svar_tekst()=='bryter')
        self.assertFalse(liste_med_alle_instansene[1].korrekt_svar_tekst()=='transistor')
        self.assertTrue(liste_med_alle_instansene[1].korrekt_svar_tekst()=='byte')
        
        # Question 3
        self.assertFalse(liste_med_alle_instansene[2].korrekt_svar_tekst()=='instruksjoner')
        self.assertFalse(liste_med_alle_instansene[2].korrekt_svar_tekst()=='variabler')
        self.assertFalse(liste_med_alle_instansene[2].korrekt_svar_tekst()=='CPU-er')
        self.assertTrue(liste_med_alle_instansene[2].korrekt_svar_tekst()=='bits')
        
        # Question 4 
        self.assertFalse(liste_med_alle_instansene[3].korrekt_svar_tekst()=='heksadesimal')
        self.assertFalse(liste_med_alle_instansene[3].korrekt_svar_tekst()=='oktal')
        self.assertFalse(liste_med_alle_instansene[3].korrekt_svar_tekst()=='desimal')
        self.assertTrue(liste_med_alle_instansene[3].korrekt_svar_tekst()=='bin??r')
                
        # Question 5 
        self.assertFalse(liste_med_alle_instansene[4].korrekt_svar_tekst()=='38')
        self.assertFalse(liste_med_alle_instansene[4].korrekt_svar_tekst()=='173')
        self.assertFalse(liste_med_alle_instansene[4].korrekt_svar_tekst()=='1011001')
        self.assertTrue(liste_med_alle_instansene[4].korrekt_svar_tekst()=='89')
        
        # Question 6 
        self.assertFalse(liste_med_alle_instansene[5].korrekt_svar_tekst()=='1011')
        self.assertFalse(liste_med_alle_instansene[5].korrekt_svar_tekst()=='11011')
        self.assertFalse(liste_med_alle_instansene[5].korrekt_svar_tekst()=='101111')
        self.assertFalse(liste_med_alle_instansene[5].korrekt_svar_tekst()=='111011')
        self.assertTrue(liste_med_alle_instansene[5].korrekt_svar_tekst()=='10111')
        
        # Question 7 
        self.assertFalse(liste_med_alle_instansene[6].korrekt_svar_tekst()=='assembly')
        self.assertFalse(liste_med_alle_instansene[6].korrekt_svar_tekst()=='c')
        self.assertFalse(liste_med_alle_instansene[6].korrekt_svar_tekst()=='java')
        self.assertFalse(liste_med_alle_instansene[6].korrekt_svar_tekst()=='python')
        self.assertTrue(liste_med_alle_instansene[6].korrekt_svar_tekst()=='maskinkode')
        
        # Question 8 
        self.assertFalse(liste_med_alle_instansene[7].korrekt_svar_tekst()=='kompilert')
        self.assertTrue(liste_med_alle_instansene[7].korrekt_svar_tekst()=='tolket')
    
if __name__ == '__main__':
    unittest.main()
    
# def read_the_document():
#     question_list = list()
#     with open('sporsmaalsfil.txt', 'r', encoding='UTF8') as fila:
#         for linje in fila:
#             linje_liste = linje.replace(':', ',').strip('\n').split(',')
#             sporsmaal = linje_liste.pop(0)
#             rett_svar = int(linje_liste.pop(0))
#             alternativer = [x.strip(' []') for x in linje_liste]
#             ny_instans = MultipleChoice(sporsmaal, rett_svar, alternativer)
#             question_list.append(ny_instans)
#     return question_list
            

# class MultipleChoice:
#     #Constructor
#     def __init__(self, question, correct_answer, alternatives):
#         self.question = question
#         self.correct_answer = correct_answer
#         self.alternatives = alternatives
        
    
#     def answer_check(self, entered_integer):
#         if entered_integer == self.correct_answer+1:
#             return True
#         else:
#             return False
        
    
#     def korrekt_svar_tekst(self):
#         return self.alternatives[self.correct_answer]
    
    
#     def __str__(self):
#         return f'{self.question}\n' + '\n'.join(f'{indeks} - {element}' for indeks, element in enumerate(self.alternatives,1))+ '\n'

# if __name__ == '__main__':
#     liste_med_alle_instansene = read_the_document() 
#     sum_spiller1 = 0
#     sum_spiller2 = 0
#     for sporsmaal in liste_med_alle_instansene:
#         print(sporsmaal)
#         svar_spiller1 = int(input("Velg et svaralternativ for spiller 1: "))
#         svar_spiller2 = int(input("Velg et svaralternativ for spiller 2: "))
#         print(f'Korrekt svar: {sporsmaal.korrekt_svar_tekst()}')
#         if sporsmaal.answer_check(svar_spiller1):
#             sum_spiller1 += 1
#             print('Spiller 1: Korrekt')
#         else:
#             print('Spiller 1: Feil')
#         if sporsmaal.answer_check(svar_spiller2):
#             sum_spiller2 += 1
#             print('Spiller 2: Korrekt')
#         else:
#             print('Spiller 2: Feil')
#     print(f'Sum spiller 1: {sum_spiller1}')
#     print(f'Sum spiller 2: {sum_spiller2}')
    