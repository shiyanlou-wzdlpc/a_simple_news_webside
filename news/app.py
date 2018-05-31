#!/usr/bin/env python3
import os
import json
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    path = '/home/shiyanlou/files'
    title_list = []
    for filename in os.listdir(path):
        with open(os.path.join(path, filename)) as f:
            for k, y  in json.loads(f.read()).items():
                if k == 'title':
                    title_list.append(y)
    titles = {'title':title_list}
    return render_template('index.html', titles=titles)

@app.route('/files/<filename>')
def files(filename):
    real_filename = filename + '.json'
    path =  '/home/shiyanlou/files'
    filepath = os.path.join(path,real_filename)
    if real_filename in os.listdir(path):
        with open(filepath) as f:
            str_file = json.loads(f.read())
        return render_template('file.html', str_file=str_file)
    else:
        return render_template('404.html'), 404


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()
            
