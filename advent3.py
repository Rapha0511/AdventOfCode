lowerCaseLetter = "abcdefghijklmnopqrstuvwxyz"
upperCaseLetter = lowerCaseLetter.upper(); 

letterValue = {}

for i in range(len(lowerCaseLetter)): #Rajout lettre + valeur dans l'objet,
    letterValue[lowerCaseLetter[i]] = i + 1
    letterValue[upperCaseLetter[i]] = i + 27



# u = []
# for line in lines:
#     line = line.rstrip()
#     str1 = line[0:(len(line) // 2)]   #premiere partie de la chaine
#     str2 = line[(len(line) // 2): len(line)] #2m partie de la chaine
#     for i in range(len(str1)):
#         if str2.find(str1[i]) != -1: #si on trouve l'index de la lettre courante de str1 dans str2 on ajoute dans un tableau la valeur correspondante puis on fait la somme du tableau 
#             u.append(letterValue[str1[i]])
#             break

# print(sum(u))

#part2

def findCommunLetter(file):
    file = open(file,"r")
    lines = file.readlines()
    subList = [lines[n:n+3] for n in range(0, len(lines), 3)]
    a = list()  
    for i in range(len(subList)):
        a.extend(set(subList[i][0].rstrip())&set(subList[i][1].rstrip())&set(subList[i][2].rstrip()))
    return a

somme = 0 
enEsperantQueCeSoitBon = findCommunLetter('data.txt')
for i in range(len(enEsperantQueCeSoitBon)):
    somme += letterValue[enEsperantQueCeSoitBon[i]]

print(somme)