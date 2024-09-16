#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>', 200

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)
    return parameter, 200

@app.route('/count/<int:parameter>')
def count(parameter):
    result = ""
    for number in range(parameter):
        result += f"{number}\n"
    return result, 200
        
@app.route('/math/<num1>/<operation>/<num2>')  
def math(num1, operation, num2):
    num1int = int(num1)
    num2int = int(num2)
    if operation == "+":
        result = num1int + num2int
        return str(result), 200
    elif operation == "-":
        result = num1int - num2int
        return str(result), 200
    elif operation == "div":
        result = num1int / num2int
        return str(result), 200
    elif operation == "*":
        result = num1int * num2int
        return str(result), 200
    else:
        return "0", 404


if __name__ == '__main__':
    app.run(port=5555, debug=True)