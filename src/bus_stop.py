# Create a new class called BusStop. This should have a name attribute.
# Add an attribute to the BusStop called 'queue'. This should be an empty list that will get filled with instances of the Person class.
# Add a method that adds a person to the queue.

class BusStop:
    def __init__(self, name):
        self.name = name
        self.queue = []

# return the length of the queue
    def queue_length(self):
        return len(self.queue)

# add a person to the queue
    def add_to_queue(self, person):
        self.queue.append(person)


# clear / empty the queue
    def clear(self):
        self.queue.clear()