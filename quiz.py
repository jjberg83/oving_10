#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 03:58:13 2021

@author: jjberg_



"""

def read_the_document():
    question_list = list()
    with open('sporsmaalsfil.txt', 'r', encoding='UTF8') as fila:
        for linje in fila:
            linje_liste = linje.replace(':', ',').strip('\n').split(',')
            sporsmaal = linje_liste.pop(0)
            rett_svar = int(linje_liste.pop(0))
            alternativer = [x.strip(' []') for x in linje_liste]
            ny_instans = MultipleChoice(sporsmaal, rett_svar, alternativer)
            question_list.append(ny_instans)
    return question_list

class Spiller:
    def __init__(self, navn, poengsum = 0):
        self.navn = navn
        self.poengsum = poengsum

def players_list():
    players_list = list()
    number_players = int(input('Hvor mange spillere er dere?\n'))
    indeks = 1
    for spiller in range(number_players):
        name_player = input(f'Hva er navnet på spiller nummer {indeks}:\n')
        ny_instans = Spiller(name_player)
        players_list.append(ny_instans)
        indeks += 1
    return players_list

class MultipleChoice:
    #Constructor
    def __init__(self, question, correct_answer, alternatives):
        self.question = question
        self.correct_answer = correct_answer
        self.alternatives = alternatives
        
    
    def answer_check(self, entered_integer):
        if entered_integer == self.correct_answer+1:
            return True
        else:
            return False
        
    
    def korrekt_svar_tekst(self):
        return self.alternatives[self.correct_answer]
    
    
    def __str__(self):
        return f'{self.question}\n' + '\n'.join(f'{indeks} - {element}' for indeks, element in enumerate(self.alternatives,1))+ '\n'
    
'''

Her er et eksempel på spill, de to første spørsmålene:
    
Den delen av en datamaskin som kjører programmet kalles? 
Svaralternativer:
0: RAM
1: Harddisk
2: CPU
3: Sekundærlager

Velg et svaralternativ for spiller 1: 0
Velg et svaralternativ for spiller 2: 2

Korrekt svar: CPU

Spiller 1: Feil
Spiller 2: Korrekt

'''
    
       
    
if __name__ == '__main__':
    liste_med_alle_spillerne = players_list()
    liste_med_alle_sporsmaalene = read_the_document()
    poeng = [0] * (len(liste_med_alle_spillerne))
    for sporsmaal in liste_med_alle_sporsmaalene:
        avgitte_svar = list()
        print(f'\n{sporsmaal}')
        indre_indeks = 0
        for spillers_svar in liste_med_alle_spillerne:
            svar = int(input(f'Velg et svaralternativ for {spillers_svar.navn}: '))
            avgitte_svar.append(svar)
            if svar - 1 == sporsmaal.correct_answer:
                poeng[indre_indeks] += 1
            indre_indeks += 1
        print(f'\nKorrekt svar: {sporsmaal.korrekt_svar_tekst()}\n')
        for indeks in range(len(liste_med_alle_spillerne)):
            if avgitte_svar[indeks]-1 == sporsmaal.correct_answer:
                print(f'{liste_med_alle_spillerne[indeks].navn}: Korrekt')
            else:
                print(f'{liste_med_alle_spillerne[indeks].navn}: Feil')
    vinner_poeng = max(poeng)
    vinner_spiller = liste_med_alle_spillerne[poeng.index(vinner_poeng)].navn
    print(f'\n{vinner_spiller} vant med {vinner_poeng} poeng!')
    

        
        
            
            
            
            
            
            
            
            