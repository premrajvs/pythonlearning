numberlist = [10,20,50,60,30,40,70,80,100,90]
#finding the index of a number
numberlist = sorted(numberlist)
print(numberlist)
find = input("enter number to insert")
find = int(find)
j = len(numberlist)
i=0
while i<j:
    #find middle number
    try:
        imiddleposition = int((i+j)/2)
        #print(imiddleposition)
        if find == numberlist[imiddleposition]:
            print(f"position {imiddleposition}")
            numberlist.insert(imiddleposition,find)
            break
        elif find > numberlist[imiddleposition]:
            i = imiddleposition
            #print(f"number is on right side. middle position: {imiddleposition} i value: {i}")
            if i+1==j and find <= numberlist[i]:
                numberlist.insert(i,find)
                break
            elif i+1==j and find > numberlist[i]:
                numberlist.insert(i+1,find)
                break
        else:
            j = imiddleposition
            #print(f"number is on left side. middle position: {imiddleposition} j value: {j} i value: {i}")
            #print(numberlist[int(imiddleposition)])
            if i+1==j and find <= numberlist[i]:
                numberlist.insert(i,find)
                break
            elif i+1==j and find > numberlist[i]:
                numberlist.insert(i+1,find)
                break
    except:
        print("")

print(numberlist)
