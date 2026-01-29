# 3 x 3 MATRIX
matrix=[[1,2,3],[4,5,6],[7,8,9]]

print("Printing the Matrix...\n")
for i in range(3):
    for j in range(3):  
        print(matrix[i][j],end=" ")

print(" ")

rows=len(matrix)
print("No. of Rows in the Matrix are : ",rows)

print(" ")
cols=len(matrix[0])
print("No. of Columns in the Matrix are :",cols)

print(" ")
elements=cols*rows
print("No. of Elements in the Matrix are : ",elements)

print(" ")
cells=cols*rows
print("No. of Cells in the Matrix are : ",cells)
