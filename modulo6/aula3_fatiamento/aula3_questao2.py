
urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

dominios = []

for i in urls:
    dominios.append(i.split(".")[1])

print(dominios)