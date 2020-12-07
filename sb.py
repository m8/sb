import glob
import re
import os

name = "name"
address = "https://github.com"
directory= "blog/"
css = "../assets/stylesheet/main.css"
html_lang = "en"

# Get Blog Pages Under Blog
files = glob.glob("./blog/*.html")
pat = r'.*?\[(.*)].*'

posts={}

def createUrl(text):
    return re.sub(r'[\W_]+', '_', text.lower())

# create blog pages
for blog_post in files:
    f = open(blog_post, "r")
    post = f.read()
    header = re.search(r'.*?Title\[(.*)].*',post)
    date = re.search(r'.*?Date\[(.*)].*',post)
    if(header.group(1) != None and date.group(1) != None):
        header_name = header.group(1)
        date_name = date.group(1)
        posts[date_name] = header_name
        with open("./public/{}{}_{}.html".format(directory,createUrl(header_name),date_name), 'w+') as f:
            f.write("""<!DOCTYPE html>\n<html lang=\"{}\">\n<head>\n<title>{}</title>\n<link rel='stylesheet' type='text/css' href='{}'>\n<meta charset='utf-8'/>\n</head>\n<body>\n<h1>{}</h1>\n<!-- SBc -->{}<!-- SBc -->\n</body>\n\n</html>""".format(html_lang,header_name,css,header_name,post))

posts = sorted(posts.items(), reverse=True) 

# create blog index
blog_index = open("./public/blogindex.html","r+")
blog_index.seek(0)
index_lines = blog_index.readlines()
# it should directly get SB from lines
lc = index_lines.index("<!-- SB -->\n")
line = ""
for s in posts:
    line += "\n" +  "<li>{} &ndash; <a href=\"blog/{}_{}.html\">{}</a></li>\n".format(s[0],createUrl(s[1]),s[0],createUrl(s[1]))
index_lines[lc] += line
with open('./public/blogindex.html', 'w') as file:
    file.writelines( index_lines )