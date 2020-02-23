#!/usr/bin/env python3

import cgitb
import cgi
cgitb.enable()

print("Content-Type: text/html")
print()

# Get input from user
form = cgi.FieldStorage()
user_color = form["color"].value.upper()

# Read text file
f = open('./src/html_colors.txt')
try:
	# Create an array of all the colors
	colors = f.read().splitlines()
finally:
    f.close()

# Print HTML
if user_color in colors:
	print(f'''<!DOCTYPE html>
	<html>
	<head>
		<title>Color Check</title>
		<link rel="stylesheet" type="text/css" href="/style.css">
	</head>
	<body>
		<div id="main">
			<h1><a href="index.html">Color check</a></h1>
			<h2><span style="font-family: 'JetBrains Mono'; font-weight: 400; color:#4A7768">{form["color"].value}</span> is a color!</h2>
			<h3>Here's what it looks like:</h3>
			<div style="background-color: {form["color"].value}"id="color_block"></div>
			<a href="/index.html"><button id="back_button">Go back</button></a>
		</div>
		<script> </script>
	</body></html>''')
else:
	print(f'''<!DOCTYPE html>
	<html>
	<head>
		<title>Try again</title>
		<link rel="stylesheet" type="text/css" href="/style.css">
	</head>
	<body>
		<div id="main">
			<h1><a href="/index.html">Color check</a></h1>
			<h2>Unfortunately, <span style="font-family: 'JetBrains Mono'; font-weight: 400; color:#4A7768">{form["color"].value}</span> is not a color.</h2>
			<h3>You can try again here:</h3>
			<form action="/cgi-bin/generate.py" method="GET">
				<input autocomplete="off" type="text" name="color" id="color_input" placeholder="'red', '#fa32bc', etc" required>
				<button id="check_button" type="submit">Check color</button>
			</form>
		</div>
		<script> </script>
	</body>
	</html>''')



