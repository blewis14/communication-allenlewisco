import requests, json, base64
from io import StringIO
from psswd import key

def write(datum,
          url="https://api.github.com/repos/blewis14/communication-allenlewisco/contents/messages.txt",
          msg="Update messages.txt"):
    sha = json.JSONDecoder().decode(requests.get(url).text)["sha"]
    string = base64.b64encode(datum.encode())

    data = {"message" : msg, "content" : string, "sha" : sha}
    requests.put(url, json=data, auth=("blewis14", key))
    
def append(datum,
           url="https://api.github.com/repos/blewis14/communication-allenlewisco/contents/messages.txt",
           msg="Add a message"):
    raise NotImplementedError("Use the write(datum) method")

if __name__ == "__main__":
    datum = str(raw_input("What do you want to put in the file? "))
    write(datum)
