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
import csv

number_to_check = "0732734971"

get = Get()

article_links =[]
article_links = get.article_links()

phone_numbers = []
phone_numbers = get.phone_numbers(article_links=article_links)


check = Check(phone_numbers=phone_numbers, links=article_links, number_to_check=number_to_check)
check.number()

print(phone_numbers)
print(article_links)

test = zip(phone_numbers, article_links)

with open('numbers.csv', 'w+', newline="") as csvfile:
    csv_out = csv.writer(csvfile, delimiter=",")
    for row in test:
        csv_out.writerow(row)
        print(row)

