from flask import Flask, render_template, redirect, url_for

from config import VIDEO_ID, HOST, PORT


app = Flask(__name__)


@app.route('/', methods=['GET'])
def get():
    return render_template(
        'index.html',
        video_id=VIDEO_ID,
    )


@app.route('/', methods=['POST'])
def post():
    return redirect(url_for('get'))


if __name__ == '__main__':
    app.run(HOST, PORT)
