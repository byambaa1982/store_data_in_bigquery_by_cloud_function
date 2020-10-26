---
title: "Store data in Cloud BigQuery using Cloud Function"
date: 2020-10-26 11:33:00 +0800
categories: [Google Cloud Function, Python]
tags: [pandas, lambda, cloud engineering]
---


## Move data to Cloud BigQuery using Cloud Function




```python
from google.cloud import bigquery
import pandas


# project_id = '[your project ID]'
project_id='my-bigquery-lab-286400'

df = pandas.DataFrame(
    {
        'my_string': ['a', 'b', 'c'],
        'my_int64': [11, 21, 31],
        'my_float64': [14.0, 15.0, 16.0]
    }
)
client = bigquery.Client(project=project_id)
table_id = 'practice.df_to_bq'
# Since string columns use the "object" dtype, pass in a (partial) schema
# to ensure the correct BigQuery data type.
job_config = bigquery.LoadJobConfig(schema=[
    bigquery.SchemaField("my_string", "STRING"),
])


def data_to_bq(request):
    """Responds to any HTTP request.
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    if request.args and 'message' in request.args:
        job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
        return job.result()
    elif request_json and 'message' in request_json:
        return request_json['message']
    else:
        return f'Hello World!'
```


If you have anything to ask, please contact me clicking following link?


You can hire me [here](https://www.fiverr.com/coderjs)

Thank you
# store_data_in_bigquery_by_cloud_function
