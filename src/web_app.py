from flask import request, jsonify, redirect, url_for
from flask_login import login_required, current_user
from main import app, db, Likes, Dislike, Behavior  # Ensure correct imports

@app.route('/likes', methods=['GET', 'POST'])
@login_required
def manage_likes():
    if request.method == 'POST':
        item = request.json.get('item')
        like = Likes(item=item, user_id=current_user.id)
        db.session.add(like)
        db.session.commit()
        return jsonify({"message": f"Added like: {item}"}), 201

    likes = [like.item for like in current_user.likes]
    return jsonify({"likes": likes}), 200

@app.route('/likes/<int:index>', methods=['DELETE', 'PUT'])
@login_required
def modify_likes(index):
    likes = current_user.likes
    if index >= len(likes):
        return jsonify({"message": "Like not found"}), 404

    like = likes[index]

    if request.method == 'DELETE':
        db.session.delete(like)
        db.session.commit()
        return jsonify({"message": f"Removed like: {like.item}"}), 200

    if request.method == 'PUT':
        new_item = request.json.get('item')
        like.item = new_item
        db.session.commit()
        return jsonify({"message": f"Updated like to: {new_item}"}), 200

    return jsonify({"message": "Invalid request"}), 400

@app.route('/dislikes', methods=['GET', 'POST'])
@login_required
def manage_dislikes():
    if request.method == 'POST':
        item = request.json.get('item')
        dislike = Dislike(item=item, user_id=current_user.id)
        db.session.add(dislike)
        db.session.commit()
        return jsonify({"message": f"Added dislike: {item}"}), 201

    dislikes = [dislike.item for dislike in current_user.dislikes]
    return jsonify({"dislikes": dislikes}), 200

@app.route('/dislikes/<int:index>', methods=['DELETE', 'PUT'])
@login_required
def modify_dislikes(index):
    dislikes = current_user.dislikes
    if index >= len(dislikes):
        return jsonify({"message": "Dislike not found"}), 404

    dislike = dislikes[index]

    if request.method == 'DELETE':
        db.session.delete(dislike)
        db.session.commit()
        return jsonify({"message": f"Removed dislike: {dislike.item}"}), 200

    if request.method == 'PUT':
        new_item = request.json.get('item')
        dislike.item = new_item
        db.session.commit()
        return jsonify({"message": f"Updated dislike to: {new_item}"}), 200

    return jsonify({"message": "Invalid request"}), 400

@app.route('/behaviors', methods=['GET', 'POST'])
@login_required
def manage_behaviors():
    if request.method == 'POST':
        behavior = request.json.get('behavior')
        description = request.json.get('description')
        new_behavior = Behavior(behavior=behavior, description=description, user_id=current_user.id)
        db.session.add(new_behavior)
        db.session.commit()
        return jsonify({"message": f"Set behavior: {behavior}"}), 201

    behaviors = {behavior.behavior: behavior.description for behavior in current_user.behaviors}
    return jsonify({"behaviors": behaviors}), 200

@app.route('/behaviors/<string:behavior>', methods=['DELETE', 'PUT'])
@login_required
def modify_behaviors(behavior):
    behavior_entry = Behavior.query.filter_by(behavior=behavior, user_id=current_user.id).first()
    if not behavior_entry:
        return jsonify({"message": "Behavior not found"}), 404

    if request.method == 'DELETE':
        db.session.delete(behavior_entry)
        db.session.commit()
        return jsonify({"message": f"Removed behavior: {behavior}"}), 200

    if request.method == 'PUT':
        new_description = request.json.get('description')
        behavior_entry.description = new_description
        db.session.commit()
        return jsonify({"message": f"Updated behavior description to: {new_description}"}), 200

    return jsonify({"message": "Invalid request"}), 400

if __name__ == '__main__':
    app.run(debug=True)
