# accept cookies
# press 50 per page
# get number of pages
# feed this number of pages into get article links functions' while
# make a function to get all article links from 200+ pages
# make another function which takes all links from previous function and access each link
# check to see if ioana's phone is in there
# if it is, show the link
from get import Get
from check import Check

number_to_check = "0737390048"

get = Get()

article_links =[]
article_links = get.article_links()

phone_numbers = []
phone_numbers = get.phone_numbers()

check = Check(phone_numbers=phone_numbers, links=article_links, number_to_check=)
check.number()

