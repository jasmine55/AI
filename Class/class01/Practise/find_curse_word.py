import urllib
def read_text():
    #open file
    quotes = open("/Users/mac/Desktop/AI/Python/Practise/movie_quotes/movie_quotes.txt")
    content_of_file = quotes.read()
    quotes.close()
    return content_of_file
    #check the curse word using google url
content_of_file = read_text()

def check_profinity(text_to_check):
    # print text_to_check
    # connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+ text_to_check)
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=shit")
    output = connection.read()
    print(output)
    connection.close()

# check_profinity(content_of_file)
check_profinity(content_of_file)
