#!/usr/bin/python3.6

import argparse
import csv
import pandas as pd

def reader():
  with open('test.csv',newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

def delete():
    with open('list.csv', 'w') as f:
        fichierCSV.write('Nos valeurs\n')

def max_val():
    maxval = pd.read_csv('list.csv')
    p = maxval['Valeurs'].max()
    print('\nLa valeur maximum de la liste est de : '.format(p))

def min_val():
    minval = pd.read_csv('list.csv')
    p = minval['Valeurs'].min()
    print('\nLa valeur maximum de la liste est de : '.format(p))

def average():
    avrg=pd.read_csv('list.csv')
    p = avrg['Valeurs'].mean()
    print('\nLa moyenne de la liste est de : '.format(p))

def sum():
    summ = pd.read_csv('list.csv')
    p = summ['Valeurs'].sum()
    print('\nLa somme de la liste est de : '.format(p))


def writer():
  with open('test.csv', 'a') as f:
      for number in argument:
          f.write(number)
          write.writerow(argument)




parser = argparse.ArgumentParser()
parser.add_argument("-l", help="Afficher le contenu de la liste",action='store_true')
parser.add_argument("-a", nargs='+', help="Ajoute les ITEMs dans la liste\n Exemple: ./NOM_Prenom_kholle_1.py -a [ITEM1, ITEM2, ...]")
parser.add_argument("-c", help="Supprime tous les éléments de la liste",action='store_true')
parser.add_argument("--max", help="Affiche la valeur maximum contenu dans la liste.",action='store_true')
parser.add_argument("--min", help="Affiche la valeur minimum contenu dans la liste.",action='store_true')
parser.add_argument("--moy", help="Affiche la moyenne de tous les éléments dans la liste.",action='store_true')
parser.add_argument("--sum", help="Affiche la somme de tous les éléments dans la liste.",action='store_true')
parser.add_argument("-t", help="Trie la liste dans l’ordre croissant",action='store_true')
parser.add_argument("--desc", help="Trie la liste dans l’ordre décroissant",action='store_true')




argument=parser.parse_args()

if argument=="-l":
   reader()
elif argument=="-c":
   delete()
elif argument=="-a":
  writer(argument)
elif argument=="-t":
  print()
elif argument== "--max":
  max_val()
elif argument == "--min":
  min_val()
elif argument == "--moy":
  average()
elif argument == "--sum":
  sum()
elif argument == "--desc":
  print()
else:
    print('Erreur dans la commande :)')