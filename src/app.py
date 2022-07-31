from flask import Flask, request, jsonify, Response, stream_with_context, abort

from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware

import requests

app = Flask(__name__)

@app.route("/<entity>", methods=["GET","POST"])
def save_entity(entity):
  db = TinyDB("data/%s.json" % entity, storage=CachingMiddleware(JSONStorage))
  if request.method == "POST":
    arg_json = request.get_json()
    if arg_json == None:
      return abort(400)
    event_id = db.insert(arg_json)
    db.close()
    return jsonify({'id': event_id}),201
  else: # is a GET
    # return jsonify(db.all())
    return abort(404)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
