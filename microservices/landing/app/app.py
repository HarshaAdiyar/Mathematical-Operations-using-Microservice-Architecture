from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def add(n1, n2):
    url = "http://addition-service:5052/"+str(n1)+"/"+str(n2)
    response = requests.get(url)
    return response.json()['Output']
    # return n1+n2

def minus(n1, n2):
    url = "http://subtraction-service:5053/"+str(n1)+"/"+str(n2)
    response = requests.get(url)
    return response.json()['Output']
    # return n1-n2

def multiply(n1, n2):
    url = "http://multiplication-service:5054/"+str(n1)+"/"+str(n2)
    response = requests.get(url)
    return response.json()['Output']
    # return n1*n2

def divide(n1, n2):
        url = "http://division-service:5055/"+str(n1)+"/"+str(n2)
        response = requests.get(url)
        return response.json()['Output']
    # return n1/n2
    
def exponent(n1, n2):
    url = "http://exponent-service:5056/"+str(n1)+"/"+str(n2)
    response = requests.get(url)
    return response.json()['Output']
    # return n1**n2
    
def modulus(n1, n2):
    url = "http://modulus-service:5057/"+str(n1)+"/"+str(n2)
    response = requests.get(url)
    return response.json()['Output']
    # return n1%n2

def equals(n1, n2):
    url = "http://equals-service:5058/"+str(n1)+"/"+str(n2)
    response = requests.get(url)
    return response.json()['Output']
    # return n1==n2


@app.route('/', methods=['POST', 'GET'])
def index():
    number_1 = request.form.get('first')
    number_2 = request.form.get('second')
    operation = request.form.get('operation')

    result = 0

    if operation == 'add':
        try:
            number_1=float(number_1)
            number_2=float(number_2)
            result = add((number_1), (number_2))
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

        except ValueError as e:
            flash(f'Please enter the numbers properly...')



    elif operation == 'minus':
        try:
            number_1=float(number_1)
            number_2=float(number_2)
            result = minus((number_1), (number_2))
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

        except ValueError as e:
            flash(f'Please enter the numbers properly...')


    elif operation == 'multiply':
        try:
            number_1=float(number_1)
            number_2=float(number_2)
            result = multiply((number_1), (number_2))
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

        except ValueError as e:
            flash(f'Please enter the numbers properly...')

    
    elif operation == 'divide':
        try:
            number_1=float(number_1)
            number_2=float(number_2)
            result = divide((number_1), (number_2))
            if(result=="Division by Zero error"):
                flash("Error: Division by Zero")
            else:
                flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

        except ValueError as e:
            flash(f'Please enter the numbers properly...')
       
    
    elif operation == 'exponent':
        try:
            number_1=float(number_1)
            number_2=float(number_2)
            result = exponent((number_1), (number_2))
            flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

        except ValueError as e:
            flash(f'Please enter the numbers properly...')
    
    
    elif operation == 'modulus':
        try:
            number_1=float(number_1)
            number_2=float(number_2)
            result = modulus((number_1), (number_2))
            if(result=="Modulo by Zero error"):
                flash("Error: Modulo by Zero error")
            else:
                flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')

        except ValueError as e:
            flash(f'Please enter the numbers properly...')

    elif operation == 'equals':
        try:
            number_1=float(number_1)
            number_2=float(number_2)
            result = equals((number_1), (number_2))
            # flash(f'The result of operation {operation} on {number_1} and {number_2} is {result}')
            if result==True:
                flash(f'Both  {number_1} and {number_2} are equal')
            else:    
                flash(f'Both  {number_1} and {number_2} are not equal') 

        except ValueError as e:
            flash(f'Please enter the numbers properly...')
        

    return render_template('index.html')

if __name__ == '__main__':
    app.run( 
        debug=True,
        port=5051,
        host="0.0.0.0"
    )
