# import this

# _name     | private, for internal use
# __name    | namemangle, easy way to define a class internal attribute without collision with other inherited atribs
# __name__  | convention, reserved words from python, special methods
# _         | temp var

class Person: 
    def __init__(self, name): # dunder method
        self.name = name

def main():
    me = Person("Victor")   
    print (me.name)

if __name__ == "__main__":
    main()