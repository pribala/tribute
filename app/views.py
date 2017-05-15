from flask import Flask, render_template
from flask import request

app = Flask(__name__)
import json
import random

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dice', methods=['GET', 'POST'])	
def diceRoll():
    if request.method == 'POST':
    # num = int(input('How many rolls do you want to simulate? '))
        # Get the value for number of rolls entered by user	
        num = int(request.form['rolls'])	
        result = {}   # create a dictionary for the result 
        rolls = {}    # create a dictionary for the possible sum of the 2 dice rolls from 2-12 
        for k in range(2, 13):
            rolls[k] = 0
        doubles = 0

        for k in range(num):
            first = random.randint(1, 6)   # generate random numbers between 1 to 6
            second = random.randint(1, 6)
            sum = first + second			
            if first == second:
                doubles+=1  # increment doubles if same number rolled on both dices
            rolls[sum]+=1

        for k in rolls:
            dict2 = {k:rolls[k]}		
            result.update(dict2)		

        dict3 = {'Doubles':doubles}	
        result.update(dict3)	
        return json.dumps(result)
    else:
        return render_template('userInput.html')	
	

if __name__ == '__main__':
    app.secret_key = 'very_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)