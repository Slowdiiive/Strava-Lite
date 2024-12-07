from flask import jsonify
from flask_restful import Resource, reqparse, abort
from uuid import uuid4 as generateId

users = {}

create_user_parser = (reqparse.RequestParser()
                      .add_argument("name", type=str, required=True)
                      .add_argument("age", type=int, required=False))

def handle_missing_args(parser):
    try:
        return parser.parse_args()
    except Exception as e:
        abort(400, message="Missing required fields", details=str(e))

# Register User
class RegisterUser(Resource):
    def post(self):
        try:
            name, age = handle_missing_args(create_user_parser).values()
        except Exception as e:
            return {"message": "Missing required fields", "details": str(e)}, 400

        id = str(generateId())
        users[id] = {
            "id": id,
            "name": name,
            "age": age,
            "workouts": [],
            "following": set()
        }
        user_data = {
            key: users[id][key]
            for key in ("id", "name", "age")
        }
        return user_data, 200

# Get User
class GetUser(Resource):
    def get(self, user_id):
        user = users.get(user_id)
        if not user:
            return {}, 404

        user_data = {
            key: user[key]
            for key in ("id", "name", "age")
        }
        return user_data, 200

# Remove User
class RemoveUser(Resource):
    def delete(self, user_id):
        if user_id in users:
            del users[user_id]
            return {}, 200
        return {"message": "No user found"}, 404

# List Users
class ListUsers(Resource):
    def get(self):
        users_datas = []
        for user in users.values():
            user_data = {
                "id": user["id"],
                "name": user["name"],
                "age": user["age"]
            }
            users_datas.append(user_data)

        return users_datas, 200


update_user_parser = (reqparse.RequestParser()
                      .add_argument("date", type=str, required=True)
                      .add_argument("distance", type=str, required=True)
                      .add_argument("time", type=str, required=True))

# Add Workout
class AddWorkout(Resource):
    def put(self,user_id):
        date, distance, time = update_user_parser.parse_args().values()
        workout_data = {
            "date": date,
            "distance": distance,
            "time": time
        }
        user = users.get(user_id)
        if user:
            user["workouts"].append(workout_data)
            return workout_data, 200
        else:
            return {"message": "User not found"}, 404


# List Workouts
class ListWorkouts(Resource):
    def get(self, user_id):
        user = users.get(user_id)

        if user is None:
            return {"message": "No user found"}, 404

        workouts = user.get("workouts", [])

        return {"workouts": workouts}, 200

# Follow Friend
follow_parser = reqparse.RequestParser()
follow_parser.add_argument('follow_id', type=str, required=True)

class FollowFriend(Resource):
    def put(self, user_id):
        args = follow_parser.parse_args()
        follow_id = args['follow_id']

        if follow_id not in users:
            abort(404, message="User to follow not found")

        users[user_id]["following"].add(follow_id)
        return jsonify({"following": list(users[user_id]["following"])})

# Show Friend Workout
class ShowFriendWorkouts(Resource):
    def get(self, user_id, follow_id):

        if follow_id not in users[user_id]["following"]:
            return {"message": "You need to follow this user to view his/her workout"}, 403

        workouts = users[follow_id].get("workouts", [])
        return {"workouts": workouts}, 200
