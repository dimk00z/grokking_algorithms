def create_ordered_list(start: int = 0,
                        step: int = 1,
                        end: int = 100):
    return [number+1 for number in range(start, end, step)]
