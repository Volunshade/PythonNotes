"""Module containing notes on Python classes."""


class Number:
    """Representation of a pseudo integer."""

    def __init__(self, number):
        """Initialize a Number type instance."""

        self.number = number

    def __str__(self):
        """String representation of a Number type instance."""

        return str(self.number)

    def __int__(self):
        """Integer representation of a Number type instance."""

        return self.number

    def __add__(self, other):
        """Addition operator representation of a Number type instance."""

        if isinstance(other, int):
            return self.number + other
        else:
            return self.number + other.number


def testing_number():
    """Execute Number class tests."""

    # x = 5  # int  <-  is a class 'int'
    # y = 10

    x = Number(5)
    y = Number(10)

    # x.display()
    # y.display()
    # print(x + y)

    # print(x)
    # print(y)

    # print(str(x))
    # print(int(x))

    # print(int(x) + int(y))

    print(x + y)
    print(x + 500)


class Human:
    """Represention of a human being."""

    def __init__(self, name: str) -> None:
        """Instantiate a Human type instance."""

        self.name = name

    def __str__(self) -> str:
        """String representation of a Human type instance."""

        return self.name

    def say_hobby(self, hobby: str):
        """Display Human instance hobby."""

        print(f"I am {self.name}, my hobby is {hobby}.")


def main():
    """Execute the main process."""

    adam = Human("Adam")
    tom = Human("Tom")

    tom.say_hobby("reading")
    adam.say_hobby("programming")


if __name__ == "__main__":
    main()
