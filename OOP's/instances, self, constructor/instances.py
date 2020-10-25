class Kettle(object):

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True

kenwood = Kettle("Kenwood",8.99)

hamilton = Kettle("Hamilton",14.55)

print("Models : {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make,
hamilton.price))

print("Models : {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

##############################################
""" play with  instances and methods"""
##############################################


print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(hamilton)
print(hamilton.on)
kenwood.switch_on()

print("*"*20)

kenwood.power = 1.5 ## It creates a attribute named power for kenwood object

print(kenwood.power)
print(hamilton.power) ##gives error as hamilton object not having power attribute
