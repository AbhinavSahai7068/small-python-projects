from urllib.request import urlopen

# fuction urlopen for opening some url
page=urlopen("https://youtube.com")


# the below line has the same functionality as when we inspect the webpage in browser
sourcecode=page.read() 

print(sourcecode)
