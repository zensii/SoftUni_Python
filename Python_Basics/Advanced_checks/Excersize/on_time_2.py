
hour_exam = int(input())
min_exam: int = int(input())
hour_arrive = int(input())
min_arrive = int(input())

delay_min = 0
delay_hour = 0
earlier_min = 0
earlier_hour = 0

if hour_exam == 0:
    hour_exam = 24
if hour_arrive == 0:
    hour_arrive = 24

if hour_exam < hour_arrive:
    print('Late')
    if min_exam > min_arrive:
        delay_hour = hour_arrive - hour_exam - 1
        delay_min = 60 - min_exam + min_arrive
        if delay_hour >= 1:
            if delay_min >= 10:
                print(f'{delay_hour}:{delay_min} hours after the start')
            else:
                print(f'{delay_hour}:0{delay_min} hours after the start')
        else:
            print(f'{delay_min} minutes after the start')
    elif min_exam < min_arrive:
        delay_hour = hour_arrive - hour_exam
        delay_min = min_arrive - min_exam
        if delay_hour >= 1:
            if delay_min >= 10:
                print(f'{delay_hour}:{delay_min} hours after the start')
            else:
                print(f'{delay_hour}:0{delay_min} hours after the start')
        else:
            print(f'{delay_min} minutes after the start')
    else:
        delay_hour = hour_arrive - hour_exam
        print(f'{delay_hour}:00 hours after the start')

elif hour_exam == hour_arrive:
    if min_exam < min_arrive:
        delay_min = min_arrive - min_exam
        print('Late')
        print(f'{delay_min} minutes after the start')
    elif min_exam == min_arrive:
        print("On time")
    else:
        if min_exam - min_arrive <= 30:
            earlier_min = min_exam - min_arrive
            print('On time')
            print(f'{earlier_min} minutes before the start')
        else:
            print("Early")
            print(f'{earlier_min} minutes before the start')

elif hour_exam > hour_arrive:
    if min_exam >= min_arrive:
        print('Early')
        earlier_hour = hour_exam - hour_arrive
        earlier_min = min_exam - min_arrive
        if earlier_min >= 10:
            print(f'{earlier_hour}:{earlier_min} hours before the start')
        else:
            print(f'{earlier_hour}:0{earlier_min} hours before the start')
    else:
        earlier_hour = hour_exam - hour_arrive - 1
        earlier_min = 60 - min_arrive + min_exam
        if earlier_hour >= 1:
            print('Early')
            if earlier_min >= 10:
                print(f'{earlier_hour}:{earlier_min} hours before the start')
            else:
                print(f'{earlier_hour}:0{earlier_min} hours before the start')
        else:
            if earlier_min <= 30:
                print('On time')
                print(f'{earlier_min} minutes before the start')
            else:
                print('Early')
                print(f'{earlier_min} minutes before the start')
