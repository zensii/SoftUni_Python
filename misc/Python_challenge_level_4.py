import urllib.request
number = 66831
# 16044,82682,66831

while True:
    url = f'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing={number}'
    try:
        request_url = urllib.request.urlopen(url)
        page_text = request_url.read().split()
        print(page_text)
        number = int(page_text[-1])

    except ValueError:
        print(f'Failed at{number}')
        number = number / 2