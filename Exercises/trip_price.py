base_rate = 40
price_per_km = 10
total_trip = 0


def calculate_trip_price(distance_km):
    global total_trip
    total_trip += 1
    return float(base_rate + price_per_km * distance_km)

def main():
    while True:
        distance = input("Enter km: ")
        if not distance:
            print(f"{total_trip = }")
            break
        price = calculate_trip_price(int(distance))
        print(f"The cost of the trip for {distance} km - {price}")
if __name__ == '__main__':
    main()
