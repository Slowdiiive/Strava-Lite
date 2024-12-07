import requests
import json

BASE = "http://127.0.0.1:5000"

def create_user(name, age):
    response = requests.post(f"{BASE}/user", json={"name": name, "age": age})
    print(f"Status code for creating {name}: {response.status_code}")
    print(json.dumps(response.json(), indent=2))
    return response.json()["id"]

# Register users
response_id_1 = create_user("Ethan", 26)
response_id_2 = create_user("Lee", 24)
response_id_3 = create_user("Eva", 25)

# Get id2 info
response_get = requests.get(f"{BASE}/user/{response_id_2}")
print(f"Status code for Get User 2: {response_get.status_code}")
print(json.dumps(response_get.json(), indent=2))

# Remove id1
response_remove = requests.delete(f"{BASE}/user/{response_id_1}")
print(f"Status code for Delete User 1: {response_remove.status_code}")
print(json.dumps(response_remove.json(), indent=2))

# List users
response_list = requests.get(f"{BASE}/users")
print(f"Status code for List Users: {response_list.status_code}")
print(json.dumps(response_list.json(), indent=2))

# Add workout to id2&3
response_update = requests.put(f"{BASE}/workouts/{response_id_2}", json={
    "date": "2024-12-02",
    "distance": "3km",
    "time": "00:45:00",
})
print(f"Status code for Add Workout: {response_update.status_code}")
print(json.dumps(response_update.json(), indent=2))

response_update = requests.put(f"{BASE}/workouts/{response_id_3}", json={
    "date": "2024-12-04",
    "distance": "2km",
    "time": "00:30:00"
})
print(f"Status code for Add Workout: {response_update.status_code}")
print(json.dumps(response_update.json(), indent=2))

# List id2's workout
response_list = requests.get(f"{BASE}/workouts/{response_id_2}")
print(f"Status code for List Workouts: {response_list.status_code}")
print(json.dumps(response_list.json(), indent=2))

# id2 follows id3
response_list = requests.get(f"{BASE}/follow-list/{response_id_2}")
print(f"Status code for Follow List: {response_list.status_code}")
print(json.dumps(response_list.json(), indent=2))

# id2 wants to see id3's workout
response_list = requests.get(f"{BASE}/follow-list/{response_id_2}/{response_id_3}")
print(f"Status code for ShowFriendWorkout: {response_list.status_code}")
print(json.dumps(response_list.json(), indent=2))