numberlist = [10,20,50,60,30,40,70,80,100,90]
#finding the index of a number
numberlist = sorted(numberlist)
#print(numberlist)
find = input("enter number to find")
j = len(numberlist)
i=0
while i<j:
    #find middle number
    try:
        imiddleposition = (i+j)/2
        #print(imiddleposition)
        if int(find) == numberlist[int(imiddleposition)]:
            print(f"position {int(imiddleposition)}")
            break
        elif int(find) > numberlist[int(imiddleposition)]:
            i = int(imiddleposition)+1
            #print(f"number is on right side. middle position: {imiddleposition} i value: {i}")
            if j-1==1 & int(find) == numberlist[j]:
                print(f"position {j}")
            else:
                print("number not found")
        else:
            j = int(imiddleposition)-1
            #print(f"number is on left side. middle position: {imiddleposition} j value: {j} i value: {i}")
            #print(numberlist[int(imiddleposition)])
            if j-1==1 & int(find) == numberlist[i]:
                print(f"position {i}")
            else:
                print("number not found")
    except:
        print("")
    finally:
        print("")