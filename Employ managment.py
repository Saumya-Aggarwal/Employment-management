import pickle
import time
import datetime
def Menu():
    print("*"*140)
    print("MAIN MENU".center(140))
    print(" "*45+"1. Insert Employee Records")
    print(" "*45+"2. Display Sorted Employee Records as per Emp no.")
    print(" "*45+"3. Display Sorted Employee Records as per Names")
    print(" "*45+"4. Display Sorted Employee Records as per Designation")
    print(" "*45+"5. Display Employee Records as the Designation")
    print(" "*45+"6. Delete Records")
    print(" "*45+"7. Update Records")
    print(" "*45+"8. Search Employee records Details as per the Employee number")
    print(" "*45+"9. Search Employee records Details as per the Employee name")
    print(" "*45+"10. Exit")
    
    print("*"*140)
def SortAcc(F): #arrange record in ascending order of employ no.
    try:
        with open(F,'rb+') as fil:
            rec=pickle.load(fil)
            rec.sort(key=lambda rec:rec["ID"])
            fil.seek(0)
            pickle.dump(rec,fil)
    except FileNotFoundError:
        print(F, "File has no records")
def SortName(F): #arrange record in ascending order of Name
    try:
        with open(F,'rb+') as fil:
            rec=pickle.load(fil)
            rec.sort(key=lambda rec:rec["NAME"])
            fil.seek(0)
            pickle.dump(rec,fil)
    except FileNotFoundError:
        print(F, "File has no records")
def SortDesig(F): #arrange record in ascending order of Designation
    try:
        with open(F,'rb+') as fil:
            rec=pickle.load(fil)
            rec.sort(key=lambda rec:rec["Desig"])
            fil.seek(0)
            pickle.dump(rec,fil)
    except FileNotFoundError:
        print(F, "File has no records")
def calcage(x):
    date = int(x[:1])
    month = int(x[3:5])
    year = int(x[6:])
    days = date + month * 31 + year * 365
    return days
def Insert(F):
    try:
        fil=open(F,'ab+')
        
        Des=["MGR","CLK","VP","PRES"]
        Dep=["HR", "IT", "SALES", "FIN"]
        
        if fil.tell()>0:
            fil.seek(0)
            Rec1=pickle.load(fil)
        else:
            Rec1=[]
        while True:             #loop for accepting records
            #allowing only unique ids 

            Name=input("Enter Employee Name :- ")
            while True:
                DOB = input("Enter DOB(DD/MM/YYYY) :- ")
                l=DOB
                l=l.replace("/","")
                if "/" not in DOB:
                    print("Please Enter DOB as per the Format")
                else:

                    from datetime import date
                    today = date.today()
                    d1 = today.strftime("%d/%m/%Y")
                    age = int(calcage(d1) - calcage(DOB))/365

                    if age < 18:
                        print("you can't be an employee with age less than 18")
                    else:
                        break


            #allowing only valid phone no.
            while True:
                Mob=input("Enter Mobile no. :- ")
                if len(Mob)!=10 or Mob.isdigit()==False:
                    print("PLEASE enter valid Mobile no.")
                else:
                    break
            #allowing only valid email ids
            while True:
                Email=input("Enter Email :- ")
                if '@' not in Email or '.' not in Email:
                    print("PLEASE enter valid mail address")
                else:
                    break
            #Allowing only specific DeptId to be inserted
            while True:
                DeptId=input("Enter Dept Name of the Employee(HR/IT/SALE/FIN):-")
                if DeptId.upper() in Dep:
                    break
                else:
                    print("PLEASE enter valid Department Id")
            #allowing only specific designation to be inserted
            while True:
                Desig=input("enter the Designation(MANAGER(MGR),CLERK(CLK),VICE PRESIDENT(VP),PRESIDENT(PRES):- ")
                if Desig.upper() in Des:
                    break
                else:
                    print("PLEASE enter valid Designation")
                    #generating emp id
            while True:
                Eid=Name[:2]+l[:10]
                Eid=Eid.upper()
                print("YOUR EMP ID :-",Eid)
                if any(dict.get('ID')== Eid for dict in Rec1): # checking whether the id is there in dictionary or not
                    print("Employee Already Exists of this ID")
                else:
                    break
                time.sleep(5)

            Sal=float(input("Enter Salary :- "))

            Dat=datetime.datetime.now()
            Dat=Dat.date()
            Rec={"ID":Eid.upper(), "NAME":Name.upper(), "Mob":Mob, "Email":Email.upper(), "DeptID":DeptId.upper(),"Desig":Desig.upper(),"Sal":Sal,"DOB":DOB,"Date of joining":Dat}
            Rec1.append(Rec)
            pickle.dump(Rec,fil)
            ch=input("Do you want to enter more records(Y/N):- ")
            if ch=="N" or ch=="n":
                break
        fil.close()
        with open(F,'wb') as fil:
            pickle.dump(Rec1,fil)
    except ValueError:
        print("Invalid value entered")
def Display(F): #function to display the records in the binary File
    try:
        with open(F,'rb') as fil:
            F="%15s %15s %15s %17s %15s %15s %15s %17s %15s"
            print(F%("ID","NAME","MOBILE","EMIAL ADDRESS","DEPT ID", "DESIGNATION","SALARY","DATE OF BIRTH","DATE OF JOINING"))
            print("="*140)
            Rec=pickle.load(fil)
            c=len(Rec)
            for i in Rec:
                for j in i.values():
                    print("%15s" % j, end=' ')
                print()
            print("*"*140)
            print("Total Records : ",c)
    except EOFError:
        print("="*140)
        print("TOtal Records : ",c)
    except FileNotFoundError:
        print(F, "File Does not Exist")
