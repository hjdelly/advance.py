import datetime                                # imported datetime library/dependecy
from time import sleep                         # imported time from sleep library/dependency
#for in loop below
for i in range(5):    # range of 5
    file_builder = open("logger.txt", "a+")             # decalre a variable file_builder set equal to open and to create the file put logger.txt then append a+ string 
    file_builder.write(f'{datetime.datetime.now()}\n')  # now to write to the file- call the write function, use string literals-say datetime then datetime now to call the function
    file_builder.close()                                # say file_builder then set it equal to the close function 

    print("file created")                               

    sleep(1)                                            

    