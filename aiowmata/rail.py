from .core import get_json


def get_predictions(station):
    return get_json("StationPrediction", "GetPrediction/{}".format(station), {})
