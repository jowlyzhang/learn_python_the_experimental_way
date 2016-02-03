#!/usr/bin/python
import pdb

class Event(object):
    events = []

    def __init__(self, action, time):
        self.action = action
        self.time = time
        Event.events.append(self)

    def __cmp__(self, other):
        return cmp(self.time, other.time)

    def run(self):
        print"%.2f: %s".format(self.time, self.action)

    @staticmethod
    def run_events():
        Event.events.sort()
        for e in Event.events:
            e.run()


def create_mc(description):
    class_name = "".join(x.capitalize() for x in description.split())
    def __init__(self, time):
        Event.__init__(self, description + " [mc]", time)

    globals()[class_name] = type(class_name, (Event,), dict(__init__=__init__))


def create_exec(description):
    class_name = "".join(x.capitalize() for x in description.split())
    klass = """
class %s(Event):
    def __init__(self, time):
        Event.__init__(self, "%s [exc]", time)
    """ % (class_name, description)
    exec klass in globals()


if __name__ == '__main__':
    descriptions = [
        'Light On',
        'Light Off',
        'Water On',
        'Water Off',
        'Thermostat night',
        'Thermostat day',
        'Ring bell',
    ]
    initializations = "ThermostatNight(5.00); LightOff(2.00);\
        WaterOn(3.30); WaterOff(4.45); LightOn(1.00);\
        RingBell(7.00); ThermostatDay(6.00)"

    pdb.set_trace()
    # Create a class for each description that inherites from class
    # `Event` and add it to the global namespace
    [create_mc(dsc) for dsc in descriptions]
    exec initializations in globals()
    [create_exec(dsc) for dsc in descriptions]
    exec initializations in globals()
    Event.run_events()

