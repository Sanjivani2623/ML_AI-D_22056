# AIE22056
#1. count the number of vowels and consonants
def vowel_const_count(sent):
    #Assuming sentences are also allowed
    vowel=['a','e','i','o','u']
    slen=len(sent)
    vowel_count=0
    const_count=0
    for i in range(0,slen):
        if sent[i] in vowel:
            vowel_count+=1
        elif sent[i]>'a' or sent[i]<='z':
            const_count+=1
        else:
            pass
    
    return vowel_count,const_count

#2. product of matrix A and B
def matrixMulp(A, B, nA, nB, mA, mB):
    if mA != nB:
        return "Matrices are not multiplicable"

    result = [[0 for _ in range(mB)] for _ in range(nA)]
    for i in range(nA):
        for j in range(mB):
            for k in range(nB):
                result[i][j] += A[i][k] * B[k][j]
    return result

#3. the number of common elements between two lists
def commonCount(list1,list2):
    #repetition are not considered here
    #therefore converting into set
    set1=set(list1)
    set2=set(list2)
    common=0
    for i in set1:
        if i in set2:
            common+=1
    return common

#4. Transpose of matrix
def MatrixTransp(matrix,n,m):
    transpose = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            transpose[i][j]=matrix[j][i]
    return transpose
    

#1. Input
sentence=input("Enter a String: ")
vowel,constant=vowel_const_count(sentence)
print("Vowel Count: ",vowel)
print("Constant Count: ",constant)

#2. Input
nA = int(input("Number of rows in matrix A: "))
mA = int(input("Number of column in matrix A: "))
nB = int(input("Number of rows in matrix B: "))
mB = int(input("Number of column in matrix B: "))

matA = []
matB = []
print("Matrix A:")
for i in range(nA):
    rowA = []
    for j in range(mA):
        ele = int(input("Enter the element: "))
        rowA.append(ele)
    matA.append(rowA)
print("Matrix B:")
for i in range(nB):
    rowB = []
    for j in range(mB):
        ele = int(input("Enter the element: "))
        rowB.append(ele)
    matB.append(rowB)

product_AB = matrixMulp(matA, matB, nA, nB, mA, mB)
print("Product of A and B:")
for row in product_AB:
    print(row)

#3. Input
print("Enter the list of numbers separated by space")
list1inp=input("Enter first list: ")
list2inp=input("Enter second list: ")

#Converting into integer
list1 = list(map(int, list1inp.split()))
list2 = list(map(int, list2inp.split()))

common=commonCount(list1,list2)
print("Number of common elements: ",common)

#4. Input
n=int(input("Number of rows in matrix A: "))
m=int(input("Number of column in matrix A: "))
matrix=[]
print("Matrix A(nxm):")
for i in range(n):
    row=[]
    for j in range(m):
        ele=int(input("Enter the element: "))
        row.append(ele)
    matrix.append(row)

print("Matrix A(nxm):")
for row in matrix:
    print(row)

Transpose=MatrixTransp(matrix,n,m)
print("Transpose of A(mxn):")
for row in Transpose:
    print(row)