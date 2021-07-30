# simple method
pos =-1    # using global variable 
def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
           globals() ['pos']=i
           return  True
        i=i+1
        
    return False
list=[2,4,5,7,8,9]
print(list)
n=int(input('Enter any number to find in  list:'))

if search(list,n):
    print('found at',pos+1)
else:
    print('not found')