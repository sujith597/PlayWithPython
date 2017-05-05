import sys
x ="Foo";
print ("Hello Python")
sys.stdout.write(x + '\n')
days = ['Monday','Tuesday','Wednesday', 'Thursday', 100,1000]
tuplesList = ("abc",1, "bcd",2,"sada",3)
pythonDict ={}
pythonDict["first"] = "Im First element"
pythonDict["second"] =" Im second element"
print(days[0])
print(days[1:3])
print (days[2:])
print(tuplesList[0])
print(tuplesList[0:])
print(pythonDict['first'])

count =0
while(count < 9) :
	print ('The cound is ', count)
	count = count +1
	
for var in tuplesList :
	print(var)