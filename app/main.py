from flask import Flask

app=Flask(__name__)

@app.route('/')
def msg():
    return "Helloworld ! Deployed using argocd"

if __name__ == "__main__":
    app.Run(host='0.0.0.0')

