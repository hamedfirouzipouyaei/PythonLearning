class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device Name: {self.name!r}, Connection: {self.connected_by}"
    
    def disconnect(self):
        self.connected = False
        print("Disconncted")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_capacity = capacity

    def __str__(self):
        return f"{super().__str__()}, Capacity: {self.capacity}, Remaining Capacity: {self.remaining_capacity}"
    
    def print_document(self, pages):
        if not self.connected:
            print("Printer is not connected.")
            return
        print(f"Printing {pages} pages...")
        self.remaining_capacity -= pages



printer = Printer("Printer", "USB", 500)
printer.print_document(10)
print(printer)
printer.disconnect()