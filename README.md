# ABC Ecommerce
## Abc Api
The api for backend part of ABC Ecommerce. It's simply reading the data from csv and process into the summarized format. It's developed by using these technologies.
- (Python 3.9.6|https://docs.python.org/release/3.9.6/) (or later) 
- (Flask project|https://flask.palletsprojects.com/en/2.0.x/)
### Start the api
```
$ pip install flask
$ pip install flask-restful
$ cd abc_api
$ python abc_webapi.py
```
### Endpoints
- GET: http://localhost:5000/ecommerceData
- GET: http://localhost:5000/summarizedEcommerceData

## Abc Web
The user interface for abc user can access the data, visualize the data into graph format with summary data table. The frontend is a single page application "index.html".It's developed by using these technologies.
- (Bootstrap 5|https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- (Highcharts|https://www.highcharts.com/)