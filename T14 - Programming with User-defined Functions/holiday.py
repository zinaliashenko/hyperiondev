# holiday.py

def hotel_cost(num_nights: int) -> float:
    nightly_rate = 330.20
    return abs(num_nights) * nightly_rate # added a number module in case the user accidentally enters a negative number


def plane_cost(city_flight: str) -> float:

    if city_flight.lower() == "kyiv":
        return 100.40
    elif city_flight.lower() == "paris":
        return 500.50
    elif city_flight.lower() == "tokyo":
        return 700.80
    else:
        raise ValueError(f"We do not have information for flights to {city_flight}.")


def car_rental(rental_days: int) -> float:
    daily_rental_cost = 30.20
    return abs(rental_days) * daily_rental_cost # added a number module in case the user accidentally enters a negative number


def holiday_cost(city_flight: str, num_nights: int, rental_days: int) -> float:      
    total_cost = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return total_cost


# user's inputs
city_flight = input("Enter the city you will be flying to Kyiv/Paris/Tokyo): ")
num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
rental_days = int(input("Enter the number of days for which you will be hiring a car: "))
 
# Calculate and print the details about the holiday
try:
    total_cost = round(holiday_cost(city_flight, num_nights, rental_days), 2)

    print("\nHoliday Details\n----------------")
    print(f"City Flight: {city_flight.capitalize()}")
    print(f"Number of Nights at Hotel: {abs(num_nights)}")
    print(f"Number of Days for Car Rental: {abs(rental_days)}")
    print(f"Total Holiday Cost: £{total_cost}")

except ValueError as error:
    print(error)
