import requests

# defines a function that sends http(s) request to url and confirms the request is ok
def requestor(url_string):
    try:
        request = requests.get(url_string)
        request.raise_for_status()
        return "thanks ill get working on this"
    except requests.exceptions.RequestException as err:
        raise SystemExit(err)

url_string = input("What url would you like to crawl?")

print(requestor(url_string))