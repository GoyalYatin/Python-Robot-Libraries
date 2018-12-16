import json_lib


def get_file_sorted_json(path):
    """
    get file from path and return sorted json
    :param path:
                file name and path
    :return:
            content in sorted json
    """
    expected = open(str(path), 'r')
    sorted_response = json_lib.to_json_sorted(expected.read())
    return sorted_response


def get_file_json(path):
    """
    get file from path and return json
    :param path:
                file name and path
    :return:
            content in json
    """
    expected = open(str(path), 'r')
    sorted_response = json_lib.to_json(expected.read())
    return sorted_response


def get_file_from_path(path):
    """
    get file from path and return string
    :param path:
                file name and path
    :return:
            content in string
    """
    expected = open(str(path), 'r')
    return expected.read()
