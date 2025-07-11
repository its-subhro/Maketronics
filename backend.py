from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_tools():
    url = 'https://spacelift.io/blog/software-development-tools'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    tool_elements = soup.select('#section-best-software-development-tools > div:nth-child(2) > div > ol > li > a > span')

    tools = []
    for element in tool_elements:
        tool_name = element.get_text(strip=True)
        if tool_name:
            tools.append(tool_name)
    return tools

@app.route('/')
def index():
    tools = get_tools()
    tools_with_index = list(enumerate(tools, start=1))  
    return render_template('index.html', tools=tools_with_index)

if __name__ == '__main__':
    app.run(debug=True)