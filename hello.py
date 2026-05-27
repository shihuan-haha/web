from flask import Flask, render_template

app = Flask(__name__)

@app.route('/page/user')
def page_user_info():
    x = { 
        "name": "John", 
        "age": 30, 
        "city": "New York" 
    }
    # 🔴 注意：這裡要寫 render_template，並且要把 x 和 text 傳過去
    return render_template('page.html', x=x, text="Hello, this is John's Profile!")