import os, math
from datas import zeroing as zing

DASHES_LENGHT = 35

def clear_screen(): # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_screen(): # main menu provider
    print('-' * DASHES_LENGHT)
    print('Arma 3 Dot Calculator')
    print('-' * DASHES_LENGHT)

def laser_designator_infos(): # informations provided by your laser designator that gets you the real distance between you and your target
    while True:
        laser_range = input('Laser designator range: ').replace(',', '.')
        laser_elevation = input('Laser designator elevation: ').replace(',', '.')

        try:
            laser_range = float(laser_range)
            laser_elevation = float(laser_elevation)
            cosine_degrees = laser_elevation * (math.pi / 180)
            real_distance = math.cos(cosine_degrees) * laser_range

            return laser_range, laser_elevation, round(real_distance)
       
        except ValueError:
            clear_screen()
            print('Only numbers, please. Try again.')
            menu_screen()
   
        except Exception as error:
            clear_screen()
            print(f'Unknow error: {error}. Try again!')
            menu_screen()

def get_best_zeroing(real_distance, zeroing_options): # gets you the best zeroing option for your lrps scope
    return min(zeroing_options, key=lambda x: abs(x - real_distance))

def get_true_mil_dot_value(best_zeroing, dot_distances): # gets you the real value for each mildot from your best zeroing option
    return dot_distances[min(dot_distances.keys(), key=lambda x: abs(x - best_zeroing))]
         
def main(): # runs the program
    zeroing_options = zing.ZEROING_OPTIONS
    dot_distances = zing.DOT_DISTANCES

    while True:
        menu_screen()
        laser_range, laser_elevation, real_distance = laser_designator_infos()
        best_zeroing = get_best_zeroing(real_distance, zeroing_options)
        true_mil_dot = get_true_mil_dot_value(best_zeroing, dot_distances)
        scope_dots = round((real_distance - best_zeroing) / true_mil_dot, 2)
        clear_screen()

        print('-' * DASHES_LENGHT)
        print('Laser range:', round(laser_range), 'meters')
        print('Laser elevation:', laser_elevation, 'degrees')
        print('Real distance:', real_distance, 'meters')
        print('Best zeroing:', best_zeroing)
        print('Each mildot:', true_mil_dot, 'meters')
        print('Dots:', scope_dots, 'dots')

if __name__ == '__main__': # start the program
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print('Program stopped by the user.')
        exit(0)