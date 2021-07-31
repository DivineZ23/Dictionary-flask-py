from flask import Flask, render_template, url_for, request
import json
from difflib import get_close_matches
data = json.load(open("data.json"))

app = Flask(__name__, template_folder="template")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    user_word = request.form['word']
    result = meaning(user_word)
    return render_template('search.html', result=result)

def meaning(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(),3,0.8)) > 0:
        str1=" "
        v=data[get_close_matches(word, data.keys(),3,0.8)[0]]
        str1=str1.join(v)
        return [f"Sorry, couldn't find {word}.\nPossible word {get_close_matches(word, data.keys(),3,0.8)[0]}:  " + str1]
    else:
        return ["Oops! the word doesn't exist. Please check again."]
if __name__ == '__main__':
    app.run()
