# TASK: Create a Bus class.
#The Bus should have a route number (e.g. 22) and a destination (e.g. "Ocean Terminal").
#The Bus should have a drive method that returns a string (e.g. "Brum brum").

class Bus:
    def __init__(self, route, destination):
        self.route_number = route
        self.destination = destination
        self.passengers = []

# the bus goes Brum brum! (drives)
    def drive(self):
        return "Brum brum"

# return a count of the bus passengers
    def passenger_count(self):
        return len(self.passengers)