# #opponent

#  A = rock = 1
#  B = paper = 2
#  C = scissors = 3

#you
# X = rock = 1
# Y = paper = 2
# Z = scissors = 3

#victoire = value + 6
#combinaison
#AY = rock - paper =  win =  2  + 6 = 8
#BZ = paper - scissors = win = 3 + 6 = 9
#CX = scissors - rock = win = 1 + 6 = 7

#AX = draw = 1 + 3 = 4
#BY = draw = 2 + 3 = 5 
#CZ = draw = 3 + 3  = 6

#BX = loose = 1 + 0 = 1
#AZ = loose = 3 + 0 = 3
#CY = loose = 2 + 0 = 2

possibility = { #object of all possibilities
    "A Y" : 8,
    "B Z" : 9,
    "C X" : 7,
    "A X" : 4,
    "B Y" : 5,
    "C Z" : 6,
    "B X" : 1,
    "A Z" : 3,
    "C Y" : 2
}
data = open("data2.txt","r"); # open file with all inpute , read mode
lines = data.readlines() # read line by line all the inpute
#part 1 
# somme = 0; 
# for line in lines: #loop through each line
#     somme += possibility[line.rstrip()] #rstrip to remove /n from inpute

# print(somme)



#part2
# X = loose Y = draw Z = win
# if X , take the value of  the loosing combo whith the associate letter 
#  same for Y(draw) and Z(win) 
choices = { # object of all possibilities 
    "A X" : possibility["A Z"],
    "B X" : possibility["B X"],
    "C X" : possibility["C Y"],
    "A Y" : possibility["A X"],
    "B Y" : possibility["B Y"],
    "C Y" : possibility["C Z"],
    "A Z" : possibility["A Y"],
    "B Z" : possibility["B Z"],
    "C Z" : possibility["C X"]
}

somme = 0
for line in lines:
   line = line.rstrip()
   somme += choices[line]
print(somme)

