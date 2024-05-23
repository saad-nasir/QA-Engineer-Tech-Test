# Solution to Problem Statement 1

## Overview

The file `crud_script.py` covers some of the basic scenarios that could be tested with the API placeholder, specifically the CRUD operations.

The following table gives an overview of those scenarios. 

| Create (PUT)    | Read (GET)    | Update (POST) |  Delete (DELETE) | 
|--------------|-----------|------------|-------| 
| Create a post with valid data | Retrieve all the posts      | Update a post with valid data       | Delete a post with valid data
|      | Retrieve a single post with a valid ID  | Update a post with invalid data       | Delete a post with invalid data

Each of the operations are implemented by test functions which use a fixture called `create_post()` whose purpose is to create a test post which would be set up and torn down for each test function that uses it. Moreover, this code uses the ``responses`` library to mock HTTP requests and responses. This approach was primarily taken to decouple the tests from the actual external service to ensure that the tests were not affected by the availability or the behavior of the external service.

## How to run this code

1. Ensure that you have the dependancies, namely; `pytest`, `requests` and `responses` installed. These dependancies are listed in the `requirements.txt` file. They can be installed by running the command 
    ``pip install -r requirements.txt``    
2. The CRUD tests can then be executed by running the following command : 
    ``pytest crud_script -v``
3. In case the above command does not work, try : 
    ``python -m pytest crud_script -v``

                                        

