##This program helps to determine whether a tweet has video, image or other content link in it. This program is developed for disaster situations
## in which we wish to cluster tweets based on the content types. This progam may work with a standalone tweet crawler or on already collected tweets.
## This program takes tweets.tsv file as input (containing all collected tweets) and produces output.tsv as output containing tweets and their associated
## content types.
##    Copyright (C) <2013>  Soudip Roy Chowdhury email: soudeep@gmail.com
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    


import urllib2
import httplib
import re
import sys
import traceback
fileName = "tweets.tsv"
allTweets = open(fileName).readlines()
separator ="\t"
f = open("output.tsv","w")
#list of video hosting sites that you may encounter in tweets
videos = ['youtube', 'vimeo', 'livestream', 'metacafe', 'yahoo! video','video']
#list of image hosting sites that you may encounter in tweets 
images =['twitpic','photobucket','flickr','instagram','yfrog','photo']
category=""
for tweets in allTweets:
    userName,UID,TID,geo,date,text = tweets.strip().split(separator)
    possible_urls = re.findall(r'https?://\S+', text)
    for links in possible_urls:
         try: 
                resp = urllib2.urlopen(links)
                linkarray= resp.geturl()
                longurl=linkarray.encode('utf8')
                
                if any(x in longurl for x in videos):
                    category="Video"
                elif any(x in longurl for x in images):
                    category="Image"
                else:
                    category = "Others"
                    
                strToWrite = userName + separator.encode('utf8')+ UID + separator.encode('utf8') + TID + separator+ geo + separator.encode('utf8') + date + separator.encode('utf8')+ text+ separator.encode('utf8')+longurl+ separator.encode('utf8')+category.encode('utf8')+"\n".encode('utf8')
                
                f.write(strToWrite)
         except urllib2.HTTPError as e:
                                            strToWrite = userName + separator.encode('utf8')+ UID + separator.encode('utf8') + TID + separator+ geo + separator.encode('utf8') + date + separator.encode('utf8')+ text+ separator.encode('utf8')+""+"\n".encode('utf8')
                                            #f.write(strToWrite)
         except urllib2.URLError as e:
                                            strToWrite = userName + separator.encode('utf8')+ UID + separator.encode('utf8') + TID + separator+ geo + separator.encode('utf8') + date + separator.encode('utf8')+ text+ separator.encode('utf8')+""+"\n".encode('utf8')
                                            #f.write(strToWrite)
         except httplib.HTTPException as e:
                                                strToWrite = userName + separator.encode('utf8')+ UID + separator.encode('utf8') + TID + separator+ geo + separator.encode('utf8') + date + separator.encode('utf8')+ text+ separator.encode('utf8')+""+"\n".encode('utf8')
                                                #f.write(strToWrite)
         except Exception:
                            import traceback
                            strToWrite = userName + separator.encode('utf8')+ UID + separator.encode('utf8') + TID + separator+ geo + separator.encode('utf8') + date + separator.encode('utf8')+ text+ separator.encode('utf8')+""+"\n".encode('utf8')
                            #f.write(strToWrite)
        
        
    
    
