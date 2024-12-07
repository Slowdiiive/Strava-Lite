from flask_restful import Api
from constants import *
from api import *

BASE_ROUTE = "/user"
USER_ID_ROUTE = f"{BASE_ROUTE}/<user_id>"

ROUTES = {
    REGISTER_USER: BASE_ROUTE,
    "GetUser": USER_ID_ROUTE,
    "RemoveUser": USER_ID_ROUTE,
    "ListUsers": "/users",
    "AddWorkout": "/workouts/<user_id>",
    "ListWorkouts": "/workouts/<user_id>",
    "FollowFriend": "/follow-list/<user_id>",
    "ShowFriendWorkouts": "/follow-list/<user_id>/<follow_id>"
}

METHODS= {
    REGISTER_USER: "POST",
    "GetUser": "GET",
    "RemoveUser": "DELETE",
    "ListUsers": "GET",
    "AddWorkout": "PUT",
    "ListWorkouts": "GET",
    "FollowFriend": "PUT",
    "ShowFriendWorkouts": "GET"
}

RESOURCES = {
    REGISTER_USER: RegisterUser,
    "GetUser": GetUser,
    "RemoveUser": RemoveUser,
    "ListUsers": ListUsers,
    "AddWorkout": AddWorkout,
    "ListWorkouts": ListWorkouts,
    "FollowFriend": FollowFriend,
    "ShowFriendWorkouts": ShowFriendWorkouts
}

def init_routes(api: Api) -> None:
    for api_name, resource in RESOURCES.items():
        print(f"Adding route: {api_name} with path: {ROUTES[api_name]} and method: {METHODS[api_name]}")
        api.add_resource(resource, ROUTES[api_name], methods=[METHODS[api_name]])
