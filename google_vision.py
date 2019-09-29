from google.cloud import vision
from google.cloud.vision import types
import os
from flask import jsonify


def google_obj():
    """ Create a API object """
    # Set the API credentials
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="creds.json"
    # Instantiate the API object
    return vision.ImageAnnotatorClient()


def google_visions(urls):
    """
    :param urls: string list - urls to the image to infer on

    :return: list - inference outputs
    """
    # Creat API object
    client = google_obj()
    image = vision.types.Image()

    obfuscate = []
    # For each url in the input list
    for url in urls:
        print()
        print(url)
        # Give it the url
        image.source.image_uri = url
        # Infer
        response = client.safe_search_detection(image=image)
        print(response)

        safe = response.safe_search_annotation
        print(safe)
        # If the content is not desirable
        if(safe.adult > 2 or safe.violence > 2 or safe.racy > 2):
            # Tell the client to obfuscate that image
            obfuscate.append(True)
        else:
            obfuscate.append(False)

    return jsonify(obfuscate)

def google_batch(input_image_uri):
    client = google_obj()
    image = vision.types.Image()
    
    source = {'image_uri': input_image_uri}
    image = {'source': source}
    type_ = enums.Feature.Type.LABEL_DETECTION
    features_element = {'type': type_}
    type_2 = enums.Feature.Type.IMAGE_PROPERTIES
    features_element_2 = {'type': type_2}
    features = [features_element, features_element_2]
    requests_element = {'image': image, 'features': features}
    requests = [requests_element]
    gcs_destination = {'uri': output_uri}

    # The max number of responses to output in each JSON file
    batch_size = 2
    output_config = {'gcs_destination': gcs_destination, 'batch_size': batch_size}

    operation = client.async_batch_annotate_images(requests, output_config)

    print('Waiting for operation to complete...')
    response = operation.result()
    print(response)



if __name__ == '__main__':
    image_url = "http://i.imgur.com/Q4eIO90.jpg"
    image_urls = ["http://i.imgur.com/Q4eIO90.jpg",
                  "https://images.theconversation.com/files/205966/original/file-20180212-58348-7huv6f.jpeg?ixlib=rb-1.1.0&q=45&auto=format&w=926&fit=clip",
                  "https://images.theconversation.com/files/205972/original/file-20180212-58327-wqq2vl.jpeg?ixlib=rb-1.1.0&q=30&auto=format&w=754&h=566&fit=crop&dpr=2"]
    print(google_visions(image_urls))
