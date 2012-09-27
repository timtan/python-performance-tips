import re

def find_domain(target_url):
    pattern = re.compile("https?://([^/]+)/")
    match = pattern.match(target_url)
    if match :
        return match.group(1)
    return ""

def main():
    cdef char * message = "pyx message"
    target_url = "https://www.google.com/search?q=Enhancement&aq=f&sugexp=chrome,mod=0&sourceid=chrome&ie=UTF-8"
    counter    = {}

    for i in range(1900000):
        domain = find_domain(target_url)  ## It will find www.google.com
        try:
            counter[domain] +=1
        except KeyError:
            counter[domain] = 0
    print "finish " + message

if __name__ == '__main__':
    main()


