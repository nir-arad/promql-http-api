# PromQL HTTP API

This python package provides a [Prometheus](https://prometheus.io/) HTTP API client library.
It encapsulates and simplifies the collection of data from a Prometheus server.
One major feature of this library is that responses to queries are returned as [Pandas](https://pandas.pydata.org/) DataFrames.

Prometheus is an open-source system monitoring and alerting toolkit. It collects metrics from configured targets at given intervals, evaluates rule expressions, displays the results, and can trigger alerts if some condition is observed to be true. The Prometheus server exposes an HTTP API for querying the collected data, and a query language called PromQL.

This library is intended to help data scientists who would like to harvest data from a Prometheus server for analysis and visualization. The library is design to be simple to use, and to provide a convenient interface to the Prometheus HTTP API. It is also designed to be performant and scalable, by using the [requests](https://requests.readthedocs.io/en/master/) library and caching HTTP connections to the Prometheus server between API accesses.

For unstable connections, the library supports retrying failed requests. The user may specify the number of retries, the time-out between retries, and the back-off factor for the retry interval.

## Installation

To install as a root user:

```commandline
python3 -m pip install promql-http-api
```

To install as a non-root user:

```commandline
python3 -m pip install --user promql-http-api
```

To uninstall:
```commandline
python3 -m pip uninstall promql-http-api
```

## Usage Examples

Here is a basic usage example:

```python
from promql_http_api import PromqlHttpApi

api = PromqlHttpApi('http://localhost:9090')
q = api.query('up', '2020-01-01T12:00:00Z')
df = q.to_dataframe()
print(df)
```

On the first line we create a PromqlHttpApi object named `api`. This example assumes that a Prometheus server is running on the local host, and it is listening to port 9090.
Replace this URL as needed with the appropriate URL for your server.

Next, we use the `api` object to create a Query object named `q`. The `query()` function takes two parameters: a query string and a date-time string.

To execute the query explicitly, without converting the result to a DataFrame, you can use:
```python
# Execute the query explicitly
promql_response_data = q()

# Convert the cached result to a DataFrame
df = q.to_dataframe()
```

Alternately, by calling the to_dataframe() method alone, we will implicitly execute the query.

```python
# Execute the query implicitly
df = q.to_dataframe()
```

Adding retries and time-out to the query work only with explicit execution:

```python
# Execute the query explicitly
# with 5 retries and retry intervals of 5, 10, 20, and 40 seconds
promql_response_data = q(retries=5, timeout=5, backoff=2)

# Convert the cached result to a DataFrame
df = q.to_dataframe()
```

## Debugging

If something goes wrong, you can look at the HTTP response and the PromQL response information. Here are some examples:
```python
from promql_http_api import PromqlHttpApi
api = PromqlHttpApi('http://localhost:9090')
q = api.query('up', '2020-01-01T12:00:00Z')
q()
promql_response = q.response
http_response = promql_response.response
print(f'HTTP response status code  = {http_response.status_code}')
print(f'HTTP response encoding     = {http_response.encoding}')
print(f'PromQL response status     = {promql_response.status()}')
print(f'PromQL response data       = {promql_response.data()}')
print(f'PromQL response error type = {promql_response.error_type()}')
print(f'PromQL response error      = {promql_response.error()}')
```

---
# List of Supported APIs

| API                               | Method                                |
|---------------------              |---------------------------------------|
| /api/v1/query                     | query(query, time)                    |
| /api/v1/query_range               | query_range(query, start, end, step)  |
| /api/v1/format_query              | format_query(query)                   |
| /api/v1/series                    | series(match)                         |
| /api/v1/labels                    | labels()                              |
| /api/v1/label/<label_name>/values | label_values(label)                   |
| /api/v1/targets                   | targets(state)                        |
| /api/v1/rules                     | rules(type)                           |
| /api/v1/alerts                    | alerts()                              |
| /api/v1/alertmanagers             | alertmanagers()                       |
| /api/v1/status/config             | config()                              |
| /api/v1/status/flags              | flags()                               |
| /api/v1/status/runtimeinfo        | runtimeinfo()                         |
| /api/v1/status/buildinfo          | buildinfo()                           |


---
# Testing

The package contains limited unit testing.
Run the tests from the package top folder using:

```commandline
pytest
```

---
# Future work

Implement a CI/CD pipeline with a Prometheus instance in a Docker container to test API accesses.

If you use this library and would like to help - please contact the author.

---
# References

[Prometheus / HTTP API](https://prometheus.io/docs/prometheus/latest/querying/api/)
