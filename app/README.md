## Google App Engine Doc For Dogs

### Setting up
Clone this repository and checkout feature/google_app

```bash
git clone https://github.com/mjsqu/doc_for_dogs
cd doc_for_dogs
git checkout feature/google_app
cd app
```

Set up a virtual environment and activate it:

```
python3 -m venv .venv
. .venv/bin/activate
```

Install Python requirements:

```
pip install requirements.txt
```

Run the flask app:

```
python main.py
```

Make updates and go to the browser to see changes. Generally changes to the Javascript will be visible after a page refresh. If you update the Python and make an error then you may need to re-run the flask app again once the errors are fixed.

### TODO - Leaflet!

Set up Leaflet in the `static/script.js` file or the `templates/index.html` file