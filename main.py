from flask import Flask, request, redirect, render_template

app = Flask(__name__)

app.config['DEBUG'] = True

username = ""

email = ""

"""
for word in text:
	letters = list(word)
	for letter in letters:
		if not((ord(letter) > 64 and ord(letter) < 91) or (ord(letter) > 96 and ord(letter) < 123)):
			letters.pop(letters.index(letter))
	text[accum] = ''.join(letters)
	accum = accum + 1
"""
	
@app.route("/")
def index():
	return render_template("form.html")
	
@app.route("/welcome",methods=['POST'])
def welcome():
	username = request.form['username']
	email = request.form['email']
	password = request.form['pwd']
	vpwd = request.form['vpwd']
	errors = False
	usererror = ""
	pwderror = ""
	vpwderror = ""
	emailerror = ""

	#Error case: If email is provided, contains a single @, a single ., no spaces, between 3 and 20 characters long
	if len(email) != 0:
		email_list = list(email)
		at_count = 0
		dot_count = 0
		other = False
		spaces = False
		
		
		if len(email) < 3 or len(email) > 20:
			emailerror = "badchar"
		else:
			for letter in email_list:
				if letter == '@':
					at_count = at_count + 1
				if letter == '.':
					dot_count = dot_count + 1
				if letter == ' ':
					spaces = True
				if not((ord(letter) > 64 and ord(letter) < 91) or (ord(letter) > 96 and ord(letter) < 123) or (ord(letter) > 47 and ord(letter) < 58)) and letter != '@' and letter != ".":
					other = True
		if spaces == True or at_count != 1 or dot_count != 1 or other == True:
			emailerror = "format"
			errors = True
	
	#Error case: username or password contains whitespace, or is less than 3 characters or greater than 20 characters
	if username.find(" ") != -1 or password.find(" ") != -1 or len(username) < 3 or len(password) < 3 or len(username) > 20 or len(password) > 20:
		if len(username) < 3:
			usererror = "short"
		if len(password) < 3:
			pwderror = "short"
		if len(username) > 20:
			usererror = "long"
		if len(password) > 20:
			pwderror = "long"
		if username.find(" ") != -1:
			usererror = "whitespace"
		if password.find(" ") != -1:
			pwderror = "whitespace"
		errors = True	
		
	#Error case: password and verify passwords do not match	
	if password != vpwd:
		vpwderror = "mismatch"
		pwderror = "mismatch"
		errors = True
		
	#Error case: empty fields
	if username == "" or password == "" or vpwd == "":
		if request.form['username'] == "":
			usererror = "empty"
		if request.form['pwd'] == "":
			pwderror = "empty"
		if request.form['vpwd'] == "":
			vpwderror = "empty"
		errors = True
	
	if errors == True:
		return render_template("form.html",usererror=usererror,pwderror=pwderror,vpwderror=vpwderror,emailerror=emailerror,username=username,email=email)
	
	return render_template("welcome.html",username=username)

app.run()
