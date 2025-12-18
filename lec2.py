# TUPPLES -- >

# A=[1,2,3] ---LIST
# BUT TUPPLES WITH ROUND BRACKETS -- >
# tupples are immutable but list are mutable

A=(1,2,3)
# print(type(A))
# A[1]=5   you cant modify tupples
print(A)
A=(12,32,32)
print(A)

#DICTIONARIES -->
IPL =['CSK','MI','RCB']
# NOW SUPPOSE WE WANT TO STORE CSK AS CHENNAI SUPPER KINDS AND SO ON SO WE CAN USING LIST OF LIST
IPL=[['CSK','CHENNAI SUPPER KINGS'],['MI','MUMBAI'],['RCB','ROYALS BANGLORE']]
print(IPL[0])
# so if we want to store the key value pair like in this case so we can use dictionaries--
IPL={
    "CSK":"CHENNAI SUPPER KINGS",
    "MI":"MUMBAI",
    "RCB":"ROYALS BANGLORE"
}
print(IPL["CSK"])
# DICTIONARIES ARE MUTABLE

IPL["GT"]="gujarat"
print(IPL)

# DELETE
del(IPL["CSK"])
print(IPL)

#nested dictionary--
ipl={
    "CSK":{"NAME":"CHENNAI SUPPER KINGS","YEAR":"1960","cap":"MSD"},
    "MI":{"NAME":"MUMBAI","YEAR":"1980","cap":"Rohit"},
}
print(ipl["CSK"]["cap"])

# you can't give key as a list becoz list is mutable but keys are not thus we can give any data type like tupple
# eg (1,2) : {... but you can give lists in the values like "cap":['msd','jadeja']

# CONTROL FLOW
# BOOLEAN TYPE
print(1==1)
print(1==1 and 2==2)
print("MI" in IPL)

# IF ELSE -- CONTROL FLOWS --
marks=30
if marks<30:
    print("fail")
    print(f'marks are {marks}')
elif marks>=30:
    print("phewww")
else:
    print("pass")
print('this is outside if')

#LOOPS --
n=0
num=[1,2,3,4]
num_square=[]
while(n<len(num)):
    print(f"square of {n} is ")
    num_square.append(num[n]**2)
    n=n+1
print(num_square)

#for loops
num_square=[]
for n in num:
    print(n)
    num_square.append(n**2)
print(num_square)

# range function
num=[3,4,5,6]
for n in range(len(num)):
    print(n)
