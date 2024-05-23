import requests
import pytest
import responses

# Base URL
BASE_URL = "https://jsonplaceholder.typicode.com"

# Constants for test data
TEST_POST_DATA = {"title": "test", "body": "test body", "userId": 1}
UPDATED_POST_DATA = {"title": "updated", "body": "updated body", "userId": 1}
INVALID_POST_DATA = {"title": "updated", "body": "updated body", "userId": "one"}
MOCK_POST_ID = 1

@pytest.fixture(scope="function")
def create_post():
    # Setup: Create a new post
    response = requests.post(f"{BASE_URL}/posts", json=TEST_POST_DATA)
    assert response.status_code == 201
    post = response.json()
    post_id = post.get('id')
    yield post_id
    # Teardown: Delete the post
    delete_response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert delete_response.status_code == 200

@responses.activate
def test_create_post():
    # Mock POST response for creating a new post
    responses.add(responses.POST, f"{BASE_URL}/posts",
                  json={**TEST_POST_DATA, "id": MOCK_POST_ID}, status=201)
    # Test creating a new post with valid data
    response = requests.post(f"{BASE_URL}/posts", json=TEST_POST_DATA)
    assert response.status_code == 201
    assert response.json()["title"] == TEST_POST_DATA["title"]

@responses.activate
def test_read_all_posts():
    # Mock GET response for retrieving all posts
    responses.add(responses.GET, f"{BASE_URL}/posts",
                  json=[{**TEST_POST_DATA, "id": MOCK_POST_ID}], status=200)
    # Test retrieving all posts
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert response.json()[0]["title"] == TEST_POST_DATA["title"]

@responses.activate
def test_read_single_post(create_post):
    # Mock GET response for a single post
    post_id = create_post
    responses.add(responses.GET, f"{BASE_URL}/posts/{post_id}",
                  json={**TEST_POST_DATA, "id": post_id}, status=200)
    # Test retrieving a single post by ID using the fixture
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
    assert response.json()["title"] == TEST_POST_DATA["title"]

@responses.activate
def test_update_post(create_post):
    # Mock PUT response for updating a post
    post_id = create_post
    responses.add(responses.PUT, f"{BASE_URL}/posts/{post_id}",
                  json={**UPDATED_POST_DATA, "id": post_id}, status=200)
    # Test updating an existing post with valid data
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=UPDATED_POST_DATA)
    assert response.status_code == 200
    assert response.json()["title"] == UPDATED_POST_DATA["title"]

@responses.activate
def test_update_post_invalid_data(create_post):
    # Mock PUT response for updating a post with invalid data
    post_id = create_post
    responses.add(responses.PUT, f"{BASE_URL}/posts/{post_id}",
                  json={**INVALID_POST_DATA, "id": post_id}, status=400)
    # Test updating an existing post with invalid data
    response = requests.put(f"{BASE_URL}/posts/{post_id}", json=INVALID_POST_DATA)
    assert response.status_code == 400

@responses.activate
def test_delete_post_valid_id(create_post):
    # Mock DELETE response for deleting a post
    post_id = create_post
    responses.add(responses.DELETE, f"{BASE_URL}/posts/{post_id}", status=200)
    # Test deleting an existing post by ID
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200

@responses.activate
def test_delete_post_invalid_id():
    # Mock DELETE response for deleting a post with an invalid ID
    responses.add(responses.DELETE, f"{BASE_URL}/posts/99999", status=404)
    # Test deleting a post with an invalid ID
    response = requests.delete(f"{BASE_URL}/posts/99999")
    assert response.status_code == 404
