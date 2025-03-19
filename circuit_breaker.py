from switch import Switch
class CircuirBreaker(Switch):
    def __init__(self, breaker_type):
        super().__init__()
        self.type = breaker_type