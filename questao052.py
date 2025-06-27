matriz=[[1,2,3],[4,5,6],[7,8,9]]
principal=secundaria=0
for i in range(3):
    for k in range(3):
        if i==k:
            principal=principal+matriz[i][k]
        if i+k==2:
            secundaria=secundaria+matriz[i][k]
print(principal)
print(secundaria)