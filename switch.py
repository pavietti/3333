class Switch:
    switch_count = 0
    switch_count +=1
    def __init__(self):
        self.name = ""
        self.position = 0
    def turn(self, new_position):
        self.position = new_position