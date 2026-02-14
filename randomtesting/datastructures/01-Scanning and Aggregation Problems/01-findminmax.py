""" #Common Mistakes

 In Python you use self in a function only when the function is declared inside a class because self makes it a instance method.
 if outside a class, it is just another variable.

 Second mistake with function, if a function is inside a class, it is mandatory to have a variable called self as first arg.

 When you want to call a class, you do not need new operator. In python calling a class is same as calling a function.
 Second, when you just say fi=findminmax, you are not creating a new object. you are renaming the class findminmax. like changing the name of the blueprint. Instead you should use () next to class name. now it creates object

 In Java you can have multiple classes and functions and then declare void main function in on class and it automatically becomes the entry point. But python runs top down. So, it does not work that way. When you import the python class in another class in a big project, you dont have to worry about what gets called when because code logic takes care of that. But if you want to run a file directly, use __name__ == "__main__". Python knows to run this automatically.
 """
class findminmax:
    def checkalllinearly(self,arrayofnumber):
        if not isinstance(arrayofnumber,(list)):
            return TypeError
        if len(arrayofnumber)<1:
            return None,None
        minimum = arrayofnumber[0]
        maximum = arrayofnumber[0]
        for number in arrayofnumber:
            if minimum>number:
                minimum=number
            if maximum<number:
                maximum=number
        return minimum,maximum

class callingclass:
    def method1(self):
        #do nothing
        print()

    def main(self,args):
        fi = findminmax()
        #data=[]
        data = [1,3,5,2,4,6]
        print(fi.checkalllinearly(data))

if __name__ == "__main__":
    c1 = callingclass()
    c1.main(None)
