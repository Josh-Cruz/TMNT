from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/ninjas')
def ninjadisplay():
   return render_template('ninjas.html')

@app.route('/ninjas/<color>')
def sort_url(color):
   if color == 'red':
       pic = "raphael.jpg"
       print pic
       print color
       return render_template('colors.html', pic = pic )

app.run (debug = True)
