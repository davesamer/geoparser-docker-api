from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)


# This should work
def test_geoparse_good_example():
    response = client.post(
        "/geoparse/",
        json={"page": "www.example.org",
              "title": "Newsarticle2",
              "time": "2023-11-08",
              "author": "",
              "content": "Austria is a nice contry"}
    )
    assert response.status_code == 200
    assert response.json() == {"page": "www.example.org",
                               "title": "Newsarticle2",
                               "time": "2023-11-08",
                               "author": "",
                               "content": "Austria is a nice contry",
                               "location_information": [{
                                   "placename": "Republic of Austria",
                                   "longitude": 13.33333,
                                   "latitude": 47.33333,
                                   "geonameid": "2782113"
                               }]}


def test_bad_example():
    pass
