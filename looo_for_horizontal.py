str_1='' 
for i in range(10): 
    str_1 += str(i)+" " 
print(str_1) 

print(' '.join([str(i) for i in range(10)]))