class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        if b == 0:  
            return "Error: Division by zero"
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        return result
    
    def modulo(self, a, b):
        while a >= b:
            a = a-b
        return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(5, 2))
    print("Example: subtraction: ", calc.subtract(2, 3))
    print("Example: multiplication: ", calc.multiply(3, 7))
    print("Example: multiplication: ", calc.multiply(4, 2))
    print("Example: division: ", calc.divide(5, 2))
    print("Example: division: ", calc.divide(6, 2))
    print("Example: modulo: ", calc.modulo(5, 2))