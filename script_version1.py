"""
Script V1
=====
  A simple script that uses the wikipedia API to search for a user-inputted
  term and returns the top 5 results with their corresponding URLs in a JSON
  format.
  
Notes:
  a bit janky at times, searches the ENTIRE wikipedia for results which is not great
  in terms of accuracy, but atleast is a psudeo-search engine? idk man, this
  thing has the potential to be good and terrible at the same time.

  i dont know how you would format the JSON request and i assume you
  know how to convert it into a python variable. send me an example JSON and
  you better keep the formatting consistent
"""
userinput = "paris"

# imports

import wikipedia
import json

# functions

def debug(results):
  for i in results:
    try:
      link = wikipedia.page(i).url
    except:
      link = None
    
    print(f"{i:30} | {link}")

# variables

link = [] # list of links
results = [] # list of results
count = 0 # while loop counter

tojson = {} # dictionary to store results

# main

wikipedia.set_lang("en")

# try to use built-in autocorrect, if it fails its most likely correctly spelled
try:
  results = wikipedia.search(userinput, results = 10)
except:
  results = wikipedia.search(wikipedia.suggest(userinput), results = 10)

# remove duplicates (results with the same URL)
for i in results:
  try:
    link.append(wikipedia.page(i).url)
  except:
    link.append("ERROR: could not retrieve link")

# parse through URLS and results, remove duplicates
while count+1 < len(link):
  if link[count] == link[count+1]:
    link.pop(count)
    results.pop(count)
    
  count += 1

# convert into a dictionary
count = 0
for a,b in zip(results, link):
  tojson[a] = b
  count += 1
  
  if count > 4:
    break

debug(results)

# export as JSON
with open(r'results.json', 'w') as file:
  json.dump(tojson, file, indent = 2)