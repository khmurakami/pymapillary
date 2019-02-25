# pymapillary

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Build Status](https://travis-ci.com/khmurakami/pymapillary.svg?token=GdqQUUu1xsypr1oorMoh&branch=master)](https://travis-ci.com/khmurakami/pymapillary)

Python Wrapper for Mapillary API V3

## Requirements

Also listed in requirements.txt:

- requests==2.21.0
- wget==3.2

## Install

#### Install Locally

This was only tested in Python 3.6

```shell
$ python3 setup.py install
```

#### Install inside a virtualenv
```shell
$ pip3 install virtualenv
$ python3 -m virutalenv env
$ source env/bin/activate
$ python3 setup.py install
```
## Using the Python Wrapper

Descriptions of functions can be found inside pymapillary/pymapillary.py

```python
from pymapillary import Mappilary

maps = Mappilary()

image_json = maps.search_images("13.0006076843,55.6089295863)


# Output  = 200 if the call went through sucessfully
```

Response:
```json
```

## Samples

Code samples can be found examples_code/python_scripts

## Testing using Unit Tests

Run test script to test if it works properly

```shell
$ python unit_test/pystocktwits_test.py
```

## Using Curl Requests to Test

These curl requests are from the Mapillary and are not mine. They can be found here: <https://www.mapillary.com/developer/api-documentation/#introduction>

```
$ cd example_curl_requests
$ ./pagnation_example.sh
```

## Notes

sample_image_detections is not tested because I don't have access to it


## TODO

- Clean up example code
- Have example parsing json
- Make README.md better
- Add test cases
