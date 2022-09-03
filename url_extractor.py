from urllib.request import urlopen

# fuction urlopen for opening some url
page=urlopen("https://youtube.com")
# it will print all the headers of the url (here youtube)
print(page.headers)
