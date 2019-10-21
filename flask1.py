from flask import Flask, render_template, request
from seekfunction import seekletter
import calculator

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

@app.route('/calc')
def do_summ() -> 'html':
    number1 = request.form['num1']
    number2 = request.form['num2']
    title2 = 'Ответ:'
    results2 = str(number1 + number2)
    return render_template('calc.html',
                           the_num1=number1,
                           the_num2=number2,
                           the_title2=title2,
                           the_results2=results2,)



@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Первая программа на Flask')

if __name__ == '__main__':
    app.run(debug=True)
