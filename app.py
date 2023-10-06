from flask import Flask, render_template
import csv

#data = [ ['1','2','abc','tt'],['3','4','def','tt'],['5','6','ghi','tt'] ]

file = open("sample.csv", "r")
data = list(csv.reader(file, delimiter=","))
file.close()

app = Flask(__name__)

@app.route('/')
def home():
    print(type(data))
    print(data)
    return render_template('Filtertable.html',  users=data)

if __name__ == '__main__':
    app.run(debug=True)
