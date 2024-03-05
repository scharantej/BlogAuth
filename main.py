
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text)
    author = db.Column(db.String(30))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/')
def index():
    posts = BlogPost.query.order_by(BlogPost.id.desc()).limit(5).all()
    return render_template('index.html', posts=posts)

@app.route('/blog_list')
def blog_list():
    posts = BlogPost.query.order_by(BlogPost.id.desc()).limit(5).all()
    return render_template('blog_list.html', posts=posts)

@app.route('/blog_details/<int:blog_id>')
def blog_details(blog_id):
    post = BlogPost.query.get(blog_id)
    return render_template('blog_details.html', post=post)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
