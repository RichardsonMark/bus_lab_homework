# TASK: Create a Bus class.
#The Bus should have a route number (e.g. 22) and a destination (e.g. "Ocean Terminal").
#The Bus should have a drive method that returns a string (e.g. "Brum brum").

class Bus:
    def __init__(self, route, destination):
        self.route_number = route
        self.destination = destination


# write a method to get the test count passing
    def drive(self):
        return "Brum brum"

