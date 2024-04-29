import table
import os
import connection
from connection import MySocket

os.system('color')
positionMap=[]
def controlTable(figureLength,dic,x,y):
    message="success"
    tableA=table.table1
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
        table.table1=tableA 
        message=table.corretMesageSucc
        
    print(message)
    return (flag,message)

def hit_count():
    tableC=table.table1
    count=0
    for x in tableC:
        for y in x:
            if y == 2:
                count+=1
    
    return count



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
        try:
            x=ord(position[0])-64
            y=ord(position[1])-47
        except:
            pass
        
        if len(position)!=2 or x<0 or y<0 or x>11 or y>11:
            message=table.wrongMesageCoor
        else:
            flag,message=controlTable(dic=direction,x=x,y=y,figureLength=length_ship)        
        
        if flag:
            print(message)
        
        table.printTable(table.table1)


print("Hello, this is the board")
table.printTable(table.table1)
position_ship(length_ship=table.carrier,name_ship="Carrier")
position_ship(length_ship=table.battleShip,name_ship="battle Ship")
position_ship(length_ship=table.cruiser,name_ship="Cruiser")
position_ship(length_ship=table.submarine,name_ship="Submarine")
position_ship(length_ship=table.destroyer,name_ship="Destroyer")

ipOUT=input("Connect to server ip : ")
ipIN=connection.getIpPublic()
ipIN=input("You ip address is :" )
s=MySocket(ipIN,ipOUT)
print(table.correConection)
ST=""
while not(ST=='Y' or ST=='N'):
    ST=input("you are the one who will start (Y/N)")

ST=ST=='Y'
        
while hit_count()<17:
    os.system("cls")
    table.printTable(table.table2)
    print("\nYour board\n")
    table.printTable(table.table1)
    if ST:
        Cod=""
        while len(Cod)!=2:
            Cod=input("put the coordinate for your missile. Format A0 : ")
            try:
                x=ord(Cod[0])-64
                y=ord(Cod[1])-47
            except:
                pass
            if len(Cod)!=2 or x<0 or y<0 or x>11 or y>11:
                print(table.wrongMesageCoor)
            else:
                s.send(Cod.encode())
                value=s.receive().decode()
                table.table2[y][x]=int(value)
    else:
        cors=s.receive().decode()
        x=ord(cors[0])-64
        y=ord(cors[1])-47
        if table.table1[y][x]==1:
            table.table1[y][x]=2
            s.send("2".encode())
        else :
            s.send("3".encode())
    ST=not(ST)

