def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    # raise NotImplementedError
    list = 0
    try:
        for index, hours in permanence_period:
            if index <= target_time <= hours:
                list += 1
        return list
    except TypeError:
        return None


#  if target_time <= 0 or not target_time:
#             return None
