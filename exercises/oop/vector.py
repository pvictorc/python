class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self.coords = [0] * d

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self.coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self.coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self.coords[j] = val

    def add(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):  # relies on len method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))  # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self.coords == other.coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other  # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return "<" + str(self.coords)[1:-1] + ">"

    def __sub__(self, other):
        """Return difference of two vectors."""
        length_vec = len(self)
        if length_vec != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(length_vec)
        for i in range(length_vec):
            result[i] = self[i] - other[i]
        return result


def main():
    """Main function to demonstrate the Vector class."""
    u = Vector(3)
    v = Vector(3)
    u[0] = 1
    u[1] = 2
    u[2] = 3
    v[0] = 4
    v[1] = 5
    v[2] = 6

    print("Vector u:", u)
    print("Vector v:", v)

    print("Sum of vectors:", u.add(v))
    print("Difference of vectors:", u - v)


if __name__ == "__main__":
    main()