import requests as rs

def getJokeFrom_API():
    url = "https://api.freeapi.app/api/v1/public/randomjokes/joke/random"
    response = rs.get(url)
    response = response.json()

    if response ["success"] :
        joke = response.get("data")
        print(joke.get("content"))
    else:
        print("there is some error")

call = False
call = bool(input("press 1 for a random joke:"))

if call:
    getJokeFrom_API()