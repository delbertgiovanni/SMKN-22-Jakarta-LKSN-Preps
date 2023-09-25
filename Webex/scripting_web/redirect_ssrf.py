from flask import Flask, redirect

app = Flask(__name__)

counter = 0

@app.route("/")
def index():
    global counter
    counter += 1
    if counter == 1:
        return redirect("http://google.com")

    return redirect('http://127.0.0.1/flag', code=302)

if __name__ == "__main__":
    app.run()