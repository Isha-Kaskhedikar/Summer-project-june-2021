from flask import Flask, render_template, request, session, redirect, url_for,g
# g is global for request context, to avoid passing things around

#temporarily using list, change to database
class User:
    def __init__(self, id, username, password):
        self.id=id
        self.username=username
        self.password=password
    def __repr__(self):
        return f'<User: {self.username}>'

users=[] #global 
users.append(User(id=1,username='ish@abc.com',password='pass'))
users.append(User(id=2,username='kaz@dreg.com',password='crow'))

app=Flask(__name__)
app.secret_key='thisissupposedtobeasecret' # use os.random for more security

@app.before_request
def before_request():
    if 'user_id' in session:
        user=[x for x in users if x.id==session['user_id']][0] # idf user from list
        g.user=user
    else:
        g.user=None

@app.route('/signup')
def signup(): 
    return render_template("signup.html")

# cookies dont make sense of python objects, so session id is passed so our app
# can make sense of it later to give python objects
@app.route('/',methods=['GET','POST'])
def login(): 
    if request.method=='POST':
        session.pop('user_id', None)
        username=request.form["emailAddress"] # username is email for now
        password=request.form['password']
        user=[x for x in users if x.username==username][0] # replace with a query
        if user and user.password==password:
            session['user_id']=user.id # make session after verification
            return redirect(url_for('profile'))
        return redirect(url_for(''))
    return render_template("login.html")

@app.route('/profile')
def profile(): 
    if not g.user: # no user session exists
        return redirect(url_for('signup'))
        
    return render_template("profile.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True)

#.\env\Scripts\activate.ps1