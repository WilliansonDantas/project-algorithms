def study_schedule(permanence_period, target_time):
    count = 0
    for left, right in permanence_period:
        if (
            not isinstance(right, int)
            or not isinstance(left, int)
            or not isinstance(target_time, int)
        ):
            return None
        if left <= target_time <= right:
            count += 1
    return count
