def allcaps(func):
    def inside():
        result = func()
        return result.upper()
    return inside
