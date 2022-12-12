from flask import Flask, render_template, request, redirect, url_for
from py1337x import py1337x
import json
import sys

app = Flask(__name__)
portNumber = sys.argv[1]
torrents = py1337x()

@app.route("/bruh")
def bruh():
    return "bruh"

@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == "POST":
        search = request.form.get("search")
        results = torrents.search(search)["items"]
        html = '''<table border=1>
                <tr><th>Name</th><th>Size</th><th>Seeders</th><th>Select</th></tr>'''
        for item in results:
            html += '<tr><td>'+item['name']+'</td><td>'+item['size']+'</td><td>'+item['seeders']+'</td><td><a href=\"/select/'+item['torrentId']+'\">SELECT</a></td>'
        html+='</table>'
        return render_template('search.html', table=html)
    else:
        return render_template('search.html')

@app.route("/")
def home():
    return redirect(url_for("search"))

@app.route("/select/<torrentId>")
def select(torrentId):
    torrentinfo = torrents.info(torrentId=torrentId)
    return render_template('select.html', name=torrentinfo['name'], category=torrentinfo['category'], type=torrentinfo['type'], language=torrentinfo['language'], downloads=torrentinfo['downloads'], link=torrentinfo['magnetLink'])

if __name__ == '__main__':
    app.run(host='localhost', port=portNumber)