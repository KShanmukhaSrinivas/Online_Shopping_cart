from flask import Flask,render_template,redirect,request,url_for,session
app = Flask(__name__)
app.config['SECRET_KEY'] = "RWFSEGSRGTJNDSFABGE"
@app.route('/success/<name>')
//changed
def success(name):
   return f'<h1>welcome {name}</h1>'

@app.route('/attendance', methods = ['POST', 'GET'])
def hello_world():
   if request.method == 'POST':
      session['user'] = request.form["name"]
      return redirect(url_for('success',name = session['user']))
   else:
      return render_template("attendance.html")

@app.route('/fl')
def hello_flask():
   return 'Hello Flask'

if __name__ == '__main__':
   app.run(debug = True)
