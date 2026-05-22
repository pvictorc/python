# import this

# _name     | private, for internal use
# __name    | namemangle, easy way to define a class internal attribute without collision with other inherited atribs
# __name__  | convention, reserved words from python, special methods
# _         | temp var
_PI = 3.14

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return round(_PI * self.radius**2,2) 

def main():
    circle = Circle(3)
    print (circle.calculate_area())

if __name__ == "__main__":
    main()