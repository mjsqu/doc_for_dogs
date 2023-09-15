# doc_for_dogs

Store the API Key provided by https://api.doc.govt.nz/ in DOC_API_KEY

## Remutaka Rail Trail Example

```bash
curl -H "x-api-key: ${DOC_API_KEY}" https://api.doc.govt.nz/v1/tracks/885769f9-ea1d-44c5-9dc1-bffa4c931df4/detail | jq -c '.dogsAllowed,.name'
```