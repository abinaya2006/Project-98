def swapFileData ():
    file1Name=input("Enter the name of the first file: ")
    file2Name=input("Enter the name of the second file: ")

    # Code to read the data.

    with open(file1Name,'r') as a:
        data_a=a.read()


    with open(file2Name,'r') as b:
        data_b=b.read()
    
    
    # Code to write the data to different files.
    with open(file1Name,'w') as a:
        a.write(data_b)
    
    with open(file2Name,'w') as b:
        b.write(data_a)




swapFileData()