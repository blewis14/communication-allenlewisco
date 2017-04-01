import requests, json, base64, time
from psswd import user, key

VERSION = "0.1.2.7"

def addMessage(datum,
               url="https://api.github.com/repos/blewis14/communication-allenlewisco/contents/messages.txt",
               msg="Add a message"):
    sha = json.JSONDecoder().decode(requests.get(url).text)["sha"]
    content = base64.b64decode((requests.get(url).json())["content"].encode())
    stamp = time.asctime(time.localtime(time.time()))
    string = base64.b64encode(content + "[" + stamp + "] " + datum + "\n")
    data = {"message" : msg, "content" : string, "sha" : sha}
    requests.put(url, json=data, auth=(user, key))

def getMessages(url="https://api.github.com/repos/blewis14/communication-allenlewisco/contents/messages.txt"):
    return base64.b64decode(requests.get(url, data={"path":url, "ref":"master"}).json()["content"].encode())

print "======================================================="
print "============= Communication - A&L Company ============="
print "=== Created by Brendan E. Lewis (blewis14 @ GitHub) ==="
print "=================== Version " + VERSION + " ==================="

while 1:
    print "======================================================="
    print "Select an option:"
    print "1. View all messages (warning: may be very long)"
    print "2. View last 10 messages"
    print "3. Add a message"
    print "4. Exit Communication"
    inp = int(input("Your choice: "))
    if (inp == 1):
        print "==================== All Messages: ===================="
        print getMessages().rstrip('\n')
    elif (inp == 2):
        print "=================== Latest Messages ==================="
        msgs = getMessages().rstrip('\n')
        msgList = msgs.split("\n")
        if (len(msgList) < 10):
            print msgs
        else:
            last10 = msgList[len(msgList) - 10 : len(msgList)]
            prnt = ""
            for i in last10:
                prnt += i + '\n'
            print prnt.rstrip('\n')
    elif (inp == 3):
        try:
            datum = str(raw_input("What is the message? "))
        except EOFError:
            print "Unexpected error. (An EOFError, in fact.) Try inputting your message again later!"
        addMessage(datum)
    elif (inp == 4):
        print "===================== Exiting.... ====================="
        time.sleep(0.5)
        break
    else:
        print "Invalid Input. Try putting in a number."
