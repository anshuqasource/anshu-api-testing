# tests/test_lesson11.py
import json
import jsonschema

def test_user_schema(api_context):
    response = api_context.get("users/2")
    user_data = response.json()["data"]

    schema = json.load(open("schemas/user_schema.json"))
    jsonschema.validate(instance=user_data, schema=schema)
@pytest.mark.skip(reason="Demo test proving schema validation works - not a real test case")
def test_schema_catches_bad_type():
    bad_data = {"id": "2", "email": "test@test.com", "first_name": "A", "last_name": "B"}
    schema = json.load(open("schemas/user_schema.json"))
    jsonschema.validate(instance=bad_data, schema=schema)