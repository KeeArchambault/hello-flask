from flask import Flask, request

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!Doctype html>
<html>
    <body>
        <form action="/hello" method = "POST">
             <label for="first-name">First Name:</label>
            <input id= "first-name" type="text" name="first_name"/>
            <input type="submit"/>
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/hello", methods = ["POST"])
def hello():
    first_name = request.form["first_name"]
    return "<h1>Hello, " + first_name + "<h1>"

@app.route("/goodbye")
def goodbye():
    first_name = request.args.get("first_name")
    return "<h1>Goodbye, " + first_name + "</h1>"    

app.run()

