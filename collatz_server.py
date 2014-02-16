from json import loads, dumps
from flask import Flask, request
from gevent import monkey
from collatz import p_range_collatz, range_collatz, p_collatz
app = Flask(__name__)

@app.route("/")
def collatz():
    data = process_input(request.args.get('data' ,''))
    out = p_collatz(data)
    return format_output(data, out)


def process_input(data):
    return [tuple(range) for range in loads(data)]

def format_output(data, out):
    str_out = ""
    for (range, output) in zip(data, out):
        str_out += str(range[0]) + " " + str(range[1]) + " " + str(output) +"\n"
    return str_out

if __name__ == '__main__':
    monkey.patch_all()
    app.debug = True
    app.run()
