#Display String as it is
blocktext = '''
"EAST WEST
NORTH SOUTH"
'''
print(blocktext)

#Counting character in string's
s1 = "python"
s2 = "programming"
print(len(s1))
print(len(s2))

#lstrim, rstrim, strim Example
uname = ' sai'.strip()
uname1 = ' sai'.lstrip()
uname2 = 'sai '.rstrip()

if uname == 'sai':
    print("Hai...",uname)
else:
    print("Hello...Guest")

if uname1 == 'sai':
    print("Hai...",uname)
else:
    print("Hello...Guest")

if uname2 == 'sai':
    print("Hai...",uname)
else:
    print("Hello...Guest")


# Replace String of to another
s="Learning Python is very difficult"
s1=s.replace("difficult","easy")
print(s1)


#string's are split in to multiple substring
s="java python angular oracle"
print(s)
courses=s.split()
print(courses)
for course in courses:
    print(course)


#split string as / 
date="07/15/1947"
print(date)
tokens = date.split('/')
for token in tokens:
    print(token)


#string case's conversion
title='pyThon proGraming'
print(title)
print(title.upper())
print(title.lower())
print(title.title())
print(title.capitalize())
print(title.swapcase())



#substring split with function startwith and endwith 
s='python programming is fun'
print(s.startswith('python'))
print(s.endswith('fun'))
print(s.startswith('Java'))
print(s.endswith('easy'))



# email id Varification in python
email = input("Enter your Email id: ")
if email.endswith('@gmail.com'):
    print("It's a gmail id")
elif email.endswith('@yahoo.com'):
    print("It's a yahoo email id")
elif email.endswith('@outlook.com'):
    print("It's a Outlook email id")
else:
    print("Other email id ")



names = ["Ramesh","Rajesh","Somesh","Kamesh"]
for name in names:
    if name.startswith('R'):
        print(name)