from math import sin, cos
from matplotlib import pyplot as plt
import random

# Represent a cannonball, tracking its position and velocity.


class Cannonball:
    # Create a new cannonball at the provided x position.
    #  @param x the x position of the ball

    def __init__(self, x):
        self._x = x
        self._y = 0
        self._vx = 0
        self._vy = 0

        # Compose Print_Iface here
        self.printer = Print_Iface()

    # Move the Cannonball, using its current velocities.
    # @param sec the amount of time that has elapsed.

    def move(self, sec, grav=9.81):
        dx = self._vx * sec
        dy = self._vy * sec

        self._vy = self._vy - grav * sec

        self._x = self._x + dx
        self._y = self._y + dy

    # Get the current x position of the ball.
    # @return the x position of the ball

    def getX(self):
        return self._x

    # Get the current y position of the ball.
    # @return the y position of the ball

    def getY(self):
        return self._y

    # Shoot the canon ball.
    # @param angle the angle of the cannon
    # @param velocity the initial velocity of the ball

    def shoot(self, angle, velocity, user_grav):
        self._vx = velocity * cos(angle)
        self._vy = velocity * sin(angle)
        self.move(0.1, user_grav)

        while self.getY() > 1e-14:

            # Use Print_Iface here
            self.printer.main_print(self.getX(), self.getY())
            self.move(0.1, user_grav)

# Add a new Crazyball class that inherits from Cannonball


class Crazyball(Cannonball):
    def move(self, sec, grav=9.81):
        super().move(sec, grav)
        if self.getX() < 400:
            rand_q = random.randrange(0, 10)
            print(f"random value: {rand_q}")

            # Adding randomness to x
            self._x += rand_q

            # Adding randomness to y
            self._y += rand_q

# Print_Iface class for printing and plotting


class Print_Iface:
    @staticmethod
    def main_print(x, y):
        print(f"The ball is at (%.1f, %.1f)" % (x, y))
        plt.scatter(x, y)
        plt.pause(0.1)


# Removed __main__ if function to allow continuous inputs for the Cannonball class using while loop

while True:

    # Demonstrate the cannonball class.
    # from cannonball import Cannonball
    a = float(input("Enter starting angle - try 45: "))
    v = float(input("Enter initial velocity - try 33: "))

    print("1 - Earth Gravity")
    print("2 - Moon Gravity")
    print("3 - Crazy Trajectory")
    print("4 - Quit")

    choice = input("Enter choice (1-4): ")

    if choice == "1":
        c = Cannonball(0)

        # Earth gravity
        c.shoot(a, v, 9.81)
    elif choice == "2":
        c = Cannonball(0)

        # Moon gravity
        c.shoot(a, v, 1.625)
    elif choice == "3":
        Crazyball = Crazyball(0)

        # Crazyball with randomness
        Crazyball.shoot(a, v, 9.81)
    elif choice == "4":
        print("goodbye")
        break

    else:
        print("Wrong Input, Try Again")
