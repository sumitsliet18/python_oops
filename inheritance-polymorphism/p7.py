class Customer:
    def __init__(self, name, new_bal):
        self.name = name
        if new_bal < 0:
            raise ValueError("Invalid balance!")
        self._balance = new_bal

        # Add a decorated balance() method returning _balance

    @property
    def balance(self):
        return self._balance

    # Add a setter balance() method
    @balance.setter
    def balance(self, new_bal):
        # Validate the parameter value
        if new_bal < 0:
            raise ValueError("Invalid balance!")
        self._balance = new_bal

        # Print "Setter method is called"
        print("Setter method is called")