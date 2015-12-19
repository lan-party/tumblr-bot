# tumblr-bot
A simple bot that scrapes images and uploads them to a blog.
Installation instructions
# 
# 
# 

Config file variables
# smtp server address
# smtp server port
# from email
# email password
# send/post email
# number of images to download (max 8)
# outer loop save location
# inner loop save location
# number of total posts
# image file type
# sleep time(hours)

Bot program flow overview
# loop1(outer loop variable +1){
#  clear data;
#  write tags to data.txt(a);
#  split data.txt to list;
#  loop2(inner loop variable +1){
#   ctag = data[inner loop variable];
#   download images from tags(inner loop variable);
#   post images with tags;
#   write variables to config;
#  }
#  sleep;
# }
