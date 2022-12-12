from flask import Flask, render_template, request, redirect, url_for, jsonify
from py1337x import py1337x
from dotenv import dotenv_values
from TorrentManager import TorrentManager
from AttrDictJson import as_attrdict

import shutil
import sys
import os
import json

download_path = os.path.join(os.path.join(os.getcwd(), 'static'), 'downloads')
app = Flask(__name__)
portNumber = sys.argv[1]
torrents = py1337x()
tm = TorrentManager(download_path, dotenv_values(".env"))

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

@app.route("/downloads", methods=['GET', 'POST'])
def downloads():
    # If there is a POST, start downloading
    if request.method == "POST":
        tm.add_torrent(request.form.get("torrentinfo"))

    # for both POST and GET, get all downloads and progress
    html = '''
                <table border=1>
                    <tr>
                        <th>Name</th>
                        <th>Progress</th>
                        <th>Status</th>
                        <th>Toggle</th>
                        <th>Delete</th>
                    </tr>
            '''
    for torrent in tm.get_torrents():
        html += '<tr><td>'+torrent.name+'</td><td id="progress" name="progress">'+str(torrent.progress)+'</td><td>'+torrent.state+'</td><td><input type="submit" value="Pause/Resume"></td><td><input name=\"'+torrent.name+'\" type=\"checkbox\"></td></tr>'
    
    html += "</table><br><input type=\"submit\" value=\"Delete All\">"

    return render_template('downloads.html', table=html)

@app.route("/query/all/info")
def ReturnJSON():
    return json.dumps(tm.maindata()['torrents'], default=as_attrdict)

@app.route("/query/all/delete")
def deleteAll():
    tm.delete_all_torrents()
    shutil.rmtree(download_path)
    os.mkdir(download_path)
    return jsonify(success='true')

if __name__ == '__main__':
    app.run(host='localhost', port=portNumber)