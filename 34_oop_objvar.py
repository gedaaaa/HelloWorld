class Robot:
    """A robot with name."""
    # 建立一个类变量统计机器人数量
    population = 0

    def __init__(self, name):
        """Initialization."""
        self.name = name
        print("initalizing {}".format(self.name))
        # 创建机器人时人口+1
        Robot.population += 1

    def die(self):
        """Destroyed."""
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("there are {:d} robots left".format(Robot.population))

    def say_hi(self):
        """Greetings."""
        print("{} at service.".format(self.name))

    @classmethod
    def how_many(cls):
        print("we have {:d} robots".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some work here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()
