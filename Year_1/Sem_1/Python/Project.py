import mysql.connector

def choice():
    print("Are you a emplyee or are you a customer?? ")
    print("Please enter your class ['Employee' or 'Customer']")
    a=input('Enter : ')
    if a=='Employee' or a=='employee':
        emp()
    elif a=='Customer' or a=='customer':
        ty()
def welcome():
    f=open('Welcome.txt','r')
    l=f.readlines()
    for i in l:
        print(i)
    f.close()    
def emp():
    f=open('emp.txt','r')
    l=f.readlines()
    for i in l:
        print(i)
    print('Are you interested ? , press y to work with us else press n to stop ')
    a=input('Enter your choice : ')
    if a=='Y' or a=='y':
        empinfo()
    if a=='N' or a=='n':
        print('Apreciated your visit, please comeback if you change your mind ')
def ty():
    print('In which hotel would you like to stay ? ')
    f1=open('Hotel_1.txt','r')
    f2=open('Hotel_2.txt','r')
    l1=f1.readlines()
    for i in l1:
        print(i)
    l2=f2.readlines()
    for j in l2:
        print(j)
    print('press 1 to avail a room in Hotel Sea View (buliding 1)')
    print('press 2 to avail a room in Hotel Sea View (building 2)')
    a=int(input('enter choice : '))
    if a==1:
        welcome()
        h1()
    if a==2:
        welcome()
        h2()
#__________________________________________________________________________________________________________________________________________________#

