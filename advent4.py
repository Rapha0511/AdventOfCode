file = open("data.txt")
lines = file.readlines()
#a = []
q = 0
for line in lines:
    #part 1
    #line = line.rstrip().replace("-",",").split(",")
    # if int(line[0]) >= int(line[2]) and int(line[1]) <= int(line[3]) or int(line[0]) <= int(line[2]) and int(line[1]) >= int(line[3]) :
    #     a.append(line)

#print(len(a))
    #part2
    line = line.rstrip().replace("-",",").split(",")
    if not (int(line[1]) < int(line[2]) or int(line[0]) > int(line[3])): #inverse de ce qui ne se superpose pas , donc ce qui se superpose
        q+=1

print(q)