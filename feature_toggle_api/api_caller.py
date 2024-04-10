import requests

# Define the base URL of your API
base_url = 'http://localhost:8000/api/v1/'

def get_feature_toggles_by_creator(creator_id):
    creator_endpoint = f'toggles/?created_by={creator_id}'
    creator_url = base_url + creator_endpoint

    creator_response = requests.get(creator_url)

    if creator_response.status_code == 200:
        # If the request was successful, return the response data
        return creator_response.json()
    else:
        # If there was an error, print the status code and error message
        print(f"Error fetching feature toggles by creator: {creator_response.status_code} - {creator_response.text}")
        return None

def update_all_feature_toggles_for_user(creator_id, new_status):
    toggles = get_feature_toggles_by_creator(creator_id)

    if toggles:
        for toggle in toggles:
            toggle_id = toggle['id']
            update_feature_toggle_status(toggle_id, new_status)

def update_feature_toggle_status(toggle_id, new_status):
    status_update_endpoint = f'toggles/{toggle_id}/'
    status_update_url = base_url + status_update_endpoint

    # Payload to update the status of the feature toggle
    payload = {
        "is_enabled": new_status  # Set the new status here
    }

    update_response = requests.patch(status_update_url, json=payload)

    if update_response.status_code == 200:
        return True
    else:
        print(f"Error updating feature toggle status: {update_response.status_code} - {update_response.text}")
        return False

# Example usage
creator_id = 1  # Replace with the ID of the creator
new_status = True  # Set the new status here
update_all_feature_toggles_for_user(creator_id, new_status)
