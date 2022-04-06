# accept cookies
# press 50 per page
# get number of pages
# feed this number of pages into get article links functions' while
# make a function to get all article links from 200+ pages
# make another function which takes all links from previous function and access each link
# check to see if ioana's phone is in there
# if it is, show the link
from get import Get

get = Get()

article_links =[]
article_links = get.article_links()

phone_numbers = []
phone_numbers = get.phone_numbers(article_links=article_links)

print(len(phone_numbers))
print(phone_numbers)

