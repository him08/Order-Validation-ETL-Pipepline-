# FUNCTIONS



def getSum(a,b):
    return a+b


print(getSum(1,2))

def sum(a,b=1):
    return a+b

print(sum(1))

def myparam(a,b):
    return a+b
# aise bhi hoskta hai now a=2 and b=1 hogya
# KEYWORD ARGUMENTS
print(myparam(b=1,a=2))

# arguments kitne bhi--
# DYNAMIC PARAMETERS -->>>>
def getsums(*args):
    print(args,type(args))
    num=0
    for a in args:
        num=num+a
    return num

d=getsums(1,2,3)
print(d)

# KEYWORD ARGUMENTS FOR THIS--
def getsums1(**kargs):
    print(kargs,type(kargs))

d=getsums1(a=1,b=2,c=3)
print(d)

# we can also import from diff python file script like using import calc then calc.getSum
# or we can make folder mypackage and their make files and import them as--
# import mypackage.calc as c
#import mypakcage.calc as c1


#  instead of unnecassarily importing the whole file we can just import the methods from it that we want--
# from mypackage.c import getSum as g
# then use it like g.getSum(1,2)

