blocks = int(input("Enter the number of blocks: "))

#
print('hello')
# Write your code here.
height = 0
i=1
altura = 0
dec = blocks - i
while dec >= 0:
    altura += 1
    i += 1
    dec -= i
    
    
#	

print("The height of the pyramid:", altura)
