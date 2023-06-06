from flask import Flask

app= Flask(__name__)

@app.route('/')
def msg():
    return "Helloworld ! Deployed using argocd"

@app.route('/argocd')
def argocd_msg():
    return "Learning argocd"

if __name__ == "__main__":
    app.run(host='0.0.0.0')

