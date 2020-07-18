fname = raw_input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0
lst=list()
for line in fh:
    line.rstrip()
    if line:
        lst=line.split()
        #print('LINE',line)
        if len(lst)>1:
            if lst[0] == 'From':
                print(lst[1])
                count=count+1
print("There were", count, "lines in the file with From as the first word")
