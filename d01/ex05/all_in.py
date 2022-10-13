import sys

def state(city_capitals):
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
    for city_cap in city_capitals.split(','):
        city_cap = city_cap.strip().lower()
        if city_cap.isalnum():
            capital_key = next((city[0] for city in capital_cities.items() if city[1].lower() == city_cap), None)
            state_key = next((state[1] for state in states.items() if state[0].lower() == city_cap), None)
            if capital_key:
                state = next((state[0] for state in states.items() if state[1] == capital_key), None)
                print(f'{capital_cities[capital_key]} is the capital of {state}')
            elif state_key:
                state = next((state[0] for state in states.items() if state[1] == state_key), None)
                print(f'{capital_cities[state_key]} is the capital of {state}')
            else:
                print(f'{city_cap} is neither a capital city nor a state')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        state(sys.argv[1])