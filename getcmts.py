#!/usr/bin/env python
# coding: utf-8

# In[1]:


#reference : https://towardsdatascience.com/how-to-build-your-own-dataset-of-youtube-comments-39a1e57aade


# In[3]:


import json
from csv import writer


# In[4]:


pip install --upgrade google-api-python-client


# In[5]:


pip install tensorflow


# In[6]:


pip install --upgrade google-api-python-client


# In[1]:


import pandas as pd
import pickle
import urllib.request
import urllib


# In[7]:


from googleapiclient.discovery import build


# In[14]:


import pandas as pd
import pickle
import urllib.request
import urllib


# In[20]:


key = 'AIzaSyC-9lNetr41_MI1jDaVTwIcWbO_cxTYMv4' 
videoId = '5cathmZFeXs'
channelId = 'UCeY0bbntWzzVlaj2z3QigXg'


# In[21]:


def build_service():
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"
    return build(YOUTUBE_API_SERVICE_NAME,
                 YOUTUBE_API_VERSION,
                 developerKey=key)


# In[23]:


#2 configure function parameters for required variables to pass to service
def get_comments(part='snippet', 
                 maxResults=100, 
                 textFormat='plainText',
                 order='time',
                 allThreadsRelatedToChannelId=channelId,
                 videoId=videoId,
                 csv_filename="yt_comments"
                 ):

    #3 create empty lists to store desired information
    comments, commentsId, authorurls, authornames, repliesCount, likesCount, viewerRating, dates, vidIds, totalReplyCounts,vidTitles = [], [], [], [], [], [], [], [], [], [], []

    # build our service from path/to/apikey
    service = build_service()
    
    #4 make an API call using our service
    response = service.commentThreads().list(
        part=part,
        maxResults=maxResults,
        textFormat='plainText',
        order=order,
        # videoId=videoId
        allThreadsRelatedToChannelId=channelId
    ).execute()

    while response: # this loop will continue to run until you max out your quota

        for item in response['items']:
            #5 index item for desired data features
            comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
            comment_id = item['snippet']['topLevelComment']['id']
            reply_count = item['snippet']['totalReplyCount']
            like_count = item['snippet']['topLevelComment']['snippet']['likeCount']
            authorurl = item['snippet']['topLevelComment']['snippet']['authorChannelUrl']
            authorname = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
            date = item['snippet']['topLevelComment']['snippet']['publishedAt']
            vidId = item['snippet']['topLevelComment']['snippet']['videoId']
            totalReplyCount = item['snippet']['totalReplyCount']
            vidTitle = get_vid_title(vidId)

            #6 append to lists
            comments.append(comment)
            commentsId.append(comment_id)
            repliesCount.append(reply_count)
            likesCount.append(like_count)
            authorurls.append(authorurl)
            authornames.append(authorname)
            dates.append(date)
            vidIds.append(vidId)
            totalReplyCounts.append(totalReplyCount)
            vidTitles.append(vidTitle)

        try:
            if 'nextPageToken' in response:
                response = service.commentThreads().list(
                    part=part,
                    maxResults=maxResults,
                    textFormat=textFormat,
                    order=order,
                    # videoId=videoId,
                    allThreadsRelatedToChannelId=channelId,
                    pageToken=response['nextPageToken']
                ).execute()
            else:
                break
        except: break

    #9 return our data of interest
    return {
        'comment': comments,
        'comment_id': commentsId,
        'author_url': authorurls,
        'author_name': authornames,
        'reply_count' : repliesCount,
        'like_count' : likesCount,
        'date': dates,
        'vidid': vidIds,
        'total_reply_counts': totalReplyCounts,
        'vid_title': vidTitles
    }


# In[ ]:


# vidid to table name
def get_vid_title(vidid):
    VideoID = "5cathmZFeXs"
    params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % vidid}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        #print(data['title'])
        return data['title']


# In[27]:


import json

# In[29]:


if __name__ == '__main__':
    yt_comments = get_comments()
    df = pd.DataFrame(yt_comments)
    print(df.shape)
    print(df.head())
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['just_date'] = df['date'].dt.date
    df.to_csv('C:/Users/madha/Downloads/SentimentAnalysisYTComments./yt_comments.csv')






