# Welcome to Mordecai3-Docker-API

This repository provides a Dockerized version of Mordecai 3, a powerful neural geoparser and event geocoder developed by Andrew Halterman. Mordecai 3 leverages state-of-the-art techniques to accurately extract geographical information from text, making it an invaluable tool for location-based data analysis.

## Credits
The core geoparsing engine, Mordecai 3, is the creation of Andrew Halterman. For more details on the model and its accuracy, refer to the [Mordecai 3 paper](https://arxiv.org/abs/2303.13675).

## Citation
If you use Mordecai 3 in your work, please give proper credit to the developer by citing the following paper:

```latex
@article{halterman2023mordecai,
      title={Mordecai 3: A Neural Geoparser and Event Geocoder}, 
      author={Andrew Halterman},
      year={2023},
      journal={arXiv preprint arXiv:2303.13675}
}
```

## How to use

1. Build the geonames index as described in https://github.com/openeventdata/es-geonames
   Alternatively, you can download a pre-built geonames index [here](https://drive.google.com/drive/folders/1h-iQY_y9A4IYUUdX8h-epGIVl4ZF_uu5?usp=drive_link).
   Extract the folder and save it in project directory.

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
