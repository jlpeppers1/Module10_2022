
#use the class keyword
class MyFirstClass:
    #notice it is indented now......................................beginning of class

    #can create variables in the class
    PI = 3.1415926535

    #initialize class; notice keyword self. This is how we "build/initialize" the object
    def __init__(self, f_name, l_name):
        #notice double indent for part of the function, 1 for being part of the class and 1 for being part of the funct
        self.first_name = f_name #notice class variable on the left, passed in param on the right
        self.last_name = l_name

    #can define other functions
    def hello_world(self):
        print("hello world")

    #can define how the object "converts" to a string...notice this overrrides a method
    def __str__(self):
        return str(self.first_name) + " " + str(self.last_name)

    def __repr__(self):
        return "MyFirstClass(\"" +self.first_name + "\", \"" + self.last_name + "\")"

    #we stop indenting now to indicate..................................end of class


#driver code
if __name__ == "__main__":
    #create the object
    my_obj = MyFirstClass("john", "smith")

    #do methods from it
    my_obj.hello_world()

    #notice this calls the __str__ method
    print(str(my_obj))

    print(str(my_obj.PI))

    print(repr(my_obj))
