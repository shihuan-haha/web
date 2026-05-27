from flask import Flask, render_template

app = Flask(__name__)

@app.route('/Hello')
def home():
    return render_template('Hello.html')
    
@app.route('/Jenny')
def home():
    return render_template('Jenny.html')

@app.route('/index')
def home():
    return render_template('index.html')

@app.route('/ex48')
def home():
    return render_template('ex48.html')
    
# 🎯 Exercise 41: 基礎路由與 HTML 範本
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/apple')
def apple():
    return render_template('apple.html')

# 🎯 Exercise 42: 傳送變數與字典資料到前端
@app.route('/page/user')
def page_user_info():
    x = { 
        "name": "John", 
        "age": 30, 
        "city": "New York" 
    }
    return render_template('page.html', x=x, text="Hello, this is John's Profile!")

# 🎯 Exercise 43: Jinja2 For 迴圈 (多筆資料表格)
@app.route('/page/list')
def page_list():
    users = [
        {"name": "John", "age": 30, "city": "New York"},
        {"name": "Jenny", "age": 25, "city": "Taipei"},
        {"name": "Bob", "age": 35, "city": "London"},
        {"name": "Alice", "age": 28, "city": "Tokyo"}
    ]
    return render_template('page_list.html', user_list=users)

# 🎯 Render 雲端部署必備：讓伺服器監聽正確的連接埠 (Port)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
