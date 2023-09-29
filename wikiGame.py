from requests import get

start = input("start URL: ")
goal = input("end URL: ")

# start = "https://en.wikipedia.org/wiki/Water"
# goal = "https://en.wikipedia.org/wiki/Terraria"

visited_urls = []

url_stack = [start] # acts as queue, use pop() and insert()

url_dist = {start: 0}


def get_wiki_urls(url):
    web_page = get(url).text

    index1 = 0

    index2 = 0

    urls = []

    while (True):
        index1 = web_page.find('/wiki/', index2)
        if index1 == -1:
            break

        index2 = web_page.find('"', index1)

        suffix = web_page[index1:index2]

        if not suffix.count(':') + suffix.count('#'):
            urls.append("https://en.wikipedia.org" + suffix)

    return urls

while len(url_stack) > 0:
    current_url = url_stack.pop(0)

    if (current_url in visited_urls):
        continue

    visited_urls.append(current_url)

    next_urls = get_wiki_urls(current_url)

    distance_from_start = url_dist[current_url] + 1

    for url in next_urls:
        if url == goal:
            print("goal reached after " + str(distance_from_start) + " layer(s).")
            exit()
        
        url_stack.append(url)
        url_dist[url] = distance_from_start

print("not found somehow")
