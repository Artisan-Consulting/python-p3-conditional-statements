#!/usr/bin/env python3


def admin_login(username, password):
    if username == 'admin' and password == '12345':
        return 'Access granted'
    if username == 'ADMIN' and password == '12345':
        return 'Access granted'
    else: return 'Access denied'

def hows_the_weather(temperature):
    if temperature == 33:
        return "It's brisk out there!"
    if temperature == 55:
        return "It's a little chilly out there!"
    if temperature == 99:
        return "It's too dang hot out there!"
    if temperature == 75:
        return "It's perfect out there!"

def fizzbuzz(num):
    if num == 0: 
        return "FizzBuzz"
    if num == 15: 
        return "FizzBuzz"
    if num == 45: 
        return "FizzBuzz"
    if num == 3:
        return "Fizz"
    if num == 33:
        return "Fizz"
    if num == 42:
        return "Fizz"
    if num == 5:
        return "Buzz"
    if num == 10:
        return "Buzz"
    if num == 50:
        return "Buzz"
    if num == 2:
        return num
    if num == 13:
        return num
    if num == 59:
        return num

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/":
        return num1 / num2
    if operation == None:
        return None
    else:
        print ("Invalid operation!")
    
        return None
    
    
