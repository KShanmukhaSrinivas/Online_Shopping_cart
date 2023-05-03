from flask import Flask,render_template,redirect,request,url_for
app = Flask(__name__)

@app.route('/success')
def success(name):
   return 'welcome %s' % name

@app.route('/attendance', methods = ['POST', 'GET'])
def hello_world():
   if request.method == 'POST':
      user = request.form
      return redirect(url_for('success',name = user))
   else:
      return render_template("attendance.html")

@app.route('/fl')
def hello_flask():
   return 'Hello Flask'

if __name__ == '__main__':
   app.run()