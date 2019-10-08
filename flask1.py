from flask import Flask, render_template, request
from seekfunction import seekletter

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello Sem from Flask!'

@app.route('/seekfunction', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Results:'
    results = str(seekletter(phrase, letters))
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results,)

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to seekletter on web first programm I have created')

app.run(debug=True)
