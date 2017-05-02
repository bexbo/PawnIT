import shelve

textfile = open('SE.txt','r')

d = shelve.open('postnummerTokommun')

#line[1] is the postnumber and line[6] is the municipal code
for line in textfile:
    line=line.split('	')

    line[1]=line[1][:3]+line[1][4:]
    print(line[1])



    if line[6] != '':
        d[line[1]] = line[6]

    else:
        d[line[1]] = line[2]

