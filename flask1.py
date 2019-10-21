from flask import Flask, render_template, request
from seekfunction import seekletter

app = Flask(__name__)

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

@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Первая программа на Flask')

if __name__ == '__main__':
    app.run(debug=True)
