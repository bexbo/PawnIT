kommuner = open('all_kommuner.txt','r')

kommuner=kommuner.read()
kommuner = kommuner.split(',')
kommunDict ={}
for kommun in kommuner:

    numbers = kommun.split(':')
    
    kommunDict[numbers[0]] = numbers[1]

print(kommunDict['2480'])


