
class InvalidRatingError(Exception):
    """Raised when the vehicle rating is not between 1 and 5"""
    pass

class NegativeDistanceError(Exception):
    """Raised when the ride distance is less than 0"""
    pass

class RideFileError(Exception):
    """Raised when there is an issue reading or writing the history file"""
    pass

