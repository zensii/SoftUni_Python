record_time = float(input())
length = float(input())
one_meter_time = float(input())

#съпротивлението на водата го забавя на всеки 15 м. с 12.5 секунди. Когато се изчислява колко пъти Иванчо ще се забави,
# в резултат на съпротивлението на водата, резултатът трябва да се закръгли надолу до най-близкото цяло число.

water_resistance = length // 15 * 12.5

Ivan_time = length * one_meter_time + water_resistance
diff_record = record_time - Ivan_time

if Ivan_time >= record_time:
    print(f"No, he failed! He was {abs(diff_record):.2f} seconds slower.")

else:
    print(f" Yes, he succeeded! The new world record is {Ivan_time:.2f} seconds.")
