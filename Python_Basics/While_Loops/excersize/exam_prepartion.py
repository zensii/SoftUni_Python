low_scores = int(input())
counter_low_score = 0
last_problem = ""
total_score = 0
num_of_problems = 0

while True:
    problem = input()

    if problem == 'Enough':
        print(f'Average score: {total_score / num_of_problems:.2f}')
        print(f'Number of problems: {num_of_problems}')
        print(f'Last problem: {last_problem}')
        break
    else:
        score = int(input())
        if score <= 4:
            counter_low_score += 1
            if counter_low_score >= low_scores:
                print(f'You need a break, {counter_low_score} poor grades.')
                break
        last_problem = problem
        total_score += score
        num_of_problems += 1