def DisplayonDesign(F):
    try:
        with open(F,'rb') as fil:
            Des=["MGR","CLK","VP","PRES"]
            print("="*140)
            Rec=pickle.load(fil)
            while True:
                D=input("Enter the Designation(MGR/CLK/PRES/VP)")
                if D.upper() in Des:
                    break
            c=0
            F="%15s %15s %15s %17s %15s %15s %15s %17s %15s"
            print(F%("ID","NAME","MOBILE","EMIAL ADDRESS","DEPT ID", "DESIGNATION","SALARY","DATE OF BIRTH","DATE OF JOINING"))
            print("="*140)
            for i in Rec:
                if i["Desig"]==D.upper():
                    c+=1
                    for j in i.values():
                        print("%15s" % j, end=' ')
                    print()
            print("*"*140)
            print("Total records : ",c)
    except EOFError:
        print("="*140)
        print("TOtal Records : ",c)
    except FileNotFoundError:
        print(F, "File Does not Exist")
    time.sleep(10)
def Update(F): #to update
    try:
        with open(F,'rb+') as fil:
            found=1
            Rec=pickle.load(fil)
            A=input("Enter the EMP ID whose details to be changed:-")
            for p in Rec:
                if A==p["ID"]:
                    found=0
                    for i,j in p.items():
                        if i!="DOJ":
                            ch=input("change " + i + " (Y/N)")
                            if ch=="y" or ch=="Y":
                                p[i]=input("Enter new " +i+ ":-" )
                                p[i]=p[i].upper()
                        elif i=="Sal":
                            ch=input("Change " + i +" (Y/N)")
                            if ch=="y" or ch=="Y":
                                p[i]=float(input("Enter " +i+ ":-" ))
                    break
            if found==-1:
                print("Employee deatails not found")
            else:
                fil.seek(0)
                pickle.dump(Rec,fil)
    except EOFError:
        print("="*140)
        print("Total Records : ", c)
    except FileNotFoundError:
        print(F, "File Does not Exist")
def Delete(F):
    try:
        with open(F,'rb+') as fil:
            Rec=pickle.load(fil)
            ch=input("Enter the Employee ID to be deleted:- ")
            for i in range(0, len(Rec)):
                if Rec[i]["ID"]==ch:
                    print("*"*140)
                    F="%15s %15s %15s %17s %15s %15s %15s %17s %15s"
                    print(F%("ID","NAME","MOBILE","EMIAL ADDRESS","DEPT ID", "DESIGNATION","SALARY","DATE OF BIRTH","DATE OF JOINING"))
                    N=Rec.pop(i)
                    for j in N.values():
                        print('%15s' % j,end=" ")
                    print()
                    print("Record Deleted")
                    break
                else:
                    print("Record Not Found")
            fil.seek(0)
            pickle.dump(Rec,fil)

    except FileNotFoundError:
        print(F, "File Does not Exist")
    except KeyError:
        print("REcord Not found")
    except IndexError:
        print("REcord Not found")
def SearchAcc(F):
    try:
        with open(F,'rb+') as fil:
            Rec=pickle.load(fil)
            ch=input("Enter the Employee ID to be Searched:- ")
            for i in Rec:
                if i["ID"]==ch.upper():
                    print("*"*140)
                    F="%15s %15s %15s %17s %15s %15s %15s %17s %15s"
                    print(F%("ID","NAME","MOBILE","EMIAL ADDRESS","DEPT ID", "DESIGNATION","SALARY","DATE OF BIRTH","DATE OF JOINING"))
                    print("*"*140)
                    for j in i.values():
                        print('%15s' % j,end=" ")
                    print()
                    
                    break
                else:
                    print("Record Not Found")


    except FileNotFoundError:
        print(F, "File Does not Exist")
    time.sleep(10)
def SearchName(F):
    try:
        with open(F,'rb+') as fil:
            Rec=pickle.load(fil)
            found=0
            ch=input("Enter the Employee Name to be Searched:- ")
            print("*"*140)
            F="%15s %15s %15s %17s %15s %15s %15s %17s %15s"
            print(F%("ID","NAME","MOBILE","EMIAL ADDRESS","DEPT ID", "DESIGNATION","SALARY","DATE OF BIRTH","DATE OF JOINING"))
            print("*"*140)
            for i in Rec:
                if i["NAME"]==ch.upper():
                    found+=1
                    for j in i.values():
                        print('%15s' % j,end=" ")
                    print()
                if found==0:
                    print("Record Not Found")
                else:
                    print("Total records displayed : ", found)
                    


    except FileNotFoundError:
        print(F, "File Does not Exist")
    except EOFError:
        print("record not found")
    time.sleep(10)

fi="Employee.dat"
while True:
    Menu()
    ch=input(" Enter your Choice :- ")
    if ch=="1":
        Insert(fi)
    elif ch=="2":
        SortAcc(fi)
        Display(fi)
        time.sleep(7)
    elif ch=="3":
        SortName(fi)
        Display(fi)
        time.sleep(7)
    elif ch=="4":
        SortDesig(fi)
        Display(fi)
        time.sleep(7)
    elif ch=="5":
        DisplayonDesign(fi)
    elif ch=="6":
        Display(fi)

        Delete(fi)
    elif ch=="7":
        Display(fi)

        Update(fi)
    elif ch=="8":
        SearchAcc(fi)
    elif ch=="9":
        SearchName(fi)
    elif ch=="10":
        print("Exiting...")


        break

    else:
        print("Wrong Choice Entered")












        
        
