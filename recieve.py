from time import sleep 

while True:
    file1 = open("file.txt", "r")
    lis = file1.read()
    a = lis.strip().split(',')
    print("The X Value: %s The Y Value: %s The Z Value: %s", {a[0], a[1], a[2]})
    sleep(0.1)
