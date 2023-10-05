import math
import os

def clear_screen(): # clears the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(): # prints the header
    print('-' * 30)
    print('Arma 3 real range calculator')
    print('-' * 30)

def get_laser_designator_info(): # returns your laser designator range, elevation and the true distance between you and your target
    range_input = input('Range: ').replace(',', '.')
    elevation_input = input('Elevation: ').replace(',', '.')
    try: 
        range_input = float(range_input)
        elevation_input = float(elevation_input)
    except:
        raise ValueError('You have to type only numbers for your distance and elevation.')
   
    cosine_degrees = elevation_input * (math.pi / 180)
    real_distance = round(range_input * math.cos(cosine_degrees))
   
    return range_input, real_distance, elevation_input

def find_closest_zeroing(real_distance, zeroing_options): # finds the right closest to main cross zeroing
    closest_zero = min(zeroing_options, key=lambda x: abs(x - real_distance))
    return closest_zero

def find_dot_amount(real_distance, dot_distances): # get how many dots you have to consider
    closest_zero_dot = min(dot_distances.keys(), key=lambda x: abs(x - real_distance))
    return dot_distances[closest_zero_dot]

def main():
    zeroing_options = [
        300, 400, 500, 600, 700, 800, 900, 1000,
        1100, 1200, 1300, 1400, 1500, 1600, 1700,
        1800, 1900, 2000, 2100, 2200
    ]

    dot_distances = {
        300: 100, 400: 94, 500: 88, 600: 82, 700: 77,
        800: 72, 900: 68, 1000: 64, 1100: 60, 1200: 56,
        1300: 53, 1400: 50, 1500: 47, 1600: 44, 1700: 41,
        1800: 39, 1900: 36, 2000: 34, 2100: 32, 2200: 30
    }

    while True:
        print_header()
        range_input, real_distance, elevation_input = get_laser_designator_info()
        closest_zero = find_closest_zeroing(real_distance, zeroing_options)
        dot_value = find_dot_amount(real_distance, dot_distances)
        qty_dot = round((real_distance - closest_zero) / dot_value, 1)

        clear_screen()
        print('-' * 30)
        print(f'Laser designator range: {round(range_input)}')
        print(f'Elevation: {elevation_input}')
        print(f'Real range: {real_distance}')
        print(f'Zeroing: {closest_zero}')
        print(f'Each mil dot range: {dot_value}m')
        print(f'Dots: {qty_dot} dots')

if __name__ == "__main__":
    main()