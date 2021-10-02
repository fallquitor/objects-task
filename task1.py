class football_player:
    total=1
    def __init__(self,name,pos):
        self.name=name
        self.pos=pos
football=[]
for i in [['Shevchenko',1],['Butko',2],['Krivcov',4],["Matvienko",22],['Ismaili',31],['Marlos',11],['Mikon',27],['Tison',7],['Moraes',10],['Fernando',99]]:
    football.append(football_player(i[0],i[1]))