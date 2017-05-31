import sys
odds = []
evens=[]
while sys.stdin.readline():
    input = sys.stdin.readline()
    input.strip()
    for i in range(0,len(input)):
        if i%2 == 0:
            evens.append(input[i])
        else:
            odds.append(input[i])
    evens.append(' ')
    evens+=odds
    #strOdd = ''.join(odds) 
    strEven= ''.join(evens)
    sys.stdout.write(strEven)
    #sys.stdout.write(strOdd)
    odds = []
    evens=[]

