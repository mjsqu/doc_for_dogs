from dotenv import load_dotenv
from google.cloud import datastore
load_dotenv()

client = datastore.Client()

query = client.query(kind="track")
query.distinct_on = ["dogsAllowed"]
for dog_value in query.fetch():
    print(dog_value['dogsAllowed'])