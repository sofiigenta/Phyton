n1 = int (input ('Ingrese N1 '))
n2 = int (input ('Ingrese N2 '))
n3 = int (input ('Ingrese N3 '))

if (n1 < n2) and (n1 < n3):
    if (n2 < n3):
        print (n1,n2,n3)
    else: 
        print (n1,n3,n2)
elif (n2 < n1) and (n2 < n3):
    if (n1 < n3 ):
        print (n2,n1,n3)
    else:
        print (n2,n3,n1)
else:
    if (n1 < n2):
        print (n3, n1, n2)
    else:
        print (n3,n2,n1)


