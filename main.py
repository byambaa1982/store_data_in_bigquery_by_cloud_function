from google.cloud import storage
import pandas


# project_id = '[your project ID]'
project_id='my-bigquery-lab-286400'
bucket_name = 'my-bigquery-lab-286400_cloudbuild'
# bucket_name=event['bucket']
# blob_name=event['name']
client = storage.Client()



df = pandas.DataFrame(
    {
        'my_string': ['a', 'b', 'c'],
        'my_int64': [11, 21, 31],
        'my_float64': [14.0, 15.0, 16.0]
    }
)

df.to_csv("my_file.csv", index=False)
client = storage.Client()
bucket = client.get_bucket(bucket_name)
blob = bucket.blob("my_file.csv")
blob.upload_from_filename("my_file.csv")


# def data_to_bq(request):
#     """Responds to any HTTP request.
#     Args:
#         request (flask.Request): HTTP request object.
#     Returns:
#         The response text or any set of values that can be turned into a
#         Response object using
#         `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
#     """
#     request_json = request.get_json()
#     if request.args and 'message' in request.args:
#         client = storage.Client()
#         bucket = client.get_bucket(bucket_name)
#         blob = bucket.blob(my_file)
#         return blob
#     elif request_json and 'message' in request_json:
#         return request_json['message']
#     else:
#         return f'Hello World!'