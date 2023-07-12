from math import * 
print("hallo world")
print("hi!")
print(10)
#---------------------------------------------
#print the type of variable
print(type(10))      #output == int
print(type(44.55))   #output == floot
print(type([1,2,3,4,5])) #output == list
print(type((1,2,3,4,5)))   #output == tuple
print(type({"one":1 , "two":2 , "three":3})) #output == dict (dictionary)
print(type(3==3)) #output == bool
#---------------------------------------------
#                 variables
name = "sherif"
print (name)
a,b,c = 1,2,3
print(a)
print(b)
print(c)
#-----------------\b == back space---------------
print("sherif samy")
#-----------------\ == escape new line-----------
print("sherif \
samy \
muhsen")
#-----------------\\ == print { 1 --> \ }------------------
print("i love coding \\ ") #output == i love coding \
print("i love coding \'test\'")#output == i love cading'test'
print("i love coding \"test\"")#output == i love cading"test"
#------------------\n == new line--------------------------
print("sherif\nsamy")
#------------------\r == carriage return-------------------
print("123456\rabcd")
#----------------------------------------------------------
#-------------------concatenation : الدمج ----------------
x = "i love"          
y = "python"          #z = x+y  
print( x + " " + y )  #print(z)
#---------------------------------------------------------
mystring1 = """frist
second
third
fourd"""
print(mystring1)
#----------------------------------------------------------
#------------index []  =  ( access single item )-----------
print(mystring1[0])  #output ==> f
print(mystring1[-1]) #output ==> d
#----------------------------------------------------------
#-------slicing  =  (access multiple sequence items)-------
#--------------------{end not incloding}-------------------
print(mystring1[0:12])  #output ==> frist second
print(mystring1[0:-11]) #output ==> frist second
print(mystring1[0::2])  #print char scape [  char  ]
print(mystring1[::3])   #print char scapr [ 2 char ]
#----------------------------------------------------------
#--------------------[ string Methods ]--------------------
a = "    i love python    "
print(len(a)) #[ output ==> 13 ] == [console.WriteLine(a.lentgh)]
#--------------[ strip() , rstrip() , lstrip() ]-----------
print(a.strip())     #output ==> i love python
print(a.rstrip())    #output ==> .....i love python
print(a.lstrip())    #output ==> i love python.....
b = "###########sherif samy##########"
print(a.strip("#"))  #output ==> sherif samy
#--------------[ split() , rsplit() , lsplit ]-------------
#-------------[ it convert string to list ]----------------
print(a.split()) #output ==> ['i', 'love', 'python']
#------------------------[ center() ]----------------------
print(name.center(10 , "$")) #output ==> [$$sherif$$]
#----------------------------------------------------------
#----------------------------------------------------------
#------------------------[numbers]-------------------------
print(str(5))      #convert num to string
print(abs(-6))     #output ==> 6 
print(pow(2,3))    #output ==> 8 
print(max(4,10))   #output ==> 10
print(min(4,10))   #output ==> 4
print(round(3.7))  #output ==> 4
print(round(3.3))  #output ==> 3
print(sqrt(9))     #output ==> 3
#----------------------------------------------------------
#--------------------[getting inputs]----------------------
Name = input("enter your name : ")
print(Name) # not runn on output run on terminal onle
#----------------------------------------------------------
#------------------[building a calculator]-----------------
num1 = int( input("plz enter num 1 : "))
num2 = int( input("plz enter num 2 : "))
result = num1+num2
print(result)
#----------------------------------------------------------
#--------------------[build frist game]--------------------
#-----------------------[mad libs]-------------------------
coler = input("enter coler : ")
plural_noun = input("enter plural_noun : ")
adjective = input("enter adjective : ")
print("tree are "+coler)
print(plural_noun+" are mean")
print("plz keep it "+adjective)
#----------------------------------------------------------
#-----------------------[lists]----------------------------
cars = [ "bmw" , "c180" , "tyota" , "bogg" , "oooo" ]
learn = [ "html" , "css" , "c++" , "js"]
print(cars[1:3])          #output ==> ["c180" , "tyota"]
print(cars[-1:])          #output ==> ["ooo"]
print(cars[:3])           #output ==> ["bmw", "c180"]
#cars.extend(learn)       #output ==> cars + learn
#print(cars)
cars += learn
print(cars)
learn.append("c#")        #plus the variable on the list
learn.insert(0,"python")  #plus but in any place on the list
learn.remove("python")    #remove any variable you want
learn.pop()               #remove last variable
learn.sort()              #sort[arrange]variables by [a,b,c,....][1,2,3,....]
Lcode = learn.copy()      #make a copy in new list[not change when you change old list]
print(learn) 
#--------------------------------------------------------------------------------------
#-----------------------[tuples الصفوف]-----------------------------------------------
tuple = ( 22 , 23 , 24 , 25 , 26)
print(tuple)
print(tuple[3])
list_of_tuples = [ (2,3) , (3,4) , (4,5) , (5,6)]
print(list_of_tuples)
print(list_of_tuples[2])
#--------------------------------------------------------------
#------------------------[functions]---------------------------
def say_hi():             #defination
    print('hello')