def h1():
    a=input('Enter your name : ')
    n1=input('Enter the date till which you will stay (PLEASE ENTER THE DATE IN THIS FORMAT[YYYY-MM-DD]) : ')
    n=str(n1)
    c=mysql.connector.connect(host='localhost',user='root',password='3469',database='hotel_management_system')
    cur=c.cursor()
    cur.execute("select * from hotel_1")
    print('(floor_no,no_of_room,vacancy)')
    for i in cur:
        print(i)
    print('In which floor would you like to stay ? ')
    print('press 1 to avail a room in First Floor')
    print('press 2 to avail a room in Second Floor')
    print('press 3 to avail a room in Third Floor')
    x=int(input('Enter Your Choice : '))
    if x==1:
        cur.execute("select * from  hotel_1_floors_data where room_no like '1%' and rooms_occupied_by='Vacant'")
        print('(room_no | rooms_occupied_by | room_occupied_till)')
        for j in cur:
            print(j)
        print('In which room would you like to stay ? ')
        a1=int(input('Enter room number : '))
        if a1==104:
            cur.execute("update hotel_1_floors_data set rooms_occupied_by=%s where room_no=104",[a])
            cur.execute("update hotel_1_floors_data set room_occupied_till=%s where room_no=104",[n])
            print('Your room has been booked')
            a3=input('If you wish to verify your stay please press v or press c to cancel verify : ')
            if a3=='V' or a3=='v':
                cur.execute("select * from hotel_1_floors_data where rooms_occupied_by=%s",[a])
                print('(room_no | rooms_occupied_by | room_occupied_till)')
                for l in cur:
                    print(l)
                print('Enjoy your stay!')
            if a3=='c' or a3=='C':
                print('Enjoy your stay!')
        elif a1==105:
            cur.execute("update hotel_1_floors_data set rooms_occupied_by=%s where room_no=105",[a])
            cur.execute("update hotel_1_floors_data set room_occupied_till=%s where room_no=105",[n])
            print('Your room has been booked')
            a3=input('If you wish to verify your stay please press v or press c to cancel verify : ')
            if a3=='V' or a3=='v':
                cur.execute("select * from hotel_1_floors_data where  rooms_occupied_by=%s",[a])
                print('(room_no | rooms_occupied_by | room_occupied_till)')
                for l in cur:
                    print(l)
                print('Enjoy your stay!')
            if a3=='c' or a3=='C':
                print('Enjoy your stay!')
    elif x==2:
        cur.execute("select * from  hotel_1_floors_data where room_no like '2%' and rooms_occupied_by='Vacant'")
        for k in cur:
            print(k)
        print('In which room would you like to stay ? ')
        a1=int(input('Enter room number : '))
        if a1==203:
            cur.execute("update hotel_1_floors_data set rooms_occupied_by=%s where room_no=203",[a])
            cur.execute("update hotel_1_floors_data set room_occupied_till=%s where room_no=203",[n])
            print('Your room has been booked')
            a3=input(' if you wish to verify your stay please press v or press c to cancel verify')
            if a3=='V' or a3=='v':
                cur.execute("select * from hotel_1_floors_data where  rooms_occupied_by=%s",[a])
                print('(room_no | rooms_occupied_by | room_occupied_till)')
                for l in cur:
                    print(l)
                print('Enjoy your stay!')
            if a3=='c' or a3=='C':
                print('Enjoy your stay!')
        elif a1==204:
            cur.execute("update hotel_1_floors_data set rooms_occupied_by=%s where room_no=204",[a])
            cur.execute("update hotel_1_floors_data set room_occupied_till=%s where room_no=204",[n])
            print('Your room has been booked')
            a3=input('If you wish to verify your stay please press v or press c to cancel verify : ')
            if a3=='V' or a3=='v':
                cur.execute("select * from hotel_1_floors_data where  rooms_occupied_by=%s",[a])
                print('(room_no | rooms_occupied_by | room_occupied_till)')
                for l in cur:
                    print(l)
                print('Enjoy your stay!')
            if a3=='c' or a3=='C':
                print('Enjoy your stay!')
        if a1==205:
            cur.execute("update hotel_1_floors_data set rooms_occupied_by=%s where room_no=205",[a])
            cur.execute("update hotel_1_floors_data set room_occupied_till=%s where room_no=205",[n])
            print('Your room has been booked')
            a3=input('If you wish to verify your stay please press v or press c to cancel verify : ')
            if a3=='V' or a=='v':
                cur.execute("select * from hotel_1_floors_data where  rooms_occupied_by=%s",[a])
                print('(room_no | rooms_occupied_by | room_occupied_till)')
                for l in cur:
                    print(l)
                print('Enjoy your stay!')
            if a3=='c' or a3=='C':
                print('Enjoy your stay!')
    elif x==3:
        cur.execute("select * from  hotel_1_floors_data where room_no like '3%' and rooms_occupied_by='Vacant'")
        for z in cur:
            print(z)
        print('In which room would you like to stay ? ')
        a1=int(input('Enter room number : '))
        if a1==303:
            cur.execute("update hotel_1_floors_data set rooms_occupied_by=%s where room_no=303",[a])
            cur.execute("update hotel_1_floors_data set room_occupied_till=%s where room_no=303",[n])
            print('Your room has been booked')
            a3=input('If you wish to verify your stay please press v or press c to cancel verify : ')
            if a3=='V' or a3=='v':
                cur.execute("select * from hotel_1_floors_data where  rooms_occupied_by=%s",[a])
                print('(room_no | rooms_occupied_by | room_occupied_till)')
                for l in cur:
                    print(l)
                print('Enjoy your stay!')
            if a3=='c' or a3=='C':
                print('Enjoy your stay!')
        elif a1==304:
            cur.execute("update hotel_1_floors_data set rooms_occupied_by=%s where room_no=304",[a])
            cur.execute("update hotel_1_floors_data set room_occupied_till=%s where room_no=304",[n])
            print('Your room has been booked')
            a3=input('If you wish to verify your stay please press v or press c to cancel verify : ')
            if a3=='V' or a3=='v':
                cur.execute("select * from hotel_1_floors_data where  rooms_occupied_by=%s",[a])
                print('(room_no | rooms_occupied_by | room_occupied_till)')
                for l in cur:
                    print(l)
                print('Enjoy your stay!')
            if a3=='c' or a3=='C':
                print('Enjoy your stay!')
        if a1==305:
            cur.execute("update hotel_1_floors_data set rooms_occupied_by=%s where room_no=305",[a])
            cur.execute("update hotel_1_floors_data set room_occupied_till=%s where room_no=305",[n])
            print('Your room has been booked')
            a3=input('If you wish to verify your stay please press v or press c to cancel verify : ')
            if a3=='V' or a3=='v':
                cur.execute("select * from hotel_1_floors_data where  rooms_occupied_by=%s",[a])
                print('(room_no | rooms_occupied_by | room_occupied_till)')
                for l in cur:
                    print(l)
                print('Enjoy your stay!')
            if a3=='c' or a3=='C':
                print('Enjoy your stay!')
