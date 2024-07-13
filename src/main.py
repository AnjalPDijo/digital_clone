# import json
# import os

# class DigitalClone:
#     def __init__(self, data_file='data/clone_data.json'):
#         # Initialize empty data structures
#         self.likes = []
#         self.dislikes = []
#         self.behaviors = {}
#         self.data_file = data_file

#         # Load data if the file exists
#         if os.path.exists(self.data_file):
#             self.load_data()

#     def add_like(self, item):
#         self.likes.append(item)
#         self.save_data()

#     def add_dislike(self, item):
#         self.dislikes.append(item)
#         self.save_data()

#     def set_behavior(self, behavior, description):
#         self.behaviors[behavior] = description
#         self.save_data()

#     def get_data(self):
#         return {
#             "likes": self.likes,
#             "dislikes": self.dislikes,
#             "behaviors": self.behaviors
#         }

#     def save_data(self):
#         with open(self.data_file, 'w') as f:
#             json.dump(self.get_data(), f, indent=4)

#     def load_data(self):
#         with open(self.data_file, 'r') as f:
#             data = json.load(f)
#             self.likes = data.get("likes", [])
#             self.dislikes = data.get("dislikes", [])
#             self.behaviors = data.get("behaviors", {})

# if __name__ == "__main__":
#     clone = DigitalClone()
#     clone.add_like("Chocolate")
#     clone.add_dislike("Rain")
#     clone.set_behavior("Morning Routine", "Likes to have coffee and read news")

#     print(clone.get_data())


import os
import json
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/clone'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'



class DigitalClone:
    def __init__(self, data_file='data/clone_data.json'):
        self.data_file = data_file
        self.likes = set()
        self.dislikes = set()
        self.behaviors = {}
        self.load_data()

    def add_like(self, item):
        self.likes.add(item.lower())
        self.save_data()

    def add_dislike(self, item):
        self.dislikes.add(item.lower())
        self.save_data()

    def set_behavior(self, behavior, description):
        self.behaviors[behavior.lower()] = description
        self.save_data()

    def does_like(self, item):
        return item.lower() in self.likes

    def does_dislike(self, item):
        return item.lower() in self.dislikes

    def describe_behavior(self, behavior):
        return self.behaviors.get(behavior.lower(), "No description available.")

    def remove_like(self, item):
        self.likes.discard(item.lower())
        self.save_data()

    def remove_dislike(self, item):
        self.dislikes.discard(item.lower())
        self.save_data()

    def remove_behavior(self, behavior):
        if behavior.lower() in self.behaviors:
            del self.behaviors[behavior.lower()]
        self.save_data()

    def update_like(self, old_item, new_item):
        if old_item.lower() in self.likes:
            self.likes.discard(old_item.lower())
            self.likes.add(new_item.lower())
        self.save_data()

    def update_dislike(self, old_item, new_item):
        if old_item.lower() in self.dislikes:
            self.dislikes.discard(old_item.lower())
            self.dislikes.add(new_item.lower())
        self.save_data()

    def update_behavior(self, behavior, new_description):
        if behavior.lower() in self.behaviors:
            self.behaviors[behavior.lower()] = new_description
        self.save_data()

    def save_data(self):
        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
        data = {
            'likes': list(self.likes),
            'dislikes': list(self.dislikes),
            'behaviors': self.behaviors
        }
        with open(self.data_file, 'w') as file:
            json.dump(data, file, indent=4)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                data = json.load(file)
                self.likes = set(data.get('likes', []))
                self.dislikes = set(data.get('dislikes', []))
                self.behaviors = data.get('behaviors', {})
        else:
            self.save_data()

    def get_data(self):
        return {
            'likes': list(self.likes),
            'dislikes': list(self.dislikes),
            'behaviors': self.behaviors
        }



class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/')
@login_required
def home():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create all database tables based on defined models
    app.run(debug=True)



