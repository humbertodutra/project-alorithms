def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    count = 0
    if not permanence_period or not target_time:
        return None

    for period in permanence_period:

        start, end = period
        if not isinstance(start, int) or not isinstance(end, int):
            return None
        if start <= target_time <= end:
            count += 1
    return count
