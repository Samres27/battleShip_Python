# the tables is a 10 x 10
# the values for the table is 0--> empty
# 1--> busy
# 2--> red
# 3--> white
from termcolor import colored
import os
table=[]
for x in range(11):
    tabC=[]
    for y in range(11):
        character=0
        if x==0 or y==0:
            if x==0 and y==0:
                character="   "
            else:    
                if y==0:
                    character=" "+chr(47+x)+" "
                else:
                    character=" "+chr(64+y)+" "
        
        tabC.append(character)
    table.append(tabC)

carrier=5
battleShip=4
cruiser=3
submarine=3
destroyer=2

block='[X]'
os.system('color')
def printTable():
    
    for x in table:
        for y in x:
            figure=block
            match y:
                case 0: figure=colored(figure,"white") 
                case 1: figure=colored(figure,"blue")
                case 2: figure=colored(figure,"red")
                case 3: figure=colored(figure,"black")
                case _: figure=colored(y,"white")
            print(figure,end=" ")
        print("\n")           

wrongMesageCoor=colored("wrong coordinates","red")
wrongMesageOut=colored("the coordinate goes out of range","red")
wrongMesageColli=colored("the ship collides with another ship","red")

corretMesageSucc=colored("Success","green")