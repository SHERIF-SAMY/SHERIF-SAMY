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
num1 = input("plz enter num 1 : ")
num2 = input("plz enter num 2 : ")
result = int(num1)+int(num2)
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
cars = [ "bmw" , "c180" , "tyota" , "bogg" , "ooo" ]
learn = [ "html" , "css" , "c++" , "js"]
print(cars[1:3])      #output ==> ["c180" , "tyota"]
print(cars[-1:])      #output ==> ["ooo"]
print(cars[:3])       #output ==> ["bmw", "c180"]
#cars.extend(learn)   #output ==> cars + learn
#print(cars)
cars += learn
print(cars)
