import pytest
import random
import json
from pydoc import locate
from faker import Faker
from playwright.sync_api import APIRequestContext
from src.endpoints.config_context import api_request_context
from src.endpoints.dogs import dogs_delete_id, dogs_get, dogs_post, dogs_get_id
from src.utils.match import match_structure, match_values

fake = Faker()
structures =  json.load(open('src/fixtures/api_structure.json'))


# Verify a Dog is correctly created
def test_dogs_post_create_a_dog(api_request_context: APIRequestContext):
  data = {
    "breed": fake.name(),
    "age":   random.randrange(0,20),
    "name":  fake.name()
  }
  response = dogs_post(api_request_context, data)
  assert response.status == 200
  assert match_structure(structures["dogs"]["post"], response.json())
  assert match_values(data, response.json())

# Verify 415 when missing data
def test_dogs_post_missing_data(api_request_context: APIRequestContext):
  data = {
  }
  response = dogs_post(api_request_context, data)
  assert response.status == 415

# Verify 422 when missing data
def test_dogs_post_incorrect_data_type(api_request_context: APIRequestContext):
  data = {
    "breed": fake.name(),
    "age":   fake.name(),
    "name":  random.randrange(0,20)
  }
  response = dogs_post(api_request_context, data)
  assert response.status == 422

# Verify an existing dog can be retrieved
def test_dogs_get_id_retrieve_dog(api_request_context: APIRequestContext):
  data = {
    "breed": fake.name(),
    "age":   random.randrange(0,20),
    "name":  fake.name()
  }
  response = dogs_post(api_request_context, data)
  id = response.json()['id']
  response = dogs_get_id(api_request_context, id)
  assert response.status == 200
  assert match_structure(structures["dogs"]["get_id"],response.json())
  assert match_values(data, response.json())

# Verify 404 on non existing dog
def test_dogs_get_id_non_existing_dog(api_request_context: APIRequestContext):
  response = dogs_get_id(api_request_context, random.randrange(1000,10000))
  assert response.status == 404

# Verify a list of dogs can be retrieved
def test_dogs_get_retrieve_list(api_request_context: APIRequestContext):
  response = dogs_get(api_request_context)
  assert response.status == 200

# Verify a dog can be deleted
def test_dogs_delete_id_a_dog_is_deleted(api_request_context: APIRequestContext):
  data = {
    "breed": fake.name(),
    "age":   random.randrange(0,20),
    "name":  fake.name()
  }
  response = dogs_post(api_request_context, data)
  id = response.json()['id']
  response = dogs_delete_id(api_request_context, id)
  assert response.status == 200
  assert match_structure(structures["dogs"]["delete_id"],response.json())
  assert match_values(data, response.json())

# Verify 404 on non existing dog
def test_dogs_delete_id_non_existing_dog(api_request_context: APIRequestContext):
  response = dogs_delete_id(api_request_context, random.randrange(1000,10000))
  assert response.status == 404

