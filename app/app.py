from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello flask from DIT DT228 Program!"

@app.route("/user/<username>")
def show_user(username):
  return "Hello user %s" % username
if __name__ == "__main__":
  app.run(host="0.0.0.0", port=3000, debug = True)
