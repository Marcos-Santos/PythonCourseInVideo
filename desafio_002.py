# Script File, from the Solution to Challenge 002.
# Arquivo de Script da Solucao do Desafio 002.
# Author Marcos Alexandre

'''################ Challenge 002 ####################
>>> Create a Python script that reads the day, month and year of a person's birth and displays 
a message with the formatted date.
>>> Crie um script Python que leia o dia , o mes e o ano de nascimento de uma pessoa e 
mostre uma mesnsagem com a data formatada.'''

#Program 
print('Desafio 002')

# Imports
import os as linux

# Starts variables bolean
checkValidDay = False
checkValidMonth = False
checkValidYear = False

# Initialize variables for months control
englishDate = 0
portugueseDate = 1

# List of Months in  English and Portuguese 
months = [['January','Janeiro'],['February','Fevereiro'],['March','Março'],
          ['April','Abril'],['May','Maio'],['June','Junho'],
          ['July','Junho'],['August','Agosto'],['Spetember','Setembro'],
          ['October','Outubro'],['November','Novembro'],['December','Dezembro']]

# Input data day
while(checkValidDay == False):
    day = int(input('Por favor digite o dia: '))
    if day in range(1,31+1):
        checkValidDay = True
    else:
        print('Por valor digite um valor entre 1 e 31')
    

# Input data month
while(checkValidMonth == False):
    month = int(input('Por favor digite o mes: '))
    if month in range(1,12+1):
        checkValidMonth = True
    else:
        print('Por valor digite um valor entre 1 e 12')


# Input data year
while(checkValidYear == False):
    year= int(input('Por favor digite o mes: '))
    if year in range(1000,9999+1):
        checkValidYear = True
        linux.system('clear')
    else:
        print('Por valor digite um valor entre 1000 e 9999')

# Final Results
print('>>> A data digitada foi {}/{}/{}.'.format(day,month,year))
print('>>> Resultado padrão Brasileiro:')
print('>>> A data digitada é {} de {} de {}.'.format(day, months[month-1][portugueseDate],year))
print('>>> Resultado padrão americano:')
print('>>> The Date inputed is {} {}th, {}.'.format(months[month-1][englishDate],day,year))
#End Code
