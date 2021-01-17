def convert_completion_time(time_to_complete: str) -> int:
    """Convert string containing a ½ character into a float."""
    normalized_string = time_to_complete.replace("½", ".5")
    return float(normalized_string)
