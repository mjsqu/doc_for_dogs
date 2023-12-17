## Google App Engine Doc For Dogs

### Running the app

Ensure `.venv` and `.env` files are present in the app directory (see "Setting up" section)
Activate the virtual environment
Run (from the `app` directory):

```
python main.py
```

### Setting up
Clone this repository and checkout feature/google_app

```bash
git clone https://github.com/mjsqu/doc_for_dogs
cd doc_for_dogs
git checkout feature/google_app
cd app
```

While in the `app` directory, set up a virtual environment and activate it:

```
# Linux
python3 -m venv .venv
. .venv/bin/activate
# Windows (PowerShell)
. .venv/Scripts/activate.ps1
```

Add a `.env` file in the `app` directory and add these two values:

```
# Get an API Key from doc.govt.nz
DOC_API_KEY=
# Add your Google Cloud Project name
GOOGLE_CLOUD_PROJECT=
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
