#!/usr/bin/env python3 

import os
while True:
    try: #error handling with os.read
        userIn = os.read(0,1024) #acts like myreadline and passes entirity of what is rea
        if (len(userIn)>1):#input detected
            userIn = userIn.decode().split('\n') #remove end of line
            for i in userIn:
                os.write(1, (str(i.split())).encode()) #tokenize input,
                if len(i.split()) == 0:
                    break
                #if empty it will still keep running
    except EOFError:
        print('There has been an error')
