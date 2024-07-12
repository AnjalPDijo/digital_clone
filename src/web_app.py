from flask import Flask, request, jsonify, render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from main import app, db, User, load_user, DigitalClone

clone = DigitalClone()

@app.route('/home')
@login_required
def web_app_home():
    return render_template('index.html')

@app.route('/likes', methods=['GET', 'POST', 'DELETE'])
@login_required
def manage_likes():
    if request.method == 'POST':
        item = request.json.get('item')
        clone.add_like(item)
        return jsonify({"message": f"Added like: {item}"}), 201
    elif request.method == 'DELETE':
        item = request.json.get('item')
        clone.remove_like(item)
        return jsonify({"message": f"Removed like: {item}"}), 200
    return jsonify({"likes": clone.get_data()['likes']}), 200

@app.route('/dislikes', methods=['GET', 'POST', 'DELETE'])
@login_required
def manage_dislikes():
    if request.method == 'POST':
        item = request.json.get('item')
        clone.add_dislike(item)
        return jsonify({"message": f"Added dislike: {item}"}), 201
    elif request.method == 'DELETE':
        item = request.json.get('item')
        clone.remove_dislike(item)
        return jsonify({"message": f"Removed dislike: {item}"}), 200
    return jsonify({"dislikes": clone.get_data()['dislikes']}), 200

@app.route('/behaviors', methods=['GET', 'POST', 'DELETE', 'PUT'])
@login_required
def manage_behaviors():
    if request.method == 'POST':
        behavior = request.json.get('behavior')
        description = request.json.get('description')
        clone.set_behavior(behavior, description)
        return jsonify({"message": f"Set behavior: {behavior}"}), 201
    elif request.method == 'PUT':
        behavior = request.json.get('behavior')
        description = request.json.get('description')
        clone.update_behavior(behavior, description)
        return jsonify({"message": f"Updated behavior: {behavior}"}), 200
    elif request.method == 'DELETE':
        behavior = request.json.get('behavior')
        clone.remove_behavior(behavior)
        return jsonify({"message": f"Removed behavior: {behavior}"}), 200
    return jsonify({"behaviors": clone.get_data()['behaviors']}), 200

if __name__ == '__main__':
    app.run(debug=True)
