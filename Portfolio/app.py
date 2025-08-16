from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', title="Home")

@app.route('/projects')
def projects():
    return render_template('projects.html', title="Projects")

@app.route('/events')
def events():
    return render_template('events.html', title="Events")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

if __name__ == '__main__':
    app.run(debug=True, port=7200)
