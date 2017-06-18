from flask import Flask,request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form= """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
      <!-- create your form here -->
      <form action="" method="post">
          <label for="rot"> Rotate by:
              <input type="text" id="rot" name="rot" value="0"/>
          </label>    
          <textarea name="text"/></textarea>
          <input type="submit" value="Submit Query"/>
      </form>
    </body>
</html>
"""
@app.route("/")
def index():
    return form

@app.route("/hello",methods=['POST'])
def hello():
    #first_name=request.args.get("first_name")
    first_name=request.form['first_name']
    return "<h1>Hello"+str(first_name)+"</h1>"

@app.route("/",methods=['POST'])
def encrypt():
    rot=int(request.form['rot'])
    rot_text=str(request.form['text'])
    encrypted_text = rotate_string(rot_text,rot)
    return "<h1>"+encrypted_text+"</h1>"



app.run()