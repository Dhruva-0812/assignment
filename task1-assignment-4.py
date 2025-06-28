try:                                                            #try if any exception occures or not
    f=open("sample.txt",'r')                                    #opening of file in read mod                    
    ch=f.read()                                                 #contents files are copied to string ch
    print("the file contents are as follows:")
    print(ch)                                                   #string ch is printed
    f.close()                                                   #closing of file
except FileNotFoundError:                                       #type of exception/error
    print("error occured!!!!")                                  #error message
finally:
    print("this file either does not exist or the the text file and python file are not in the same folder!!!")
