from jsonschema import validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_


'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
# not too confident about my approach to this. the task didnt say i needed to make the order than PATCH the order but thats what i did
@pytest.mark.parametrize("new_status", ["sold"])
def test_patch_order_by_id(new_status):
    # here im creatign that data for the order
    new_order_data = {
        "pet_id": 0,
        "quantity": 1,
        "status": "pending"
    }
    # here i post the order
    create_response = api_helpers.post_api_data("/store/order", new_order_data)
    # making sure the site is active (general stuff)
    assert create_response.status_code == 201
    # collect the .json data
    created_order = create_response.json()
    # geting the ID from the post
    order_id = created_order.get("id")

    # now i do the ACTUAL task
    # defining new update
    send_new_update = {"status": new_status}
    # defining the end point
    test_endpoint = f"/store/order/{order_id}"
    # patching to the end point
    response = api_helpers.patch_api_data(test_endpoint, send_new_update)
    # just make sure the site is still looking good after the patch
    assert response.status_code == 200
    # grab the data
    result = response.json()
    # making sure the message is proper
    assert result.get("message") == "Order and pet status updated successfully"
    # if all above is acurate return as pass
    pass


# pytest pytest-api-example/test_store.py -v --html=report.html