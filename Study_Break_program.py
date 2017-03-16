# This program is for take break during study hours
import time
import webbrowser
total_break=3
break_count=0
print ("Study Started on"+time.ctime())
while(break_count<total_break):
    time.sleep(2*60*60)
    webbrowser.open("https://www.youtube.com/watch?v=8DMF0U6xV78")
    break_count=break_count+1
