'''
Programme designed to calculate total holiday cost including: flight, hotel and car-rental costs
'''

print("This Programme Will Calculate The Cost Of The Total Holiday Package Inclusive of Flight, Hotel and Car-Rental Costs.")

# User input request for destination city from selection of cities.
while True:
    city_flight = input("\nPlease choose from destinations : Paris, Rome, Amsterdam, Portugal : ").lower()
    valid_cities = ['paris', 'rome', 'amsterdam', 'portugal']

    if city_flight not in valid_cities:
        print("Invalid entry. Please choose from cities: Paris, Rome, Amsterdam, Portugal.")
        continue
    
    else:
        break
    
print(f"\nDestination city : {(city_flight).upper()}")

# User input request for number of nights stay at hotel.
while True:
    try: 
        num_nights = int(input("\nEnter number of nights stay at hotel: "))
    except ValueError:
        print("\nInvalid entry. Please choose a valid number.")
        continue
    else:
        break


# User input request for days of car rental.
while True:
    try:
        rental_days = int(input("\nEnter number of days required for car hire: "))
    except ValueError:
        print("\nInvalid entry. Please choose a valid number.")
        continue
    else:
        break
    
# Defining and calculating hotel cost for number of nights x cost per night based on city
def hotel_cost(num_nights):
    while True:
        if city_flight == "paris":
            price_per_night1 = 90
            return int(num_nights * price_per_night1)

        elif city_flight == "rome":
            price_per_night2 = 80
            return int(num_nights * price_per_night2)
            
        elif city_flight == "amsterdam": 
            price_per_night3 = 40
            return int(num_nights * price_per_night3)

        elif city_flight == "portugal": 
            price_per_night4 = 50
            return int(num_nights * price_per_night4)

        else:
            print("\nInvalid entry. Please choose again.")
            break
        
calc_hotel_cost = hotel_cost(num_nights)
print(f"\nTotal hotel cost for {num_nights} nights: £{calc_hotel_cost}")

# Defining and recalling cost of flight based on city input by user
def plane_cost(city_flight):
    while True:
        if city_flight == "paris":
            pl_cost_1 = 200
            return pl_cost_1 

        elif city_flight == "rome": 
            pl_cost_2 = 300
            return pl_cost_2
            
        elif city_flight == "amsterdam": 
            pl_cost_3 = 150
            return pl_cost_3

        elif city_flight == "portugal": 
            pl_cost_4 = 125
            return pl_cost_4

        else:
            print("\nInvalid entry. Please choose again.")
            break

plane_cost_recall = plane_cost(city_flight)
print(f"\nCost of flight to {city_flight}: £{plane_cost_recall}")

# Defining and calculating car-rental cost for number of days enterd by user
# Car rental cost = rental days x daily rent rate in city
def car_rental(rental_days):
    while True:
        if city_flight == "paris":
            daily_rent1 = 40
            return daily_rent1 * rental_days

        elif city_flight == "rome": 
            daily_rent1 = 35
            return daily_rent1 * rental_days
            
        elif city_flight == "amsterdam": 
            daily_rent1 = 25
            return daily_rent1 * rental_days

        elif city_flight == "portugal": 
            daily_rent1 = 20
            return daily_rent1 * rental_days
        
        else:
            print("\nInvalid entry. Please choose again.")
            break

calc_car_rental = car_rental(rental_days)
print(f"\nTotal car-rental cost for {rental_days} days is: £{calc_car_rental}")

# Defining and calculating total holiday cost by recalling and adding the values 
# from the defined functions.
def holiday_cost(hotel_cost, plane_cost, car_rental):
    calc_hotel_cost = hotel_cost(num_nights)
    plane_cost_recall = plane_cost(city_flight)
    calc_car_rental = car_rental(rental_days)
    return (calc_hotel_cost + plane_cost_recall + calc_car_rental)

total_holiday_cost = holiday_cost(hotel_cost, plane_cost, car_rental)
print(f"\nTHE TOTAL HOLIDAY COST for {num_nights} nights stay in {(city_flight).upper()} \
inclusive of hotel, flight and car-rental: £{total_holiday_cost}")
