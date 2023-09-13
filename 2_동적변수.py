for i in range(1,8) :
    globals()["name{}".format(i)] = i
for i in range(1,8) :
    print("name{}".format(i))
    print(globals()["name{}".format(i)])        
for i in range(1,8) :
    globals()["Name{}".format(i)] = "robot{}".format(i)            
Name6 = "hi"
for i in range(1,8) :
    print(globals()["Name{}".format(i)])