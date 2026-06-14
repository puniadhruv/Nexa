
class Calculator:
    def __init__(self):
        self.memory = 0

    def add(self, num):
        self.memory += num
        return self.memory

    def subtract(self, num):
        self.memory -= num
        return self.memory

    def multiply(self, num):
        self.memory *= num
        return self.memory

    def divide(self, num):
        if num == 0:
            raise ValueError("Cannot divide by zero")
        self.memory /= num
        return self.memory

    def clear(self):
        self.memory = 0
        return self.memory

if __name__ == "__main__":
    calc = Calculator()
    print("Initial memory: ", calc.clear())

    for operation, number in [('+', 5), ('-', 3), ('*', 2), ('/', 4)]:
        getattr(calc, operation)(number)
        print(f"After {operation}ing by {number}: ", calc.memory)
