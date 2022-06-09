## CutLink's

**CutLink's** is a **URL Shortner** built using **Python** (**Flask**) that helps user to shorten therir URL both using **Website** and **API** calls.

![CutLink's Homepage](/Extras/Homepage.png "CutLink's Homepage")

## Features

- 

## Installation

CutLinks requires [Python 3](https://www.python.org/) to run.

Follow the following steps to start the server.

```sh
git clone https://github.com/harshitgarg02/CutLinks.git
cd cutlinks
pip install -r requirements.txt
```

Change the values of variable in config.py [Currently Filled with Sample Data], After changing start the server with 

```sh
python run.py
```

## Api Documentation

#### URL Shortening
Request:
```
POST /api/shorten
```
Parameters:
```
long_url : URL that needs to be shortened.
```
Optional Parameters:
```
api_key : Token that you get when you register on our website.
custom_url : Custom Slug if needed.
```
Example Request:
```
POST https://cutlinks.herokuapp.com/api/shorten/?api_key=8f6f3c862eb7135b48d1c12b229ed5c3012f68930a43ae07e3280dd8f878d6f4&long_url=https://cutlinks.herokuapp.com/&custom_url=homepage
```
Example Response:
```sh
{
    "status": 200,
    "message": "Request Sucessfully Executed.",
    "data": {
        "Short URL": "https://cutlinks.herokuapp.com/homepage",
        "Destination URL": "https://cutlinks.herokuapp.com/"
    }
}
```
#### Get URL Info
Request:
```
GET /api/getinfo
```
Parameters:
```
short_url : Shortened URL whose data needs to be Fetched.
```
Optional Parameters:
```
api_key : Token that you get when you register on our website.
```
Example Request:
```
GET https://cutlinks.herokuapp.com/api/getinfo/?api_key=8f6f3c862eb7135b48d1c12b229ed5c3012f68930a43ae07e3280dd8f878d6f4&short_url=https://cutlinks.herokuapp.com/homepage
```
Example Response:
```sh
{
    "status": 200,
    "message": "Request Sucessfully Executed.",
    "data": {
        "Short URL": "https://cutlinks.herokuapp.com/homepage",
        "Destination URL": "https://cutlinks.herokuapp.com/",
        "No. of Clicks": 10,
        "Created At": "2022-05-11 22:16:09.584971+00:00"
    }
}
```

## License

MIT
