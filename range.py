#The range function generates a sequence of Integers
a_range =range(5)
print('a_range->',a_range)
print('list(a_range) ->',list(a_range))
#It is often used to execute a "for"loop a numberof times
for i in range(5):
    print(i,end=' ') # executed five times
    print()
# It is similar to the slice function with a start,stop and step
a_range = range(10)# stop only
print('list(a_range) ->',list(a_range))
a_range= range(10,16)# start and stop
print('list(a_range) ->',list(a_range))
a_range=range(10,-1,-1) # start , stop and step
print('list(a_range)->',list(a_range))

k1=range(5)
print('k1->',list(k1))
k2=range(10,16)
print('k2->',list(k2))
k3=range(10,22,2)
print('k4->',list(k3))
k4=range(100,1,-25)
print('k4->',list(k4))
x=float.fromhex('A')
print(x)
