score = 0
def main():
    '''This program is an implementation of the Rosenberg
       Self-Esteem Scale. This program will show you ten
       statements that you could possibly apply to yourself.
       Please rate how much you agree with each of the
       statements by responding with one of these four letters:

       D means you strongly disagree with the statement.
       d means you disagree with the statement.
       a means you agree with the statement.
       A means you strongly agree with the statement.'''

    q1 = get_positive_answer(input('1. I feel that I am a person of worth, at least on an equalplane with others.Enter D, d, a, or A: '))
    q2 = get_positive_answer(input('2. I feel that I have a number of good qualities.Enter D, d, a, or A: '))
    q3 = get_negative_answer(input('3. All in all, I am inclined to feel that I am a failure.Enter D, d, a, or A: '))
    q4 = get_positive_answer(input('4. I am able to do things as well as most other people.Enter D, d, a, or A: '))
    q5 = get_negative_answer(input('5. I feel I do not have much to be proud of.Enter D, d, a, or A: '))
    q6 = get_positive_answer(input('6. I take a positive attitude toward myself.Enter D, d, a, or A: '))
    q7 = get_positive_answer(input('7. On the whole, I am satisfied with myself.Enter D, d, a, or A: '))
    q8 = get_negative_answer(input('8. I wish I could have more respect for myself.Enter D, d, a, or A: '))
    q9 = get_negative_answer(input('9. I certainly feel useless at times.Enter D, d, a, or A: '))
    q10 = get_negative_answer(input('10. At times I think I am no good at all.Enter D, d, a, or A: '))

    total_score = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10
    print(f'Your score is {total_score}')
    print(f'A score below 15 may indicate problematic low self-esteem.')
def get_positive_answer(answer):
    if answer == 'A':
        points = 3
    elif  answer == 'a':
        points = 2
    elif answer == 'd':
        points = 1
    else:  
        points = 0
        
    answer = points
    return answer
def get_negative_answer(negative_answer):
    if negative_answer == 'A':
        points = 0
    elif  negative_answer == 'a':
        points = 1
    elif negative_answer == 'd':
        points = 2
    else:  
        points = 3
        
    negative_answer = points
    return negative_answer


main()