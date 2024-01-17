'''
1    **
2   ****
3  ******
4 ***  ***
5***    ***
6 ***  ***
7  ******
8   ****
9    **
'''

import math

n = 8
pattern = '*'
space = ' '
k = 16

for i in range(1, n*2):

    if i <= math.ceil(n/2):
        print(f'{(n-i) * space}{pattern*2*i}')
        
    elif i <= n:
        print(f'{int((k-i*2)/2) * space}{pattern * 3}{(k-6-int((k-i*2)/2)*2) * space}{pattern * 3}{int((k-i*2)/2) * space}')
        
    elif i <= n+2:
        print(f'{int((k-(n*2-i)*2)/2) * space}{pattern * 3}{(k-6-int((k-(n*2-i)*2)/2)*2) * space}{pattern * 3}{int((k-(n*2-i)*2)/2) * space}')

    else:
        print(f'{(i-n) * space}{pattern*2*(n*2-i)}')

    
