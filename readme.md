# sb
sb stands for simple blog or blog index creator script written with python highly influenced from [lb](https://github.com/lukesmithxyz/lb).
sb is not complete blog system like lb. In sb you can just create blog index pages and posts from source files. Its written in python hence its easy to configure but not so efficient way to create blogs. 

## Folders
```
-blog
--example1.html
--example2.html
-public
--blog_index.html
--blog/
---example1_2020.html
---example2_2020.html
```

## In Blog Folder
In the blog folder, you can write HTML whatever you want. It will be replaced inside of a templated HTML file. You should fill the 'Date' and 'Title' of each source files like that:
```
<!-- Title[ Simple Blog 1 ] -->
<!-- Date[2020-08-08] -->

It's test file
```

## In Index Page
You can use ```<!-- SB -->``` in blogindex.html file, and run 
```
python3 sb.py
``` 
your blog post will be listed under ```<!-- SB -->``` line.

## Todo
* Sort by date
* Some kind of history file to track unnecessary file creation
* RSS feed

