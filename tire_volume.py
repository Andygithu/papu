from datetime import datetime
import math
width = float(input('Enter the width of the tire in mm (ex 205):'))
aspect_ratio = float(input('Enter the aspect ratio of the tire (ex 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (ex 15): '))

volume = (math.pi * width ** 2 * aspect_ratio *
          (width * aspect_ratio + 2540 * diameter))/10000000000

print(f'The approximate volume is {volume:.2f} liters.')


current_time = datetime.now()


with open('volumes.txt', 'at',) as dimens_file:
    print(f'{current_time:%Y-%m-%d}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}', file=dimens_file)


decision = input(
    'Do you wanna buy a tire with the dimensions entered?(YES/NO): ')
if decision.lower() == 'yes':
    phone = input('Please enter your phone number: ')
    with open('volumes.txt', 'at',) as dimens_file:
        print(f'Phone : {phone}', file=dimens_file)
# TO READ VOLUMES.TXT FILE.I DID LEARN THIS CODE FROM A VIDEO ON YOUTUBE.
    with open('volumes.txt', 'r') as f:
        f_content = f.read()
        print(f_content)
