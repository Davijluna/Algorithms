def study_schedule(permanence_period, target_time):
    list = 0
    try:
        for index, hours in permanence_period:
            if index <= target_time <= hours:
                list += 1
        return list
    except TypeError:
        return None
