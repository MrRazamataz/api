# API testing at api.mrrazamataz.ga
import urllib.parse, urllib.request, re
from flask import Flask, request, abort, jsonify, redirect
import json, sqlite3, requests

app = Flask(__name__)


@app.route('/yturl', methods=['GET'])
def yturl():
    if request.method == 'GET':
        print(request.json)
        search = request.args.get('search')
        if search:
            print(search)
            query_string = urllib.parse.urlencode({"search_query": search})
            formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
            search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
            clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
            video_url = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
            result = {
                "error": "False",
                "video_url": video_url
            }

        else:
            result = {
                "error": "True",
                "error_msg": "Missing param `search`. Usage: /yturl?search=song 2 blur"
            }
        return result
    else:
        abort(400)


@app.route('/', methods=['GET'])
def root():
    return redirect("https://github.com/MrRazamataz/api", code=302)


if __name__ == '__main__':
    from waitress import serve

    serve(app, host="0.0.0.0", port=9000)
    # app.run(host='0.0.0.0', port=9000)
