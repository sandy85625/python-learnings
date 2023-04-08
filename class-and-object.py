
"""
1. Create a class complex to represent complex numbers
2. Define two functions to 

a) add two complex numbers

b) multiply two complex numbers
Illustrate complex number addition and multiplication

It implement functions:
- __add__ which is mathematical '+' operator. Eg: logic is same as: z1 + z2
- __mul__ which is mathematical '*' operator. Eg: logic is same as: z1 * z2

"""

class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {-self.imag}i"

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + self.imag * other.real)




print("==============================")
print("Class and Objects: Addition and Product of two Complex number")

# Create two complex numbers
z1 = Complex(2, 3)
z2 = Complex(4, -5)
print(f"\nGiven two complex numbers is: {z1}, {z2}")

# Add the two complex numbers
print("\nAdding two complex numbers, z1 + z2 gives: ")
z_sum = z1 + z2
print(f"Sum: {z_sum}")

# Multiply the two complex numbers
print("\nProducts of two complex numbers, z1 * z2 gives: ")
z_prod = z1 * z2
print(f"Product: {z_prod}")
