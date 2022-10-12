import sys

def state(capital):
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
        }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
        }
    
    key = next((city[0] for city in capital_cities.items() if city[1] == capital), None)
    if key:
        key = next((state[0] for state in states.items() if state[1] == key), None)
        print(key)
    else:
        print('Unknown capital city')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        state(sys.argv[1])