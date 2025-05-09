#               i     j
# 1             1     1
# 1 2           2     2
# 1 2 3         3     3
# 1 2 3 4       4     4 
# 1 2 3 4 5     5     5
# 1 2 3 4       6     4 
# 1 2 3         7     3
# 1 2           8     2 
# 1             9     1
rows=5
for i in range(1,2*rows):
    res=""
    col= i if  i<=rows else 2*rows-i
    for j in range(1,col+1):
        res+=str(j)+" "
    print(res)
  
                # i   sp    j 
#      1          1    4    1
#     1 2         2    3    2 
#    1 2 3        3    2    3  
#   1 2 3 4       4    1    4 
#  1 2 3 4 5      5    0    5
#   1 2 3 4       6    1    4
#    1 2 3        7    2    3
#     1 2         8    3    2
#      1          9    4    1

rows=5
for i in range(1,2*rows):
    res=""
    space=rows-i if i<=rows else i-rows
    col=i if i<=rows else 2*rows-i
    for sp in range(1,space+1):
        res+=" "
    for j in range(1,col+1):
        res+=str(j)+" "
    print(res)
        
# hour glass patttern   i   sp   j
# 1 2 3 4 5             1    0   5
#  1 2 3 4              2    1   4
#   1 2 3               3    2   3
#    1 2                4    3   2
#     1                 5    4   1
#    1 2                6    3   2
#   1 2 3               7    2   3 
#  1 2 3 4              8    1   4
# 1 2 3 4 5             9    0   5

rows=5
for i in range(1,2*rows):
    res=""
    space=i-1 if i<=rows else 2*rows-1-i
    col=rows-i+1 if i<=rows else i-rows+1
    for sp in range(1,space+1):
        res+=" "
    for j in range(1,col+1):
        res+=str(j)+" "
    print(res)

# hallow diamond shape
#     1
#    1 2
#   1   3
#  1     4
# 1       5
#  1     4
#   1   3 
#    1 2 
#     1

rows=5
for i in range(1,2*rows):
    res=""
    space=rows-i if i<=rows else i-rows
    col=i if i<=rows else 2*rows-i
    for sp in range(1,space+1):
        res+=" "
    for j in range(1,col+1):
        if j==1 or j==col:
         res+=str(j)+" "
        else:
           res+=" "+ " "
    print(res)
        

# 1 2 3 4 5             1    0   5
#  1     4              2    1   4
#   1   3               3    2   3
#    1 2                4    3   2
#     1                 5    4   1
#    1 2                6    3   2
#   1   3               7    2   3 
#  1     4              8    1   4
# 1 2 3 4 5             9    0   5

rows=5
for i in range(1,2*rows):
    res=""
    space=i-1 if i<=rows else 2*rows-1-i
    col=rows-i+1 if i<=rows else i-rows+1
    for sp in range(1,space+1):
        res+=" "
    for j in range(1,col+1):
        if j==1 or j==col or i==1 or i==2*rows-1:
            res+=str(j)+" "
        else:
            res+=" "+" " 
    print(res)