#__________________________________________________________________________________________________________________________________________________#

def h2():
    a=input('Enter your name : ')
    n1=input('Enter the date till which you will stay (PLEASE ENTER THE DATE IN THIS FORMAT[YYYY-MM-DD]) : ')
    n=str(n1)
    c=mysql.connector.connect(host='localhost',user='root',password='3469',database='hotel_management_system')
    cur=c.cursor()
    cur.execute("select * from hotel_2")
    print('(floor_no,no_of_room,vacancy)')
    for i in cur:
        print(i)
    print('In which floor would you like to stay ? ')
    print('press 1 to avail a room in First Floor')
    print('press 2 to avail a room in Second Floor')
    
    x=int(input('Enter Your Choice : '))
    if x==1:
        cur.execute("select * from  hotel_2_floors_data where room_no like '1%' and rooms_occupied_by='Vacant'")
        print('(room_no | rooms_occupied_by | room_occupied_till)')
        for j in cur:
            print(j)
        print('In which room would you like to stay ? ')
        a1=int(input('Enter room number : '))
        if a1==101:
            cur.execute("update hotel_1_floors_data set rooms_occupied_by=%s where room_no=101",[a])
            cur.execute("update hotel_1_floors_data set room_occupied_till=%s where room_no=101",[n])
            print('Your room has been booked')
            a3=input('If you wish to verify your stay please press v or press c to cancel verify : ')
            if a3=='V' or a3=='v':
                cur.execute("select * from hotel_1_floors_data where rooms_occupied_by=%s",[a])
                print('(room_no | rooms_occupied_by | room_occupied_till)')
                for l in cur:
                    print(l)
                print('Enjoy your stay!')
            if a3=='c' or a3=='C':
                print('Enjoy your stay!')
        elif a1==102:
            cur.execute("update hotel_1_floors_data set rooms_occupied_by=%s where room_no=102",[a])
            cur.execute("update hotel_1_floors_data set room_occupied_till=%s where room_no=102",[n])
            print('Your room has been booked')
            a3=input('If you wish to verify your stay please press v or press c to cancel verify : ')
            if a3=='V' or a=='v':
                cur.execute("select * from hotel_1_floors_data where  rooms_occupied_by=%s",[a])
                print('(room_no | rooms_occupied_by | room_occupied_till)')
                for l in cur:
                    print(l)
                print('Enjoy your stay!')
            if a3=='c' or a3=='C':
                print('Enjoy your stay!')
        elif a1==103:
            cur.execute("update hotel_1_floors_data set rooms_occupied_by=%s where room_no=103",[a])
            cur.execute("update hotel_1_floors_data set room_occupied_till=%s where room_no=103",[n])
            print('Your room has been booked')
            a3=input('If you wish to verify your stay please press v or press c to cancel verify : ')
            if a3=='V' or a3=='v':
                cur.execute("select * from hotel_1_floors_data where  rooms_occupied_by=%s",[a])
                print('(room_no | rooms_occupied_by | room_occupied_till)')
                for l in cur:
                    print(l)
                print('Enjoy your stay!')
            if a3=='c' or a3=='C':
                print('Enjoy your stay!')
        
    elif x==2:
        cur.execute("select * from  hotel_1_floors_data where room_no like '2%' and rooms_occupied_by='Vacant'")
        for k in cur:
            print(k)
        print('In which room would you like to stay ? ')
        a1=int(input('Enter room number : '))
        if a1==203:
            cur.execute("update hotel_1_floors_data set rooms_occupied_by=%s where room_no=104",[a])
            cur.execute("update hotel_1_floors_data set room_occupied_till=%s where room_no=104",[n])
            print('Your room has been booked')
            a3=input('If you wish to verify your stay please press v or press c to cancel verify : ')
            if a3=='V' or a3=='v':
                cur.execute("select * from hotel_1_floors_data where  rooms_occupied_by=%s",[a])
                print('(room_no | rooms_occupied_by | room_occupied_till)')
                for l in cur:
                    print(l)
                print('Enjoy your stay!')
            if a3=='c' or a3=='C':
                print('Enjoy your stay!')
        if a1==204:
            cur.execute("update hotel_1_floors_data set rooms_occupied_by=%s where room_no=204",[a])
            cur.execute("update hotel_1_floors_data set room_occupied_till=%s where room_no=204",[n])
            print('Your room has been booked')
            a3=input('If you wish to verify your stay please press v or press c to cancel verify : ')
            if a3=='V' or a3=='v':
                cur.execute("select * from hotel_1_floors_data where  rooms_occupied_by=%s",[a])
                print('(room_no | rooms_occupied_by | room_occupied_till)')
                for l in cur:
                    print(l)
                print('Enjoy your stay!')
            if a3=='c' or a3=='C':
                print('Enjoy your stay!')
        if a1==205:
            cur.execute("update hotel_1_floors_data set rooms_occupied_by=%s where room_no=205",[a])
            cur.execute("update hotel_1_floors_data set room_occupied_till=%s where room_no=205",[n])
            print('Your room has been booked')
            a3=input('If you wish to verify your stay please press v or press c to cancel verify : ')
            if a3=='V' or a3=='v':
                cur.execute("select * from hotel_1_floors_data where  rooms_occupied_by=%s",[a])
                print('(room_no | rooms_occupied_by | room_occupied_till)')
                for l in cur:
                    print(l)
                print('Enjoy your stay!')
            if a3=='c' or a3=='C':
                print('Enjoy your stay!')
