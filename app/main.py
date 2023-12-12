# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_render_template]
# [START gae_python3_render_template]
import datetime
import json
import os
import requests
from google.cloud import datastore
from google.cloud.datastore.query import PropertyFilter

from flask import Flask, render_template, request, jsonify, abort
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

API_URI_ROOT = "https://api.doc.govt.nz/v1"
API_PARAMS = {
    "headers": {"x-api-key": os.environ.get("DOC_API_KEY")},
    "params": {"coordinates": "wgs84"},
}

client = datastore.Client()

def get_tracks():
    r = requests.get(
            f"{API_URI_ROOT}/tracks/",
            **API_PARAMS
    )
    return r.json()

def get_track(asset_id):
    r = requests.get(
            f"{API_URI_ROOT}/tracks/{asset_id}/detail",
            **API_PARAMS,
    )
    return r.json()

def store_track(track):
    try:
        entity = datastore.Entity(
            key=client.key(
                "track",
                track.get("assetId"),
            )
        )
    except ValueError:
        app.logger.warning(f"{track} invalid")
        return

    for k in track.keys():
        if k != "line":
            # Line not stored in GCS - retrieved 'live'
            entity[k] = track[k]
    
    client.put(entity)

def get_distinct_values(key):
    query = client.query(kind="track")
    query.distinct_on = [key]
    distinct_values = []
    for distinct_value in query.fetch():
        distinct_values.append(distinct_value[key])
    return distinct_values

def get_matching_tracks(key,value):
    query = client.query(kind="track")
    query.add_filter(
  filter=PropertyFilter(key,"=",value)
)
    results=[]
    for result in query.fetch():
        results.append(dict(result))
    return results

@app.route("/")
def root():
    results = get_distinct_values("dogsAllowed")

    return render_template("index.html", tracks=results)


@app.route("/tracks", methods=["GET"])
def track():
    """This method will return information about a selected track."""
    import os, requests

    DOC_API_KEY = os.environ.get("DOC_API_KEY")

    selected_track = request.get_json()

    APITRACK = f"{API_URI_ROOT}/tracks"
    pass

@app.route("/track_filter", methods=["POST"])
def track_filter():
    """This method will return tracks given a particular filter."""
    filter = request.get_json()

    return get_matching_tracks(filter["key"],filter["value"])


@app.route("/tasks/refresh_tracks", methods=["GET"])
def task_refresh_tracks():
    """Writes files for all tracks to storage.

    Local - writes to static/tracks
    GCS - writes to bucket/static/tracks
    """
    import os
    import requests

    tracks = get_tracks()

    app.logger.info(f"Updating info for {len(tracks)} tracks")

    for i, track in enumerate(tracks):
        asset_id = track.get("assetId")
        store_track(get_track(asset_id))

        if i % 20 == 0:
            app.logger.info(f"Updated {i+1} of {len(tracks)} tracks")

    return "task complete"


@app.route("/tasks/test", methods=["GET"])
def test_task():
    doglist = get_matching_tracks("dogsAllowed","Dogs allowed. Keep dog under control at all times.")

    return str(doglist)


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)
# [END gae_python3_render_template]
# [END gae_python38_render_template]
