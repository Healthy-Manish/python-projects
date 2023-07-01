# import urlib
# use urlib.request to get the data from the url
# write a function that takes a url 
# returns a response

import urllib.request as urlib
 

def main(url):
    print("Checking connectivity ")
    response = urlib.urlopen(url)
    print("connected to "+url+" successfully")
    print("The response code was: ",response.getcode())


print("This is a site connectivity program")
input_url = input(("Input the url of the site: "))
main(input_url)
