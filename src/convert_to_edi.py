import re


def convert_to_edi(filename):
    """
    Converts the file to edifact format file in same location
    :param filename:
                    filename with relative path
    :return:
            doesnot return but stores converted file in same location
    """
    input_file = open(filename, 'r')
    contents = input_file.read()
    contents = re.sub(r"\\\*", "convertingReleaseCharecter", contents)
    contents = re.sub(r"\\\+", "convertingReleaseCharecter1", contents)
    contents = re.sub(r"\\\:", "convertingReleaseCharecter2", contents)
    contents = re.sub(r"\*O", "", contents)
    contents = re.sub(r"''", "", contents)
    contents = re.sub(r"\+", "\x1d", contents)
    contents = re.sub(r":", "\x1f", contents)
    contents = re.sub(r"'&", "\x1c", contents)
    contents = re.sub(r"\*", "\x19", contents)
    contents = re.sub(r"\n", "", contents)
    contents = re.sub(r"\r", "", contents)
    contents = re.sub(r"\'", "\x1c", contents)
    contents = re.sub(r"convertingReleaseCharecter", "*", contents)
    contents = re.sub(r"convertingReleaseCharecter1", '+', contents)
    contents = re.sub(r"convertingReleaseCharecter2", ":", contents)

    output_file = open(filename.split(".")[0] + ".edi", "w")
    output_file.write(contents)
    input_file.close()
    output_file.close()
