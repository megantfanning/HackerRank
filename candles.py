#Megan Fanning
#7/26/2016
#candle problem for hacker rank
import sys

age = input()
heights = input()
heights = heights.split(" ");
heights = map(int, heights)

tallestCandle=1
candlesBlown=0
for i in heights:    
    if i==tallestCandle:
        candlesBlown+=1
    elif i > tallestCandle:
        tallestCandle=i
        candlesBlown=1
print(candlesBlown)
