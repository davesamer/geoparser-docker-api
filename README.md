## Mordecai3 as containerized API service

### How to use

1. Download the pre-built geonames_index and save the in the project directory
   https://drive.google.com/drive/folders/1h-iQY_y9A4IYUUdX8h-epGIVl4ZF_uu5?usp=drive_link

2) Start the service with the following command

```
docker compose up
```

3. After that the API endpoint is accessible under
   http://localhost:8080/geoparse/

The following code shows an example how make request to the mordecai 3 API in python

```python
    import requests


    item = {
        "page": "test",
        "title": "test title",
        "time": "test time",
        "author": "test author",
        "content": "Austria & Germany are both really beautiful countries"
    }

    URL = 'http://localhost:8080/geoparse/'
    response = requests.post(URL, json=item)
    results = response.json()

```

The output should look like this

```json
{
  "page": "test",
  "title": "test title",
  "time": "test time",
  "author": "test author",
  "content": "Austria & Germany are both really beautiful countries",
  "location_information": [
    {
      "geonameid": "2782113",
      "placename": "Republic of Austria",
      "longitude": 13.33333,
      "latitude": 47.33333
    },
    {
      "geonameid": "2921044",
      "placename": "Federal Republic of Germany",
      "longitude": 10.5,
      "latitude": 51.5
    }
  ]
}
```

#### Next steps:

Deployment

- Migrate to gitlab
- API should read the file path and not the json file
- Output should follow a certain standard (ask franz again); spans should be included
- Create more tests

Geoparser Development

- Integrate mordecai2 (2)
- Integrate geoparsepy (3)

Fix bugs

- Why does mordecai3 does not return any geoentities for some longer texts, although there clearly are geoentities in the text?
- Fix Timeouts from elasticsearch - they are occuring somehow random.
