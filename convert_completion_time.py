

def convert_completion_time(time_to_complete: str) -> int:
    normalized_string = time_to_complete.replace("½", ".5")
    return float(normalized_string)
