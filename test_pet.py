from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''
def test_pet_schema():
    test_endpoint = "/pets/1"

    response = api_helpers.get_api_data(test_endpoint)

    assert response.status_code == 200

    # Validate the response schema against the defined schema in schemas.py
    validate(instance=response.json(), schema=schemas.pet)

'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''
# statuses that i found in the schemas.py file have been added to the status param
@pytest.mark.parametrize("status", ["available", "sold", "pending"])
def test_find_by_status_200(status):
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": status
    }

# in the endpoint of /pets/findByStatus that is indicated by "test_endpoint", we want to test the status indicated by the "params"
    response = api_helpers.get_api_data(test_endpoint, params)
    # checking for a 200 status. 200 means the site is up and active.
    assert response.status_code == 200
    # with pets we will gather the .json data
    pets = response.json()
    # now we make a for loop where we will check the status for the site on every pet 
    for pet in pets:
        assert pet["status"] == status
        validate(instance=pet, schema=schemas.pet)

'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id}
2) Parameterizing the test for any edge cases
'''
# to test pet id and to see id the site is 404 i used 3 separate numbers that are likely never used ID: 0, -1, 99999. so it 'should' 404
# UPDATE: i guess 0 is an ID? it returned as failed so thats 200, removed 0 from the array
@pytest.mark.parametrize("pet_id", [-1, 99999])
# i also set the name to be pet_id so i just plug that into the '()'
def test_get_by_id_404(pet_id):
    # the end point given by the task in step 1.
    test_endpoint = f"/pets/{pet_id}"
    # collect the respones from the test point 
    response = api_helpers.get_api_data(test_endpoint)
    # lastly lets make sure the respone is 404
    assert response.status_code == 404
    # not my code below but ill explain it anyways. if its 404 return a 'pass'
    pass