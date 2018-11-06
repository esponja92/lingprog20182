from flask import Flask
from flask import render_template
import models

app = Flask(__name__)

@app.route('/')
def raiz():
    return  '\
<html> \
<body> \
Name:	<input type="text" id="myAnchor" name="name" value=""> <button onclick="myFunction()" id="button">aluno</button>\
<button onclick="F()" id="button">professor</button>\
<a href="localhost:5000/#myAnchor" id="demo"> vai</a>\
<script> \
function myFunction() { \
    var x = document.getElementById("myAnchor").value; \
     document.getElementById("demo").href= x; \
} \
function F() { \
    var x = document.getElementById("myAnchor").value; \
     document.getElementById("demo").href= "professor/"; \
} \
</script> \
</body> \
</html>'

	

@app.route('/<nome>/')
def Who(nome=""):
    if (nome == "professor"):
           return models.Professor.draw()
    else:
           models.Aluno.w(nome)
           return '\
<html> \
<body> \
Idade:	<input type="text" id="myAnchor"  value=""> <button onclick="myFunction()" id="button">salva</button>\
<a href="localhost:5000/"+nome+"/#myAnchor" id="demo"> vai</a>\
<script> \
function myFunction() { \
    var x = document.getElementById("myAnchor").value; \
     document.getElementById("demo").href= x; \
} \
</script> \
</body> \
</html>'

@app.route('/<nome>/<idade>')
def Age(nome="",idade=""):
	models.Aluno.update(nome, idade)
	nome = nome +"/" + idade
	return  '<html> \
<body> \
<h1> Valeu </h1>\
</body> \
</html>'

"""                                ,.   '\'\    ,---.
Quiet, Pinky; I'm pondering.    | \\  l\\l_ //    |   Err ... right,
       _              _         |  \\/ `/  `.|    |   Brain!  Narf!
     /~\\   \        //~\       | Y |   |   ||  Y |
     |  \\   \      //  |       |  \|   |   |\ /  |   /
     [   ||        ||   ]       \   |  o|o  | >  /   /
    ] Y  ||        ||  Y [       \___\_--_ /_/__/
    |  \_|l,------.l|_/  |       /.-\(____) /--.\
    |   >'          `<   |       `--(______)----'
    \  (/~`--____--'~\)  /           U// U / \
     `-_>-__________-<_-'            / \  / /|
         /(_#(__)#_)\               ( .) / / ]
         \___/__\___/                `.`' /   [
          /__`--'__\                  |`-'    |
       /\(__,>-~~ __)                 |       |__
    /\//\\(  `--~~ )                 _l       |--:.
    '\/  <^\      /^>               |  `   (  <   \\
         _\ >-__-< /_             ,-\  ,-~~->. \   `:.___,/
        (___\    /___)           (____/    (____)    `---'
"""
