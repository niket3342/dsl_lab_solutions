



SE = ["Amar","Raju","Pawan","Prince","Aman","Vivek","Dinesh", "Rajesh"]

cricket = ["Aman","Amar","Prince","Dinesh"]

badminton = ["Prince","Vivek","Aman",]

football = ["Raju","Pawan","Aman","Prince"]



# list of students who play both cricket and badminton

def First():

  A = []

  for i in cricket:

    for j in badminton:

        if i == j:

            A.append(i)    

  print("List of students who play both cricket and badminton are:",A)



# list of students who play either cricket or badminton but not both

def Second():

  B = []

  for i in cricket:

    if i not in badminton:

      B.append(i)

  for j in badminton:

    if j not in cricket:

      B.append(j)     



  print("\nList of students who play either cricket or badminton but not both are:",B)



#  Number of students who play neither cricket nor badminton

def Third():

  C = []

  for i in SE:

    if i not in cricket and badminton:

      C.append(i)



  print("\nList of students who play neither cricket nor badminton are ",C)

  print("The number of students who play neither cricket nor badminton are ",len(C))



# Number of students who play cricket and football but not badminton

def Fourth():

  D = []

  for i in SE:

    if i not in badminton:

        D.append(i)

  print("\n List of students who play cricket and football but not badminton are:",D)

  print("Number of students who play cricket and football both but not badminton are",len(D))






flag=1
while flag==1:
    print("\n\n--------------------MENU--------------------\n")
    print("1. list of students who play both cricket and badminton")
    print("2.list of students who play either cricket or badminton but not both")
    print("3.Number of students who play neither cricket nor badminton  ")
    print("4.Number of students who play cricket and football but not badminton ")
    print("5. Exit\n")
    ch=int(input("Enter your Choice (from 1 to 5) :"))

    if ch==1:
        First()
        a = input("Do you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==2:
        Second()
        a = input("Do you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==3:
        Third()
        a = input("Do you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==4:
        Fourth()
        a = input("Do you want to continue (yes/no) :")
        if a == "yes":
            flag = 1
        else:
            flag = 0
            print("Thanks for using this program!")

    elif ch==5:
        flag=0
        print("Thanks for using this program!")

    else:
        print("!!Wrong Choice!! ")
        a=input("Do you want to continue (yes/no) :")
        if a=="yes":
            flag=1
        else:
            flag=0
            print("Thanks for using this program!")




