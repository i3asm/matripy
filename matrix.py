from array import *

def chooseMat(text, mats):
    try: 
        num = int(input(text + "  "))
    except:
        print("Please enter an integer number")
        num = chooseMat(text, mats)
    num %= len(mats)
    return num

def drawMat(mat):
    if (len(mat)==0):
        return
    for i in range(len(mat[0])):
        print ("-----", end='')
    print()
    for row in mat:
        print ("|", end='')
        for elm in row:
            print(elm,"  ", end = '')
        print("|")
    print ("----------")

def showAllMats(mats):
    if (len(mats)==0):
        return
    for i in range(len(mats)):
        print(i+1, ')')
        drawMat(mats[i])
        print()

def initMat():
    matRows = int(input("Enter how many rows you want:  "))
    matCols = int(input("Enter how many columns you want:  "))
    mat = [[0 for x in range(matCols)] for y in range(matRows)]
    for i in range(matRows):
        for j in range(matCols):
            print ("at row ",i+1, " and column ",j+1,"  ")
            mat[i][j] = int(input())
    return mat

def addMats(mats):
    showAllMats(mats)
    mat1=chooseMat("which matrix do you want to add?", mats)-1
    mat2=int(input("to which matrix?"))-1
    if (len(mats[mat1]) == len(mats[mat2])):
        if (len(mats[mat1][0]) == len(mats[mat2][0])):
            rows, cols = len(mats[mat1]), len(mats[mat1][0])
            result=[[0 for x in range(rows)] for y in range(cols)]
            for i in range(rows):
                for j in range(cols):
                    sum=mats[mat1][i][j]+mats[mat2][i][j]
                    result[i][j]=sum
            drawMat(result)
            mats.append(result)
        else:
            print('\033[93m'+"\nsizes doesn't match"+'\033[0m')
    else:
        print('\033[93m'+"\nsizes doesn't match"+'\033[0m')

def multiplyMatByNumber(mats):
    showAllMats(mats)
    mat=chooseMat("which matrix do you want to mutiply?", mats)-1
    try:
        num=int(input("by what number? "))
    except:
        print("Please enter an integer number")
        multiplyMatByNumber(mats)
    result=[[0 for x in range(len(mats[mat][0]))] for y in range(len(mats[mat]))]
    
    for i in range(len(mats[mat])):
        for j in range(len(mats[mat][0])):
            result[i][j] = mats[mat][i][j] * num
    drawMat(result)
    mats.append(result)

    #mat=int(input("which matrix do you want to mutiply?  "))-1
def multiplyMats(mats):
    showAllMats(mats)
    mat1=chooseMat("which matrix do you want to mutiply?", mats)-1
    mat2=chooseMat("by which matrix ?", mats)-1
    if (len(mats[mat1][0]) != len(mats[mat2])):
        print("the number of columns in matrix 1 should be equal to the number of rows in matrix 2")
        return multiplyMats(mats)
    result=[[0 for x in range(len(mats[mat2][0]))] for y in range(len(mats[mat1]))]
    for i in range(len(result)):
        for j in range(len(result[0])):
                res = 0
                for k in range(len(mats[mat2])):
                    res += mats[mat1][i][k] * mats[mat2][k][j]
                result[i][j] = res
    drawMat(result)
    mats.append(result)

def transposeMat(mats):
    showAllMats(mats)
    mat=chooseMat("which matrix do you want to transpose", mats)-1
    result=[[0 for x in range(len(mats[mat]))] for y in range(len(mats[mat][0]))]
    for i in range(len(result)):
        for j in range(len(result[0])):
            result[i][j] = mats[mat][j][i]
    drawMat(result)
    mats.append(result)

def findDeterminant(mats):
    showAllMats(mats)
    mat=mats[chooseMat("which matrix do you want to get the determinant of?", mats)-1]
    if (len(mat) != len(mat[0])):
        print("choose a proper mat")
        findDeterminant(mats)
        return
    if (len(mat) == 1):
        print ("ARE YOU KIDDING ME!! 1x1 matrix?!")
        return
    if (len(mat) == 2):
        determinate2(mat)
    if (len(mat) == 3):
        determinate3(mat)
    if (len(mat) == 4):
        determinate4(mat)

def determinate2(mat):
    det = mat[0][0]*mat[1][1] - mat[1][0]*mat[0][1]
    return det

def determinate3(mat):
    # split the matrix to three 2x2 matricies and compine them
    mat0 = [[mat[1][1],mat[1][2]],[mat[2][1],mat[2][2]]]
    mat1 = [[mat[1][0],mat[1][2]],[mat[2][0],mat[2][2]]]
    mat2 = [[mat[1][0],mat[1][1]],[mat[2][0],mat[2][1]]]
    det = mat[0][0]*determinate2(mat0) - mat[0][1]*determinate2(mat1) + mat[0][2]*determinate2(mat2)

mats=[[[]]]
# try:
#     mats[0]=initMat()
#     drawMat(mats[0])
# except ValueError:
#     print("value error, retry again")
def main():
    try:
        control=0
        while (control != -1):
            print("\n***********************************")
            print("what operation do you want to do?")
            print("1) show all matrecies")
            print("2) add new matrix")
            print("3) sum two matrecies")
            print("4) multiply matrix by number")
            print("5) multiply two matrecies")
            print("6) trnspose a matrix")
            print("7) find the determinant of a matrix")
            print("-1) exit\n")
            control = int(input("your choice: "))
            print("***********************************\n")
            if (control==1):
                showAllMats(mats)
            if (control==2):
                mats.append(initMat())
            if (control==3):
                addMats(mats)
            if (control==4):
                multiplyMatByNumber(mats)
            if (control==5):
                multiplyMats(mats)
            if (control==6):
                transposeMat(mats)
            if (control==7):
                findDeterminant(mats)
    except ValueError:
        print("value error, try again")
        main()
    except:
        main()

main()
