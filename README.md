My GitHub: https://github.com/Slowdiiive/Project
Name: Lijing Li
Email: lli86@stevens.edu
Title: "Strava Live"

Brief Description: 
This project can register, remove users, and view the user list. 
It enables users to add and update their workout data. 
Also, users can follow their friends and view their friends' workouts.

The bugs I met:

1/ When I registered users and try to get their list, the command prompt put:
(.venv) D:\Flask\Strava Live>curl -X GET http://127.0.0.1:5000/users
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p> 

The way I solved: Accidentally, the computer restarted and it can run normally.


2/ When I did the Follow Friend,
(.venv) D:\Flask\Strava Lite>curl -X PUT http://127.0.0.1:5000/follow-list/ceab1c0c-6
48a-41a5-961d-f934fbe01c31 -H "Content-Type: application/json" -d "{\"follow-id\": \"6631fab4-a42d-4cdc-b8a6-87f4ebf23a7c\"}"
{"message": {"follow_id": "Missing required parameter in the JSON body or the post body or the query string"}} 

The way I solved: Changed follow-id to follow_id, and it went correctly. {"following":["6631fab4-a42d-4cdc-b8a6-87f4ebf23a7c"]}

-----------------------------------------
python app.py

Register user:
curl -X post http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{\"name\": \"Ethan\", \"age\": \"26\"}"
curl -X post http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{\"name\": \"Lee\", \"age\": \"24\"}"
curl -X post http://127.0.0.1:5000/user -H "Content-Type: application/json" -d "{\"name\": \"Eva\", \"age\": \"25\"}"

Get user2 info:
curl -X get http://127.0.0.1:5000/user/{response_id2}

Remove user1:
curl -X delete http://127.0.0.1:5000/user/{response_id_1}

List users:
curl -X get http://127.0.0.1:5000/users

Add workout to user2&3:
curl -X PUT http://127.0.0.1:5000/workouts/{response_id2} -H "Content-Type: application/json" -d "{\"date\": \"2024-12-02\", \"time\": \"00:45:00\", \"distance\": \"3km\"}
curl -X PUT http://127.0.0.1:5000/workouts/{response_id3} -H "Content-Type: application/json" -d "{\"date\": \"2024-12-04\", \"time\": \"00:30:00\", \"distance\": \"2km\"}

List user2's workouts:
curl -X get http://127.0.0.1:5000/workouts/{response_id2}

id2 follows id3:
curl -X PUT http://127.0.0.1:5000/follow-list/{response_id2} -H "Content-Type: application/json" -d "{\"follow-id\": \"{response_id3}\"}"

id2 wants to see id3's workout:
curl -X GET http://127.0.0.1:5000/follow-list/{response_id2}/{response_id3}
