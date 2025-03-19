from circuit_breaker import CircuirBreaker
from switch import Switch


if __name__ == "__main2__":
    sw1 = Switch()
    Switch.switch_count = 3
    sw1.name = "Q1"
    sw1.position = 1
    sw1.switch_count = 5
    print(sw1)   
    sw2=Switch()
    print(sw2)
    sw3=sw2
    CB1 = CircuirBreaker()
    CB1.turn(1)
pass