#__________________________________________________________________________________________________________________________________________________#

def empinfo():
    c=mysql.connector.connect(host='localhost',user='root',password='3469',database='hotel_management_system')
    cur=c.cursor()
    print("Please register yourself to hotel's employee databse ")
    a=input('Please enter your name : ')
    d=input("Please enter the department you want to wonk on ['Cleaner','Chief','Receptionist'] : ")
    if d=='Cleaner' or d=='cleaner':
        print('Salary given to cleaner is between 10000 to 25000, please enter your price within this price range')
        s=int(input('Enter your desired salary : '))
        if s>=10000 and s<=25000:
            cur.execute("insert into Emp values(%s,%s,%s)",[a,d,s])
            print('You are a registered worker now !')
    if d=='Chief' or d=='chief':
        print('Salary given to chief is between 15000 to 30000, please enter your price within this price range')
        s=int(input('Enter your desired salary : '))
        if s>=15000 and s<=30000:
            
            cur.execute("insert into Emp values(%s,%s,%s)",[a,d,s])
            print('You are a registered worker now !')
    if d=='Receptionist' or d=='receptionist':
        print('Salary given to Receptionist is between 30000 to 50000, please enter your price within this range')
        s=int(input('Enter your desired salary : '))
        if s>=30000 and s<=50000:
            cur.execute("insert into Emp values(%s,%s,%s)",[a,d,s])
            print('You are a registered worker now !')
            
#__________________________________________________________________________________________________________________________________________________#

choice()