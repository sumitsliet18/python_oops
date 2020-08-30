# MODIFY the function to catch exceptions
def invert_at_index(x, ind):
    try:
        return 1 / x[ind]
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except IndexError:
        print("Index out of range!")


a = [5, 6, 0, 7]

# Works okay
print(invert_at_index(a, 1))

# Potential ZeroDivisionError
print(invert_at_index(a, 2))

# Potential IndexError
print(invert_at_index(a, 5))

# Define SalaryError inherited from ValueError
class SalaryError(ValueError): pass

# Define BonusError inherited from SalaryError
class BonusError(SalaryError): pass


class SalaryError(ValueError): pass


class BonusError(SalaryError): pass


class Employee:
    MIN_SALARY = 30000
    MAX_BONUS = 5000

    def __init__(self, name, salary=30000):
        self.name = name
        if salary < Employee.MIN_SALARY:
            raise SalaryError("Salary is too low!")
        self.salary = salary

    # Rewrite using exceptions
    def give_bonus(self, amount):
        if amount > Employee.MAX_BONUS:
            raise BonusError("The bonus amount is too high!")

        if self.salary + amount < Employee.MIN_SALARY:
            raise SalaryError("The salary after bonus is too low!")

        self.salary += amount

