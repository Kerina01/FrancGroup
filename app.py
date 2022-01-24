from flask import Flask, render_template, jsonify, Response, request, json

app = Flask(__name__)

@app.route('/')
def index_view():
    username = request.args.get('username')
    with open("posts.json", 'r') as f:
        posts = json.load(f)

    with open("users.json", 'r') as uf:
        users = json.load(uf)
    
    dictList = []
    followers = []
    final = []
    
    for i in posts:
        for elem in posts[i]:
            tweetOwner = {'username':i}
            elem.update(tweetOwner)
            dictList.append(elem)

    for i in users:
        if (i == username):
            followers = users[i]

    followers.append(username)
    
    for item in dictList:
        if (followers.count(item['username']) > 0):
            final.append(item)

    newlist = sorted(final, key=lambda d: d['time'])

    return render_template('index.html', username = username, dictList = newlist)

@app.route('/users')
def users_view():
    with open('./users.json', 'r') as f:
        users = f.read()
    return Response(users, mimetype="application/json")

@app.route('/posts')
def posts_view():
    with open('./posts.json', 'r') as f:
        posts = f.read()
    return Response(posts, mimetype="application/json")

if __name__ == '__main__':
    app.run(host='127.0.0.1')