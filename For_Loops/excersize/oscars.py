name = input()
academy_points = float(input())
appraisers = int(input())
final_score = academy_points

for _ in range(appraisers):
    appraiser_name = input()
    points = float(input())
    final_score += len(appraiser_name) * points / 2
    if final_score > 1250.5:
        print(f'Congratulations, {name} got a nominee for leading role with {final_score:.1f}!')
        exit()

print(f'Sorry, {name} you need {1250.5 - final_score:.1f} more!')
