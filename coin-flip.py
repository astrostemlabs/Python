import random

countof_T = 0
countof_H = 0
change = 0
sequenceof_T = 0
sequenceof_H = 0
max_sequenceof_T = 0
max_sequenceof_H = 0
seq=""

for a in range(10):
    x = random.choice("HT")
    print(x)
    seq +=x
    if a == 0:
        y = x
    if x == "H":
        countof_H += 1
          
    if x == "T":
        countof_T += 1
    if y != x:
        y = x
        change += 1

print("Heads came up",countof_H,"times.")
print("Tails came up",countof_T,"times.")
print("There were",change,"changes that occured.")
 
print(seq)
l=len(seq)
#----------------- Find sequence of 'H'------------------------------------
for i in range(0,l-1):
    if seq[i] =='H' :
        if sequenceof_H == 0:
            sequenceof_H =1
        if seq[i]==seq[i+1] :
            sequenceof_H +=1
            if sequenceof_H > max_sequenceof_H:
                max_sequenceof_H = sequenceof_H
        else: 
            if sequenceof_H > max_sequenceof_H:
                max_sequenceof_H = sequenceof_H
            sequenceof_H =1    
if seq[l-1] =='H' :
    if seq[l-2] =='T' :
       sequenceof_H =1

if sequenceof_H> max_sequenceof_H:
   max_sequenceof_H = sequenceof_H
   
#----------------- Find sequence of 'T'------------------------------------
for i in range(0,l-1):
    if seq[i] =='T' :
        if sequenceof_T == 0:
            sequenceof_T =1
        if seq[i]==seq[i+1] :
            sequenceof_T +=1
            if sequenceof_T > max_sequenceof_T:
                max_sequenceof_T = sequenceof_T
        else: 
            if sequenceof_T > max_sequenceof_T:
                max_sequenceof_T = sequenceof_T
            sequenceof_T =1    
if seq[l-1] =='T' :
    if seq[l-2] =='H' :
       sequenceof_T =1

if sequenceof_T> max_sequenceof_T:
   max_sequenceof_T = sequenceof_T
   
          
print('max_sequenceof_H',max_sequenceof_H)
            
print('max_sequenceof_T',max_sequenceof_T)

if max_sequenceof_H > max_sequenceof_T :
    print( "Number of consecutive Head is higher than that of Tail")
if max_sequenceof_T > max_sequenceof_H :
    print( "Number of consecutive Tail is higher than that of Head")
if max_sequenceof_T == max_sequenceof_H :
    print( "Number of consecutive Tail is same as that of Head")   
