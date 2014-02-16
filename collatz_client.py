from json import dumps
from requests import get

SERVICE_URL = "http://localhost:5000"
DATA_PARAM = "data"

def get_json_input():
    data = []
    while(True):
        input = raw_input()
        if input == "":
            break
        else:
            data.append(tuple([int(x) for x in input.split()]))
    return dumps(data)

def get_url(input):
    return SERVICE_URL + "?" + DATA_PARAM + "=" + input

def format_output(output):
    out = output.split('\n')
    for res in out:
        print res

if __name__ == "__main__":
    print "\n -- Collatz Server Client -- \n"
    print """Enter a pair of numbers followed by a new line character for each test case.\nIndicate end of input by entering two new line characters.\n """
    input = get_json_input()
    url = get_url(input)
    result = get(url).content
    format_output(result)
