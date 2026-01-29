matrix=[[1,2,3],[4,5,6],[7,8,9]]

rows=3
cols=3

print(" ")
print("Printing the Matrix...\n")
for i in range(3):
    for j in range(3):  
        print(matrix[i][j],end=" ")
    print("\n")

print(" ")

result=[[0]*rows for _ in range(3)]

for i in range(rows):
    for j in range(cols):
        result[j][i]=matrix[i][j]

print(" ")
print("Printing the Transposed Matrix...\n")
for i in range(3):
    for j in range(3):  
        print(result[i][j],end=" ")
    print("\n")
print(" ")