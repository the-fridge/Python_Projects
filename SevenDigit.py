#Seven digit display
#Given an input i
#Return the number of segments required to display the number in a seven digit display

#@JeppeK2017

i = input()
sum = 0
for ch in i:
    a = int(ch)
    if(a == 0):
        sum += 6
    elif(a == 1):
        sum += 2
    elif(a == 2):
        sum += 5
    elif(a == 3):
        sum += 5
    elif(a == 4):
        sum += 4
    elif(a == 5):
        sum += 5
    elif(a == 6):
        sum += 6
    elif(a == 7):
        sum += 3
    elif(a == 8):
        sum += 7
    elif(a == 9):
        sum += 6
    
    
print(sum)



        
