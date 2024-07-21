
# import os
# import json
# from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
# from flask_sqlalchemy import SQLAlchemy
# from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


# app = Flask(__name__)
# app.config['SECRET_KEY'] = os.urandom(24)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/clone'
# db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'



# class DigitalClone:
#     def __init__(self, data_file='data/clone_data.json'):
#         self.data_file = data_file
#         self.likes = set()
#         self.dislikes = set()
#         self.behaviors = {}
#         self.load_data()

#     def add_like(self, item):
#         self.likes.add(item.lower())
#         self.save_data()

#     def add_dislike(self, item):
#         self.dislikes.add(item.lower())
#         self.save_data()

#     def set_behavior(self, behavior, description):
#         self.behaviors[behavior.lower()] = description
#         self.save_data()

#     def does_like(self, item):
#         return item.lower() in self.likes

#     def does_dislike(self, item):
#         return item.lower() in self.dislikes

#     def describe_behavior(self, behavior):
#         return self.behaviors.get(behavior.lower(), "No description available.")

#     def remove_like(self, item):
#         self.likes.discard(item.lower())
#         self.save_data()

#     def remove_dislike(self, item):
#         self.dislikes.discard(item.lower())
#         self.save_data()

#     def remove_behavior(self, behavior):
#         if behavior.lower() in self.behaviors:
#             del self.behaviors[behavior.lower()]
#         self.save_data()

#     def update_like(self, old_item, new_item):
#         if old_item.lower() in self.likes:
#             self.likes.discard(old_item.lower())
#             self.likes.add(new_item.lower())
#         self.save_data()

#     def update_dislike(self, old_item, new_item):
#         if old_item.lower() in self.dislikes:
#             self.dislikes.discard(old_item.lower())
#             self.dislikes.add(new_item.lower())
#         self.save_data()

#     def update_behavior(self, behavior, new_description):
#         if behavior.lower() in self.behaviors:
#             self.behaviors[behavior.lower()] = new_description
#         self.save_data()

#     def save_data(self):
#         os.makedirs(os.path.dirname(self.data_file), exist_ok=True)
#         data = {
#             'likes': list(self.likes),
#             'dislikes': list(self.dislikes),
#             'behaviors': self.behaviors
#         }
#         with open(self.data_file, 'w') as file:
#             json.dump(data, file, indent=4)

#     def load_data(self):
#         if os.path.exists(self.data_file):
#             with open(self.data_file, 'r') as file:
#                 data = json.load(file)
#                 self.likes = set(data.get('likes', []))
#                 self.dislikes = set(data.get('dislikes', []))
#                 self.behaviors = data.get('behaviors', {})
#         else:
#             self.save_data()

#     def get_data(self):
#         return {
#             'likes': list(self.likes),
#             'dislikes': list(self.dislikes),
#             'behaviors': self.behaviors
#         }



# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(150), unique=True, nullable=False)
#     password = db.Column(db.String(150), nullable=False)

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         user = User(username=username, password=password)
#         db.session.add(user)
#         db.session.commit()
#         login_user(user)
#         return redirect(url_for('home'))
#     return render_template('register.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form.get('username')
#         password = request.form.get('password')
#         user = User.query.filter_by(username=username).first()
#         if user and user.password == password:
#             login_user(user)
#             return redirect(url_for('home'))
#         else:
#             flash('Login Unsuccessful. Please check username and password', 'danger')
#     return render_template('login.html')

# @app.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return redirect(url_for('login'))

# @app.route('/')
# @login_required
# def home():
#     return render_template('index.html')

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()  # Create all database tables based on defined models
#     app.run(debug=True)


import json
import os
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


# Define User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    likes = db.relationship('Likes', backref='user', lazy=True)
    dislikes = db.relationship('Dislike', backref='user', lazy=True)
    behaviors = db.relationship('Behavior', backref='user', lazy=True)


# Define Like model
class Likes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# Define Dislike model
class Dislike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(150), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


# Define Behavior model
class Behavior(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    behavior = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


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
    return render_template('index.html', username=current_user.username)


# Likes API Routes
@app.route('/likes', methods=['GET', 'POST'])
@login_required
def manage_likes():
    if request.method == 'GET':
        # Fetch likes for current user
        likes = [like.item for like in current_user.likes]
        return jsonify({'likes': likes})

    if request.method == 'POST':
        # Add a new like for current user
        data = request.json
        new_like = Likes(item=data['item'], user_id=current_user.id)
        db.session.add(new_like)
        db.session.commit()
        return jsonify({'message': 'Like added successfully'}), 201


@app.route('/likes/<int:index>', methods=['DELETE', 'PUT'])
@login_required
def modify_like(index):
    like_to_modify = current_user.likes[index]
    if request.method == 'DELETE':
        db.session.delete(like_to_modify)
        db.session.commit()
        return jsonify({'message': 'Like deleted successfully'})

    if request.method == 'PUT':
        data = request.json
        like_to_modify.item = data['item']
        db.session.commit()
        return jsonify({'message': 'Like updated successfully'})


# Dislikes API Routes
@app.route('/dislikes', methods=['GET', 'POST'])
@login_required
def manage_dislikes():
    if request.method == 'GET':
        # Fetch dislikes for current user
        dislikes = [dislike.item for dislike in current_user.dislikes]
        return jsonify({'dislikes': dislikes})

    if request.method == 'POST':
        # Add a new dislike for current user
        data = request.json
        new_dislike = Dislike(item=data['item'], user_id=current_user.id)
        db.session.add(new_dislike)
        db.session.commit()
        return jsonify({'message': 'Dislike added successfully'}), 201


@app.route('/dislikes/<int:index>', methods=['DELETE', 'PUT'])
@login_required
def modify_dislike(index):
    dislike_to_modify = current_user.dislikes[index]
    if request.method == 'DELETE':
        db.session.delete(dislike_to_modify)
        db.session.commit()
        return jsonify({'message': 'Dislike deleted successfully'})

    if request.method == 'PUT':
        data = request.json
        dislike_to_modify.item = data['item']
        db.session.commit()
        return jsonify({'message': 'Dislike updated successfully'})


# Behaviors API Routes
@app.route('/behaviors', methods=['GET', 'POST'])
@login_required
def manage_behaviors():
    if request.method == 'GET':
        # Fetch behaviors for current user
        behaviors = {behavior.behavior: behavior.description for behavior in current_user.behaviors}
        return jsonify({'behaviors': behaviors})

    if request.method == 'POST':
        # Add a new behavior for current user
        data = request.json
        new_behavior = Behavior(behavior=data['behavior'], description=data['description'], user_id=current_user.id)
        db.session.add(new_behavior)
        db.session.commit()
        return jsonify({'message': 'Behavior added successfully'}), 201


@app.route('/behaviors/<behavior>', methods=['DELETE', 'PUT'])
@login_required
def modify_behavior(behavior):
    behavior_to_modify = next((b for b in current_user.behaviors if b.behavior == behavior), None)

    if behavior_to_modify is None:
        return jsonify({'message': 'Behavior not found'}), 404

    if request.method == 'DELETE':
        db.session.delete(behavior_to_modify)
        db.session.commit()
        return jsonify({'message': 'Behavior deleted successfully'})

    if request.method == 'PUT':
        data = request.json
        behavior_to_modify.behavior = data['behavior']
        behavior_to_modify.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Behavior updated successfully'})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
