# -*- coding: utf-8 -*-
from Ai import *
from write_to_log import write_to_log
from flask import Flask, redirect
import os
app = Flask(__name__)

@app.route("/")
def hello_world():
    pass

@app.route("/gen/<prmit>")
def generate(prmit):
    gen(prmit)
    write_to_log(prmit)
    return redirect(f"/static/{prmit}.png")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)