say_hi()                  #calling
                  #######################
def name_age(name,age):
    print("hi " + name + " my age is : " +str(age))

name_age("sherif",18)     #calling function with arguments
                  ########################
#def sum(num3 ,num4):
#    num3 = input("enter fnum : ")    num4 = input("enter snum : ")
#    print(num3,num4)
#    return num3+num4
# print(sum())
#-------------------------------------------------------------------------
#------------------------[if conditionals]--------------------------------
is_hungry = input("Are you hungry ? : ")
if is_hungry == "yes" or is_hungry == "Yes":
    print("go to eat.")
elif is_hungry == "no" or is_hungry == "No":
    print("go to sleep.")
else :
    print("try again.")
#-------------------------------------------------------------------------
#________________________[comparisons  المقارانات]_______________________
num1 = input("enter the fnum : ")
num2 = input("enter the snum : ")
num3 = input("enter the thrnum : ")
if num1 >= num2 and num1 >= num3 :
    print(num1 + " ==> [num1] is the Bigest")
elif num2>= num1 and num2 >= num3 :
    print(num2 + " ==> [num2] is the Bigest")
else : 
    print(num3 + " ==> [num3] is the bigest")
#_________________________________________________________________________
#_____________________________[calculator]________________________________
num1 = float(input("enter the fnum : "))
mark = input("enter the mark [ + , * , - , / , % ] :")
num2 = float(input("enter the snum : "))
if mark == "+":
    result= num1 + num2
    print(str(num1) + " + " + str(num2) +" = "+ str(result))
elif mark == "-":
     result= num1 - num2
     print(str(num1) + " - " + str(num2) +" = "+ str(result))
elif mark == "*":
     result= num1 - num2
     print(str(num1) + " * " + str(num2) +" = "+ str(result))
elif mark == "/":
     result= num1 - num2
     print(str(num1) + " / " + str(num2) +" = "+ str(result))
elif mark == "%":
     result= num1 - num2
     print(str(num1) + " % " + str(num2) +" = "+ str(result))
else :
    print("wrong choice ! try agian .")
#________________________________________________________________________
#_______________________[dictionary القواميس]___________________________
convert_month = {
    1 or"jan":"january",
    2 or"feb":"february ",
    3 or"mar":"march",
    4 or"apr":"aprile",
    5 or"may":"may",
    6 or"jun":"june",
    7 or"jul":"july",
    8 or"aug":"agustus",
    9 or"sep":"september",
   10 or"oct":"oktober",
   11 or"nov":"november",
   12 or"dec":"december"}
print(convert_month["jan"])
print(convert_month.get(13 , "not incloud"))
#_______________________________________________________________________
#__________________________[ while loops ]____________________________________
i = int( input("enter i : "))
while i <= 10 :
    if i==4:
        continue
    elif i==6 : 
        break
    print(i)
    i += 1
else : 
    print("end of loop ")
#_______________________________________________________________________
#____________________________[ for loop ]_______________________________
carrs = [" bmw " , " c180 " , " bugatty " , " dudg " , " frrari " , " lampo " ]
for car in carrs:
    print(car)
#---------------------------------------------------------
for num in range(10):
    print(num)
#---------------------------------------------------------
for num in range(5 , 21):
    print(num)
#---------------------------------------------------------
for num in range(11):
    if num % 2 == 0:
        print(num , "is even number")

    else:
        print (num, " is odd number.")
#---------------------------------------------------------
for num in range(2 , 11):
    if num == 5 :
        continue
    print(num)