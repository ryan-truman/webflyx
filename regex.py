import re
urls = ["https://londongrapple.co.uk", "https://google.com", "/test", "#", "/#"]

r = re.compile("^/|#")
results = list(filter(r.match, urls))

print(results)