# Driven code
# step 1 importing the .txt values into python and storing in the list 
def read_text():
    with open("/home/kurinchiban/Python Programs/sudoku_Validator/Sudoku_Sample_Input.txt")as input_values:
        numbers=[]
        list_int=[]
        for line in input_values:
            row=line.rstrip("\n")
            numbers=row.split(",")
            # converting the string values into integer file 
            for i in numbers:
                i=int(i)
                list_int.append(i)
    return list_int
# step 2 convering the list values into matrix
def to_matrix(l,n):
    matrix = []
    for i in range (0, len(l), n):
        matrix.append(l[i:i+n])
    return matrix
    """ Another method to convert list to matrix 
    matrix=[]
    a=0
    flag=0
    n=9
    for i in range(0,len(list_1)//n):
        b=((i+1)*n)
        matrix.append(list_1[a:b])
        a=b
    return matrix"""
# step 3 validating the matrix that passes the suduku test case
def check_Valid_Sudoku(Suduku_board):
    N=9
    list_2 = [False] * (N+1)
    # check 1 checking the each row wheter the duplicate values present in the row
    for i in range(0,N):
        for m in range(0,N+1):
            list_2[m]=False
        for j in range(0,N):
            z=Suduku_board[i][j]
            if (list_2[z]==True):
                return False
            list_2[z]=True
    # check 2 checking the each column wheter the duplicate values present in the row
    for i in range(0,N):
        for m in range(0,N+1):
            list_2[m]=False
        for j in range(0,N):
            z=Suduku_board[j][i]
            if (list_2[z]==True):
                return False
            list_2[z]=True 
    # check 3 checking the each column and column wheter the duplicate values present in the given square (values)      
    for i in range(0, N , 3):
        for j in range(0, N , 3):
            for m in range(0, N+1):
                list_2[m] = False
            for k in range(0, 3):
                for l in range(0, 3):
                    X = i + k
                    Y = j + l
                    Z = Suduku_board[X][Y]
                    if (list_2[Z] == True):
                        return False
                    list_2[Z] = True
    # return true if the all the test case is pass
    return True 
# driver code
list_1=read_text()
Suduku_board=to_matrix(list_1,9)
if (check_Valid_Sudoku(Suduku_board)):
    print("The Sudoku board is having the Valid values")
else:
    print("The Sudoku board is not having the Valid values Try different values")