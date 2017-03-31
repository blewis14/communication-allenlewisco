import requests, json, base64, time
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
    sha = json.JSONDecoder().decode(requests.get(url).text)["sha"]
    content = base64.b64decode((requests.get(url).json())["content"].encode())
    stamp = time.asctime(time.localtime(time.time()))
    string = base64.b64encode(content + "[" + stamp + "] " + datum + "\n")
    data = {"message" : msg, "content" : string, "sha" : sha}
    requests.put(url, json=data, auth=("blewis14", key))

if __name__ == "__main__":
    datum = str(raw_input("What do you want to put in the file? "))
    append(datum)
