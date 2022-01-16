# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input('Please enter your gender (F/M): ')
    birthdate = input('Please enter your birthdate (YYYY-MM-DD): ')
    weight = float(input('Enter your weight in US pounds: '))

    height = float(input('Enter your height in US pounds: '))
    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index,
    # and basal_metabolic_rate functions as needed.
    years = compute_age(birthdate)
    lb_to_kg = kg_from_lb(weight)
    in_to_cm = cm_from_in(height)
    # MEN BODY MAX INDEX
    bmi = body_mass_index(weight, height)

    print(f'Years: {years} ')
    print(f'Weight (kg): {lb_to_kg:.1f}')
    print(f'Height (cm): {in_to_cm:.1f}')
    # MEN BODY MAX INDEX
    print(f'Body mass index: {bmi}')

    # Print the results for the user to see.
    pass


def compute_age(birth):
    """Compute and return a person's age in years.
    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
            (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    """
    lb_to_kg = lb * 0.45359237
    return lb_to_kg


def cm_from_in(inch):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """
    in_to_cm = inch * 2.54
    return in_to_cm


def body_mass_index(weight, height):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000*weight)/height**2
    return bmi


def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """
    return


# Call the main function so that
# this program will start executing.
main()
