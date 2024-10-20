def list_roman_emperors(*args, **kwargs):
    emperors_good = {}
    emperors_bad = {}
    for arg in args:
        emperor_name, success_status = arg
        if success_status is True:
            emperors_good.setdefault(emperor_name, []).append(success_status)
        else:
            emperors_bad.setdefault(emperor_name, []).append(success_status)


    for emperor_name, rule_length in kwargs.items():
        if emperor_name in emperors_good:
            emperors_good[emperor_name].append(rule_length)
        else:
            emperors_bad[emperor_name].append(rule_length)

    sorted_good = dict(sorted(emperors_good.items(), key=lambda x: (-x[1][1], x[0])))
    sorted_bad = dict(sorted(emperors_bad.items(), key=lambda x: (x[1][1], x[0])))

    result = ''

    result += f"Total number of emperors: {len(emperors_good) + len(emperors_bad)}\n"

    if emperors_good:
        result += "Successful emperors:\n"
        for emperor, info in sorted_good.items():
            result += f"****{emperor}: {info[1]}\n"

    if emperors_bad:
        result += "Unsuccessful emperors:\n"
        for emperor, info in sorted_bad.items():
            result += f"****{emperor}: {info[1]}\n"

    return result


print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Claudius", True), Augustus=40, Trajan=19, Claudius=13,))