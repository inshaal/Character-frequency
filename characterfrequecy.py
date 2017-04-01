#[By INS] Frequency of occurence of character in a string
x=raw_input("Enter string : ")
n=raw_input("Enter character : ")
i,l=0,0
for i in range(0,len(x)):
    if x[i]==n:
        l +=1
    else:
        continue
i +=1
print "The frequency of occurence of that character is ",l

