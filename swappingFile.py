def swapFileData():
    file1=input("write the file name : ")
    f=open("sample1.txt", 'r')
    read_file = f.read()
    print(read_file)
    read_file2 = b.read()
    print(read_file2)
    f2=open("sample2.txt", 'w')
    b.write(data_b)
    print(b)
    a.write(data_a)
    print(a)
    
swapFileData()
