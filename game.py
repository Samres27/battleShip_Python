import table
import os
import connection
from connection import MySocket

os.system('color')
positionMap=[]
def controlTable(figureLength,dic,x,y):
    message="success"
    tableA=table.table
    for a in range(figureLength):
        valueShip=(y+a,x)
        if dic=='v':
            if y+figureLength>11:
                message=table.wrongMesageOut
                break
            else:
                valueShip=(y+a,x)
                if not(valueShip in positionMap):
                    tableA[y+a][x]=1
                else: 
                    message=table.wrongMesageColli
                    break
        else:
            if x+figureLength>11:
                message=table.wrongMesageOut
                break
            else:
                valueShip=(y,x+a)
                if not(valueShip in positionMap):
                    tableA[y][x+a]=1
                else: 
                    message=table.wrongMesageColli
                    break
        
        positionMap.append(valueShip)
    
    flag=message!="success"
    os.system("cls")
    if not(flag): 
        table.table=tableA 
        message=table.corretMesageSucc
        
    print(message)
    return (flag,message)


def position_ship(length_ship,name_ship):
    cross='''To position, follow the following form o--->
                                        |
                                        v'''
    print(cross)
    flag=True
    while flag:
        input("Let's start positioning the {name} of size {length}... press enter".format(length=length_ship,name=name_ship))
        direction='n'
        while not(direction=='c' or direction=='v'):
            direction=input("choose between vertical line(v) or cossbar(c): ")
        
        position=input("Select the coordinates of your ship. Format A1: ")
        message=""
        x=ord(position[0])-64
        y=ord(position[1])-47
        
        if len(position)!=2 or x<0 or y<0 or x>11 or y>11:
            message=table.wrongMesageCoor
        else:
            flag,message=controlTable(dic=direction,x=x,y=y,figureLength=length_ship)        
        
        if flag:
            print(message)
        
        table.printTable()


print("Hello, this is the board")
table.printTable()
position_ship(length_ship=table.carrier,name_ship="Carrier")
position_ship(length_ship=table.battleShip,name_ship="battle Ship")
position_ship(length_ship=table.cruiser,name_ship="Cruiser")
position_ship(length_ship=table.submarine,name_ship="Submarine")
position_ship(length_ship=table.destroyer,name_ship="Destroyer")

ipOUT=input("Connect to server ip is: ")
ipIN=connection.getIpPublic()
print("You ip address is :" + str(ipOUT))