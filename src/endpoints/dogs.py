from playwright.sync_api import APIRequestContext


def dogs_post(api_request_context: APIRequestContext, data):
  return api_request_context.post(
    "/dogs",
    data=data
  )

def dogs_get(api_request_context: APIRequestContext):
  return api_request_context.get(
    f"/dogs",
  )

def dogs_get_id(api_request_context: APIRequestContext, id):
  return api_request_context.get(
    f"/dogs/{id}",
  )

def dogs_delete_id(api_request_context: APIRequestContext, id):
  return api_request_context.delete(
    f"/dogs/{id}",
  )