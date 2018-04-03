import webbrowser
import os
import re

movie_list = []

f = open('helloworld.html', 'w')

page = """<html>
<head></head>
<body>
</body>
</html>"""

f.write(page)
f.close()

webbrowser.open_new_tab('D:/Documents/Udacity/movie/helloworld.html')