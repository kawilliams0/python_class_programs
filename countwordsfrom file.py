
# Wap to count the words in a file 
with open("content.txt",'r') as fobj:
    count=0
    for ele in fobj:
        count+=len(ele.split())
    print(count)

#Count Number of characters in the file 
with open("content.txt",'r') as fobj:
    sum=0
    for line in fobj:
        new_row=line.strip('\n')
        sum+=len(new_row)
    print(sum)
        
