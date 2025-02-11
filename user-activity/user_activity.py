import sys
import requests

def common_events(username):
  url = f"https://api.github.com/users/{username}/events"
  path = "Roadmap Developer/user-activity/"

  data = []   
  r = requests.get(url)

  if r.status_code == 200:
    data = r.json()
    for event in data:
      type_event = event["type"]
      if type_event == "PushEvent":
        print(f'- Pushed to {event["repo"]["name"]}')
      elif type_event == "IssuesEvent":
        print(f'- Create issue number {event["payload"]["issue"]["number"]}')
      elif type_event == "IssueCommentEvent":
        print(f'- Commented on issue {event["payload"]["issue"]["number"]}')
      elif type_event == "WatchEvent":
        print(f'- Starred {event["repo"]["name"]}')
      elif type_event == "PullRequestEvent":
        print(f'- Pull request {event["payload"]["action"]}. Number {event["payload"]["number"]}')
      elif type_event == "CreateEvent":
        print(f"- Created {event["payload"]["ref_type"]} {event["payload"]["ref"]}")
      else:
        print(f"- Event {event["type"]}")
  else:
    print(f"Error to obtain the data for user {username}: {r.status_code}")

if __name__ == '__main__':
  if len(sys.argv) > 1:
    common_events(sys.argv[-1])
  else:
    print("Add the GitHub username in the command line.")