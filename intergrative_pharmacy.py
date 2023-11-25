# PROJECT INTEGRATIVE PHARMACY
import mysql.connector as mjs
import datetime
# STATEMENT TO ESTABLISH CONNECTION TO SQL
DATABASE: PHARMACY
db=mjs.connect(host="localhost",user="root",password="12345",datab
ase="pharmacy")
cur=db.cursor()
cur.execute("create database if not exists pharmacy ")
cur.execute("create table if not exists med (code int primary key
auto_increment, medname varchar(25),advice varchar(50), price
float,purpose varchar(40))")
cur.execute("create table if not exists billhead (billno int primary key
auto_increment, amount float,billdate date)")
cur.execute("create table if not exists billdetails (billno int , code int,
description varchar(25),price float, qty int(3), billtotal float)")
def badd():
 print("<<< B I L L M E N U >>>")
 print(" List of medicines and advices available for customers")
 print("\t<<<\tMEDICINE DETAILS\t>>>\t")
 sql="select * from med"
 cur.execute(sql)
 print("="*90)
 print("%5s"%"code","%20s"%" Medname ","%20s"%"
Advice","%20s"%"Price","%20s"%"Purpose")
 print("="*90)
13
 for i in cur:

print("%5s"%i[0],"%20s"%i[1],"%20s"%i[2],"%20s"%i[3],"%20s"%i[4]
)
 print("="*90)
 order=[]
 mtot=0
 tdate=datetime.datetime.now()
 while True:
 mcode=int(input("Enter code: "))
 flag=0
 cur.execute("select * from med")
 mprice=0
 mname=" "

 for i in cur:
 if i[0]==mcode:
 flag=1
 mname=i[1]
 mprice=i[3]
 if flag==0:
 print("Medicine Not Available please see menu and order ")
 else:
 print("You ordered ",mname, "Having Price : ",mprice)
 mqty=int(input("Enter the quantity: "))
 mtotal=mprice*mqty
 mtot+=mtotal
 order.append([mcode,mname,mprice,mqty,mtotal])
 rep=input("Want to add more (Y/N): ")
 if rep in "nN":
 break
14
 cur.execute("insert into billhead (amount,billdate)values
(%s,%s)",(mtot,tdate))
 db.commit()
 cur.execute("select * from billhead")
 bn=0
 for i in cur:
 bn=i[0] # to get last bill number
 for i in order:
 b=i
 b.insert(0,bn)
 cur.execute("insert into billdetails values
(%s,%s,%s,%s,%s,%s)",i)
 print ("Please Pay Rs. ",mtot)
 db.commit()

def dsr():
 tdate=datetime.date.today()
 print("\t<<<\tDaily Sails Report \t>>>")
 print("="*50)
 print("Billno \tBill amount \t\tBill date")
 print("="*50)
 cur.execute("select * from billhead where billdate=%s",(tdate,))
 sales=0
 for i in cur:
 print(i[0],i[1],"\t",i[2],sep="\t")
 sales=sales+i[1]
 print("="*50)
 print("Todays Sales is : Rs. ",sales)
 print("="*50)
def ds():
 print("\t<<<\tDate wise Sales Report \t>>>")
15
 print("="*50)
 print("Billno \tBill amount \t\tBill date")
 print("="*50)
 tdate=input("Enter Date of which sale is required (yyyy-mm-dd) :
")
 cur.execute("select * from billhead where billdate=%s",(tdate,))
 sales=0
 for i in cur:
 print(i[0],i[1],"\t",i[2],sep="\t")
 sales=sales+i[1]
 print("="*50)
 print("Today's Sales are: Rs.",sales)
 print("="*50)

def Bmenu():
 while True:
 print("\n<<<<<Bill Master>>>>>")
 print("1. Generate Bill")
 print("2. Daily Sales Report")
 print("3. Sale on Specific date")
 print("4. Exit")
 ch=int(input("Enter your choice(1-4) :"))
 if ch==1:
 badd()
 elif ch==2:
 dsr()
 elif ch==3:
 ds()
 elif ch==4:
 return
 else:
16
 print("<<<<<<<<< INVALID CHOICE >>>>>>>>>")
def iadd():
 print("\n<<<\tMED ADDITION MODULE\t>>>")
 mname=input("Enter Name of the medicine : ")
 madvice=input("Enter the advice: ")
 mprice=float(input("Enter Price : "))
 mpurpose=input("Enter the purpose of medicine: ")
cur.execute("insert into med(medname,advice,price,purpose)
values(%s,%s,%s,%s)", (mname,madvice,mprice,mpurpose))
 db.commit()
def imod():

 print("\n<<<\tMED MODIFICATION MODULE\t>>>")
 mcode=int(input("Enter code of medicine to Modify: "))
 sql="select * from med where code=%s;"
 cur.execute(sql,(mcode,))
 for i in cur:
 pass
 print(cur.rowcount)
 if cur.rowcount==-1:
 print("No such code exists")
 else:
 print("Medicine Name : ",i[1])
 print("Old Medicine Price",i[3])
 mprice=float(input("Enter New Price : "))
 sql="update med set price=%s where code=%s"
 cur.execute(sql,(mprice,mcode))
 db.commit()
 print("Price Updated")
17
def ishow():
 print("\n\t<<<\tBILL DETAILS\t>>>\t")
 sql="select * from med"
 cur.execute(sql)
 print("="*95)
 print("%10s"%"code","%20s"%" Medname ","%20s"%"
Advice","%20s"%"Price","%20s"%"Purpose")
 print("="*95)
 for i in cur:

print("%10s"%i[0],"%20s"%i[1],"%20s"%i[2],"%20s"%i[3],"%20s"%i[4
])
 print("="*95)

def sb():
 bn=int(input("Enter Billno : "))
 cur.execute("select * from billhead where billno=%s",(bn,))
 print("\t<<<\tBill Head \t>>>")
 print("="*50)
 print("Billno \tBillamount \t\tBill date")
 print("="*50)

 sales=0
 for i in cur:
 print(i[0],i[1],"\t",i[2],sep="\t")
 print("="*50)
 cur.execute("select * from billdetails where billno=%s",(bn,))
 print("\t<<<\tBill Details \t>>>")
 print("="*50)
 print("code \tMedname price\t qty \t Total")
 print("="*50)
 for i in cur:
18
 print(i[1],i[2],i[3],i[4],i[5],sep="\t")
 print("="*50)

 print("="*50)

def Imenu():
 while True:
 print("\n<<<<<Medicine Master>>>>>")
 print("1. Add Medicine Details")
 print("2. Modify Modicine Details")
 print("3. Show all Medicines ")
 print("4. Exit")
 ch=int(input("Enter your choice(1-4) :"))
 if ch==1:
 iadd()
 elif ch==2:
 imod()
 elif ch==3:
 ishow()
 elif ch==4:
 return
 else:
 print("<<<<<<<<< INVALID CHOICE >>>>>>>>>")
def reports():
 print("\n1. Daily Sales Report")
 print("2. Sale on Specific date")
 print("3. Show bill detail")
 print("4. Exit")
 ch=int(input("Enter your choice(1-4) :"))
 if ch==1:
19
 dsr()
 elif ch==2:
 ds()
 elif ch==3:
 sb()
 elif ch==4:
 return
 else:
 print("<<< invalid Choice >>>")
def Main():
 while True:
 print("\n<<<<<Main Menu>>>>>")
 print("1. Medicine Master ")
 print("2. Bill Master")
 print("3. Reports")
 print("4. Exit")
 ch=int(input("Enter your choice(1-4) :"))
 if ch==1:
 Imenu()
 elif ch==2:
 Bmenu()
 elif ch==3:
 reports()
 elif ch==4:
 break
 else:
 print("<<<<<<<<< INVALID CHOICE >>>>>>>>>")
try:
 Main()
except:
 print(" Sorry Some error occured . Exiting the Program")
