import requests
import json
import time

URL = 'http://localhost:8080/geoparse/'

if __name__ == "__main__":

    path_to_swc_examples = "../data/_aljazeera_turkey_backup.json"
    path_to_swc_examples_test_results = "../data/swc_examples_test_results.json"

    # path_to_swc_examples = "../data/test_example.json"
    # path_to_swc_examples_test_results = "../data/test_example_results.json"

    # load data
    f = open(path_to_swc_examples, encoding='utf-8')
    swc_examples = json.load(f)

    test_results = {}

    # iterate over items
    for i, item in enumerate(swc_examples):

        time.sleep(10)

        # count nr of signs in content attribute
        nr_characters_content = len(item["content"])

        # make request and start timing
        time_start = time.time()
        response = requests.post(URL, json=item)
        time_processing = time.time() - time_start

        # countr nr of retrieved geoentities
        results = response.json()
        nr_geo_ents = len(results["location_information"])

        id_ = f"article_{i}"
        test_results[id_] = {"text_length": nr_characters_content,
                             "processing_time": time_processing,
                             "retrieved_geo_entities": nr_geo_ents}
        print(test_results[id_])

    with open(path_to_swc_examples_test_results, "w") as outfile:
        json.dump(test_results, outfile)
