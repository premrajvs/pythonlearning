class elements:
    def __init__(self,value=None,nextelement=None):
        self.value = value
        self.nextelement = nextelement

# e1 = elements(100) if i add this element and pass it to CustomLinkedList Class, it will show value of 100 and None
#cl1 = customLinkedList(e1)
#print(f"element is {e1.value} and next element is {e1.nextelement}")

class customLinkedList():
    def __init__(self,element=None):
        # I am creating an empty element with None value and None next element
        # I am storing it in a separate variable so that I can refernce it later when i print
        self.head = elements()

    def printcustomlinkedlist(self):
        element = self.head
        if element is None:
            print(f"Element: {element.value} NextElement: {element.nextelement}")
            return
        print(element.value)
        #print(element.nextelement)
        while element is not None:
            element = element.nextelement
            if element is not None:
                print(element.value)
                #print(element.nextelement)

    def insetelement(self,*values):
        for item in values:
            newelement = elements(item)
            if self.head.value is None:
                self.element = newelement
                self.head = newelement
            else:
                print(f"previous value: {self.element.value}")
                self.element.nextelement = newelement
                self.element = newelement
                print(f"new current element value: {self.element.value}")

    def deleteelement(self,value):
        todelete = elements(value)
        self.element = self.head
        while True:         
            if self.head.value is None:
                print("List is empty")
                return
            elif self.element is None:
                print("value do not exist")
                return
            else:
                if self.element.value == self.head.value and self.element.nextelement == self.head.nextelement:
                    #this is the first element. So, it does not have any previous elements.
                    #we only have to delete this element and move head to next element
                    if self.element.value == todelete.value:
                        self.head = self.element.nextelement
                        self.element = None
                        self.element = self.head
                        return
                    #this is the first element and it is not equal to the element to be deleted.
                    #so, assigning this to a temp previous element
                    else:
                        self.previouslement = self.element
                        self.element = self.element.nextelement
                else:
                    #check if current value is equal to element to be deleted in a loop
                    # if yes, change previous element next element to this element
                    if todelete.value == self.element.value:
                        self.previouslement.nextelement = self.element.nextelement
                        self.element.value = None
                        self.element.nextelement = None
                        break
                    else:
                        self.element = self.element.nextelement

cl1 = customLinkedList()
cl1.printcustomlinkedlist()
cl1.insetelement(3,4,5)
#cl1.insetelement(6)
#cl1.printcustomlinkedlist()
#cl1.addelement(1)
cl1.deleteelement(7)
cl1.printcustomlinkedlist()

"""
This is another way of implementing but it users inheritance. 
If i inherit elements class in CustomLinkedList Class, it will mean that CustomLinkedList Class is a type of elements class
This is wrong. So, we should not implement it via inheritance.

class customLinkedList(elements):
    def __init__(self,element=None):
        super().__init__(element)
        self.element = element

    def printcustomlinkedlist(self):
        element = self.element
        print(f"Element: {element.value} NextElement: {element.nextelement}")

e1 = elements(100)
cl1 = customLinkedList(e1)

cl1.printcustomlinkedlist()
 """