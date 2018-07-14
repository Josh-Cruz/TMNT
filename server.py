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
    color_map = {
        'red': "raphael.jpg",
        'blue': "leonardo.jpg",
        'orange': "michelangelo.jpg",
        'purple': "donatello.jpg",
        'default': "notapril.jpg"
    }
    if color in color_map:
       pic = color_map[color] 
    else:
        pic = color_map['default']
    return render_template('colors.html', pic = pic )
app.run (debug = True)
