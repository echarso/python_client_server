import json
from flask import Flask
from flask import render_template
from flask import request
from controller import Controller


app = Flask(__name__)
con = Controller();


@app.route("/increase")
def increase():
    value = request.args.get('value')
    user = request.args.get('user')
    print "=================== decrease", value,user

    return con.increase(float(value))


@app.route("/decrease")
def decrease():
    value = request.args.get('value')
    user = request.args.get('user')
    print "=================== decrease ", "value ", value, "user " , user

    return con.decrease(float(value))

if __name__ == '__main__':
    app.run(debug=True)
