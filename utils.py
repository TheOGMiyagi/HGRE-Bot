import xdice
import json

def roll_raw(pattern):
    try:
        xdice_pattern = xdice.Pattern(pattern)
    except ValueError:
        return -1
    return xdice_pattern.roll()


# def getJSON(File, OutputDict: str)
    # with open(File) as f
        # OutputDict = json.load(f)

