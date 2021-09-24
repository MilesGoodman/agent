import random
import time


class McClean():
    """Representation of the cleaning robot."""

    def __init__(self, akku = 100):
        self.akku = akku

    def empty_trashbin(self, office):
        print(f"Emptying trash bin in {office.name}")
        office.trashbin = True
        self.akku -= 5

    def clean_window(self, office):
        print(f"Cleaning window in {office.name}")
        office.window = True
        self.akku -= 5

    def clean_desk(self, office):
        print(f"Cleaning desk in {office.name}")
        office.desk = True
        self.akku -= 5

    def clean_floor(self, office):
        print(f"Cleaning floor in {office.name}")
        office.floor = True
        self.akku -= 5

    def go_to_office(self, office):
        print(f"Going to office {office}.")
        self.akku -= 10

    def recharge(self):
        self.akku -= 10
        print(f"Recharging from {self.akku}%...")
        while self.akku < 100:
            time.sleep(0.01)
            self.akku += 1
            if self.akku % 10 == 0:
                print(f"Recharged to {self.akku}%.")

    def check_akku(self):
        if self.akku <= 15:
            self.recharge()

    def do(self, offices):
        """Entry function, to be called when the robot should perform its routine."""
        for office in offices:
            print()
            self.check_akku()
            self.go_to_office(office.name)
            self.check_akku()
            if not office.trashbin:
                self.empty_trashbin(office)
            self.check_akku()
            if not office.window:
                self.clean_window(office)
            self.check_akku()
            if not office.desk:
                self.clean_desk(office)
            self.check_akku()
            if not office.floor:
                self.clean_floor(office)


class Office():
    """Representation of an office."""

    def __init__(self, name, trashbin, window, desk, floor):
        self.name = name
        self.trashbin = trashbin
        self.window = window
        self.desk = desk
        self.floor = floor

    def __repr__(self):
        # return a string with information about this office
        str = (f"Office {self.name}: "
            f"trashbin: {self.trashbin}, "
            f"window: {self.window}, "
            f"desk: {self.desk}, "
            f"floor: {self.floor}")
        return str


def main():
    print("\n== McClean ==\n")

    offices = init_offices(10)

    print("Initial state of offices:")
    for office in offices:
        print(office)

    mcclean = McClean()
    mcclean.do(offices)

    print("\n\nState of offices after cleaning:")
    for office in offices:
        print(office)

    print("\nEnd.\n")


def init_offices(number_of_offices):
    """Return a list containing the specified number of new offices.

    Their properties are randomized.
    """

    offices = [] # list of the new offices
    for i in range(number_of_offices):
        offices.append(Office(
            str(i),
            bool(random.randint(0, 1)), # generate 0 or 1 and cast it to False/True
            bool(random.randint(0, 1)),
            bool(random.randint(0, 1)),
            bool(random.randint(0, 1))
        ))
    return offices


if __name__ == '__main__':
    main()
