print ('                       THE SQUARE MATRIX CALCULATOR     '                 )
print('************************************************************************')
while True:
    print('OPERATION MENU \n 1. Addition \n 2. Subtraction \n 3. Multiplicaion \n 4. Exit')
    option=int(input('enter option number')) 
    if option>=4:
        print('thank you for using matrix calculator')
        break
    else:
        dimensions=int(input('enter number of rows/columns for the square matrix:')) 
        print()
        print('MATRIX NO.1')
        print()
        mat1=[]
        for i in range (1,dimensions+1):
            print('enter values for matrix 1 and row',i,'seperated by commas:',end=' ')
            a=input()
            a1=a.split(',')
            mat1.append(a1)
        print()
        for i in range(len(mat1)):
            for j in range(len(mat1)):
                print(mat1[i][j],end='    ')
            print()   
        print() 
        print('MATRIX NO.2')    
        print()
        mat2=[]
        for f in range (1,dimensions+1):
            print('enter values for matrix 2 and row',f,'seperated by commas:',end=' ')
            b=input()
            b1=b.split(',')
            mat2.append(b1)
        print()  
        for i in range(len(mat2)):
            for j in range(len(mat2)):
                print(mat2[i][j],end='    ')
            print()    
        if option==1:
           resultant_mat=[[float(mat1[m][k])+float(mat2[m][k])for m in range(len(mat1))]for k in range(len(mat2))]
        if option==2:
            resultant_mat=[[float(mat1[m][k])-float(mat2[m][k])for m in range(len(mat1))]for k in range(len(mat2))]
        if option==3:
            resultant_mat=[[0 for h in range(len(mat1))]for k in range(len(mat2))]
            for i in range(len(mat1)):
                for j in range(len(mat2[0])):
                    for k in range (len(mat2)):
                        resultant_mat[i][j]+=float(mat1[i][k])*float(mat2[k][j])
    print()
    print('RESULTANT MATRIX')        
    print()
    for i in range(len(resultant_mat)):
        for j in range(len(resultant_mat)):
            print(round(resultant_mat[j][i],2),end='    ')
        print()    
                    
                    
        
        
        

