import mysql.connector
def add_user():
	quary1="insert into auth (u_id,paswrd,Name,phone) values (%s,%s,%s,%s)"
	user_name=input("enter an user name : ")
	quary2="select paswrd from auth where u_id LIKE "+ "'"+user_name+"'"
	mycursor.execute(quary2)
	result=mycursor.fetchall()
	l=len(result)
	if l==0:
		password=input("enter your password : ")
		name=input("enter your full name : ")
		phone= input("enter your phonenumber")
		val=list()
		val.append(user_name)
		val.append(password)
		val.append(name)
		val.append(phone)
		val1=tuple(val)
		mycursor.execute(quary1,val1)
		mydb.commit()
		print("signup succesfull")
	else:
		print("user already registered")
def login():
	j=0
	user_name=input("enter an user name : ")
	quary2="select paswrd from auth where u_id LIKE "+ "'"+user_name+"'"
	mycursor.execute(quary2)
	result=mycursor.fetchall()
	i=len(result)
	if i> 0:
		password=input("enter your password : ")
		if result[0][0]==password:
			print("log in succesfull")
			j=1
		else:
			print("wrong password")
	else:
		print("wrong username")
	return j,user_name
def show_user():
	quary3="select Name from auth"
	mycursor.execute(quary3)
	result=mycursor.fetchall()
	for i in result:
		print (i)
def admin_login():
	user_name=input("enter an user name : ")
	quary2="select paswrd from admin where u_id LIKE "+ "'"+user_name+"'"
	mycursor.execute(quary2)
	result=mycursor.fetchall()
	i=len(result)
	if i> 0:
		password=input("enter your password : ")
		if result[0][0]==password:
			print("log in succesfull")
			s='''press 1 to add new user
				 press 2 to show the the user database
				 press 3 to show names and phone number
				 press 4 to delete a record
				 press 5 to add product in stock
				 press 6 to exit
				 '''
			print(s)
			choice=int(input("enter your choice"))
			while choice!=6:
				
				if choice ==1:
					add_user()
					print(s)
					choice=int(input("enter your choice"))
				elif choice == 2:
					print("hello")
					quary4="select * from auth"
					mycursor.execute(quary4)
					result=mycursor.fetchall()
					for i in result:
						print (i)
					print(s)
					choice=int(input("enter your choice"))
				elif choice == 3:
					show_user()
					print(s)
					choice=int(input("enter your choice"))
				elif choice==4:
					user_name=input("enter the user name you want to delete")  
					quary6="delete from auth where u_id="+"'"+user_name+"'"
					mycursor.execute(quary6)
					mydb.commit()
					print("deleted succesfully")
					print(s)
					choice=int(input("enter your choice"))
				elif choice==5:
					stock()
					print(s)
					choice=int(input("enter your choice"))

		else:
			print("wrong password")
	else:
		print("wrong username")
def update(i,user_name):
	if i==1:
		#phonenumber
		new_phonne=input("enter your new phone number")
		quary5="update auth set phone="+"'"+new_phonne+"'"+"where u_id="+"'"+user_name+"'"
		mycursor.execute(quary5)
		mydb.commit()
		print("update succesfull")
		i=int(input("press 1 if you want to update your phone no.\n press 2 to update your name \n press 3 to change user name\n press 4 to change password\n press 0 to exit"))
		return i
	elif i==2:
		#name:
		new_name=input("enter your name")
		quary5="update auth set Name="+"'"+new_name+"'"+"where u_id="+"'"+user_name+"'"
		mycursor.execute(quary5)
		mydb.commit()
		print("update succesfull")
		i=int(input("press 1 if you want to update your phone no.\n press 2 to update your name \n press 3 to change user name\n press 4 to change password\n press 0 to exit"))
		return i
	elif i==3:
		#user_id
		new_user_id=input("enter new user id")
		quary5="update auth set u_id="+"'"+new_user_id+"'"+"where u_id="+"'"+user_name+"'"
		mycursor.execute(quary5)
		mydb.commit()
		print("update succesfull")
		print("log in again")
		i=0
		return i
	elif i==4:
		#pswrd	
		new_password=input("enter new password")
		quary5="update auth set paswrd="+"'"+new_password+"'"+"where u_id="+"'"+user_name+"'"
		mycursor.execute(quary5)
		mydb.commit()
		print("update succesfull")
		print ("log in again")
		i=0
		return i
def stock():
	s1='''press 1 the product is new
	press 2 to refill stock
	press 3 to update price
	press 4 to sale 
	press 0 to exit'''
	print (s1)
	switch=int(input("enter your option"))
	while switch!=0:
		if switch==1:
			product=input("enter the product name")
			quantity=input("enter the quantity")
			price=input("enter the price")
			val=list()
			val.append(product)
			val.append(quantity)
			val.append(price)
			val1=tuple(val)
			quary6="insert into stock (product,quantity,price) values (%s,%s,%s)"
			mycursor.execute(quary6,val1)
			mydb.commit()
			print("entry succlesfull")
			print (s1)
			switch=int(input("enter your option"))
		elif switch==2:
			product=input("enter the product name")
			quantity=int(input("enter the new quantity to be added"))
			quary6="select quantity from stock where product LIKE "+ "'"+product+"'"
			mycursor.execute(quary6)
			result=mycursor.fetchall()
			i=int(result[0][0])
			newquantity=i+quantity
			print(str(newquantity))
			quary7="update stock set quantity="+"'"+str(newquantity)+"'"+"where product="+"'"+product+"'"
			mycursor.execute(quary7)
			mydb.commit()
			print("update succesfull")
			print (s1)
			switch=int(input("enter your option"))
		elif switch==3:
			product=input("enter the product name")
			new_price=input("enter the new price")
			quary7="update stock set price="+"'"+new_price+"'"+"where product="+"'"+product+"'"
			mycursor.execute(quary7)
			mydb.commit()
			print("update succesfull")
			print (s1)
			switch=int(input("enter your option"))
		elif switch==4:
			product=input("enter the product name")
			sell_quantity=int(input("enter the new quantity to be sold"))
			quary6="select quantity from stock where product LIKE "+ "'"+product+"'"
			quary8="select price from stock whre product LIKE"+"'"+product+"'"
			mycursor.execute(quary6)
			result=mycursor.fetchall()
			i=int(result[0][0])
			if i >= sell_quantity: 
				print(sell_quantity)        			#n.t.o.i
				newquantity=i-sell_quantity
				quary7="update stock set quantity="+"'"+str(newquantity)+"'"+"where product="+"'"+product+"'"
				mycursor.execute(quary8)
				result=mycursor.fetchall()
				i=int(result[0][0])
				i=(i*sell_quantity)
				print("yous total price id"+str(i))
			else: 
				print("not available")



s='''press 1 to signup
press 2 to log in
press 3 for admin login'''
print(s)   

mydb = mysql.connector.connect(host="localhost",user="root",passwd="root",database="login")
mycursor=mydb.cursor()
a=int(input("\nenter your choice"))

if a==1:
	add_user() #signup 
		
elif a==2:
	j,user_name=login() #user
	i=0
	if j==1:
		i=int(input("press 1 to update your phone no.\n press 2 to update your name \n press 3 to change user name\n press 4 to change password\npress 5 to edit in stocks\n press 0 to exit\n"))
		while i!=0:
			if i==5:
				stock()
			else:
				i=update(i,user_name)
	
elif a==3:
	admin_login() #admin