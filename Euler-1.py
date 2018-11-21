'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.*/'''
'''
a=0
for x in range(0,1000):
	
	if (x%3)==0:
		a=a+x
print(a)		
			
for x in range(0,1000):
	if (x%5)==0:
		a=a+x 
print(a)	
		
for x in range(0,1000):
	
	if (x%15)==0:
		a=a-x 		
		
print(a)
'''

n = 0
for i in range(1,10):
	if not i % 5 or not i % 3:
		print (i)
		n = n + i
      
print(n)
