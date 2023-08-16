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

#lstrim, rstrim, strim
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