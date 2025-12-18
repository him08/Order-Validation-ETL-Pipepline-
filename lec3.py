#loops for loop (dictionary)

ipl ={
    "CSK":"CHENNAI ",
    "MI":"MUMBAI"
}
# dictionary items key value are printed in form of tupple
print(ipl.items())

# convienent name >
for team,name in ipl.items():
    # i me teams aagyi CSK AND MI nd then ipl[i krkre unka value
    print(team)
    print(name)

# ********continue and break**************
ipl=['csk','mi','gt','rj']
for team in ipl:
    print(team)
    if team == 'mi':
        break
    # when we see MI then i need to stop and dont don anything

for team in ipl:
    print(team)
    if team == 'mi':
        continue

# list comprehention
IPL=['CSK','MI','GT','RJ']
ipl_len=[]
for team in IPL:
    ipl_len.append(len(team))

# **************using list comprehention***************
ipl_len_com= [len(team) for team in IPL]

# now if we want a conditon here--
# simple first what you want and then for loop and then the if condition
ipl_len_com =[len(team) for team in IPL if len(team)>2]

print(ipl_len)
print(ipl_len_com)

# ***** ERROR HANDLING *****************(try,except)
# a=1/0

try:
    a=1/0
    print(a)
except Exception as e:
    print('this is exception block')
    print(e)
else:
    print('this is else block')
    # here listen if no exception then else is printed easily
finally:
    print('this is finally block')
    # this will always go to finally block

#  ************ FILES HANDLING ***********
# file name and read mode r

f=open("file1.txt","r")
print(f.read())

# read line by line>>
for line in f:
    print(line)

f.close()

# write mode--overwrite all the content --keep overwriting

f=open("file1.txt","w")
f.write("hello world")
f.close()

# no overwrite just append --APPEND MODE

f=open("file1.txt","a")
f.write("hello world \n")
f.close()


