from flask import Flask, jsonify, request

app_name = 'comentarios'
app = Flask(app_name)
app.debug = True

comments = {}

@app.route('/api/comment/new', methods=['POST'])
def api_comment_new():
    try:
        request_data = request.get_json()
        if not all(key in request_data for key in ['email', 'comment', 'content_id']):
            raise ValueError("Missing required fields")

        email = request_data['email']
        comment = request_data['comment']
        content_id = str(request_data['content_id'])

        new_comment = {'email': email, 'comment': comment}

        if content_id in comments:
            comments[content_id].append(new_comment)
        else:
            comments[content_id] = [new_comment]

        message = f"Comment created and associated with content_id {content_id}"
        response = {'status': 'SUCCESS', 'message': message}
        return jsonify(response)

    except Exception as e:
        response = {'status': 'ERROR', 'message': str(e)}
        return jsonify(response), 400


@app.route('/api/comment/list/<content_id>')
def api_comment_list(content_id):
    content_id = str(content_id)
    if content_id in comments:
        return jsonify(comments[content_id])
    else:
        message = f"Content_id {content_id} not found"
        response = {'status': 'NOT-FOUND', 'message': message}
        return jsonify(response), 404


if __name__ == "__main__":
    app.run()
