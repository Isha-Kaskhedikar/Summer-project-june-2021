from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    
    return "hello bitches"
# if __name__=="__main__":
#     app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)

#.\env\Scripts\activate.ps1