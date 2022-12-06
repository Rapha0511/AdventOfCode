# [W] [V]     [P]                    
# [B] [T]     [C] [B]     [G]        
# [G] [S]     [V] [H] [N] [T]        
# [Z] [B] [W] [J] [D] [M] [S]        
# [R] [C] [N] [N] [F] [W] [C]     [W]
# [D] [F] [S] [M] [L] [T] [L] [Z] [Z]
# [C] [W] [B] [G] [S] [V] [F] [D] [N]
# [V] [G] [C] [Q] [T] [J] [P] [B] [M]
#  1   2   3   4   5   6   7   8   9 


array = [ 
    ["W","B","G","Z","R","D","C","V"],
    ["V","T","S","B","C","F","W","G"],
    ["W","N","S","B","C"],
    ["P","C","V","J","N","M","G","Q"],
    ["B","H","D","F","L","S","T"],
    ["N","M","W","T","V","J"],
    ["G","T","S","C","L","F","P"],
    ["Z","D","B"],
    ["W","Z","N","M"]
    ]


file = open('data.txt','r')
lines = file.readlines()

for line in lines:
    line = line.strip().replace("move","").replace("from",",").replace('to',',') #on remplace les trucs qui servent a rien part de ','
    move, From , to = map(int, line.split(",")) # 1 element = move , 2m From, 3m to
    trucAjouter = array[From - 1][:move] # on recupere la patie du tableau a ajouter , ici les 3 premiers elements du  tableau qui nous interesse 
    #trucAjouter.reverse() # on le reverse pour simuler un ajout d'element 1 par 1
    array[to - 1] = trucAjouter + array[to - 1] # on ajoute a la les trucaajouter au début du tableau destinataire
    del array[From - 1][0:move] # et on supprime les trucaajouter du tableau emetteur

result = ""

for i in range(len(array)):
    result += array[i][0] #recupération de la premiere lettre de chaque ligne
print(result)
