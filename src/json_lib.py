import json

def to_json_sorted(text):
    """
    Converts text to sorted(alphabetically on the attribute names) json value
    :param text:
                text to be converted to json
    :return:
            sorted json value
    """
    json_value = json.dumps(json.loads(text), sort_keys=True, indent=0)
    return json_value


def to_json(text):
    """
    Converts text to non sorted json value
    :param text:
                text to be converted to json
    :return:
            non sorted json value
    """
    json_value = json.dumps(json.loads(text), indent=0)
    return json_value
