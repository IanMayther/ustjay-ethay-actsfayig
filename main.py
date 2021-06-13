import os
from typing import Text

import requests
from flask import Flask, send_file, Response
from bs4 import BeautifulSoup

app = Flask(__name__)


def get_fact():

    response = requests.get("http://unkno.com")

    soup = BeautifulSoup(response.content, "html.parser")
    facts = soup.find_all("div", id="content")

    return facts[0].getText()


@app.route('/')
def home():
    fact = get_fact().lower()
    data = {'input_text': fact}
    response = requests.post('https://hidden-journey-62459.herokuapp.com/piglatinize/', data= data)
    result  = requests.get(response.url)
    soup = BeautifulSoup(result.content, "html.parser")
    answer = soup.getText()[39:]
    
    print(fact[7:])
    print(answer)

    quote = "Fact: " + fact
    latinize = "Latinized: " + answer
    website = "Link: " + response.url
    return '\n'.join([quote, latinize, website])


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6787))
    app.run(host='0.0.0.0', port=port)

