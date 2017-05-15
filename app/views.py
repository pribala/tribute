from flask import Flask
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
        num = request.form['rolls']	
		result = {} 
		rolls = {}
		for k in range(2, 13):
			rolls[k] = 0
		doubles = 0

		for k in range(num):
			first = random.randint(1, 6)
			second = random.randint(1, 6)
			if first == second:
					doubles+=1
			rolls[first+second]+=1

		for k in rolls:
			#print('%d - %d %f%%' %(k, rolls[k], float(rolls[k])/float(num)*100))
			dict2 = {k:rolls[k]}		
			result.update(dict2)		

		#print('Doubles - %d - %f%%' %(doubles, float(doubles)/float(num)))
		dict3 = {'Doubles':doubles}	
		result.update(dict3)	
		return json.dumps(result)
    else:
        return render_template('userInput.html')	
	

if __name__ == '__main__':
    app.secret_key = 'very_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)