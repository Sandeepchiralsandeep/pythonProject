

'''def fetch_stats(selected_user, processed_data):
    if selected_user != 'Overall':
        processed_data = processed_data[processed_data['user'] == selected_user]
        #fetch the number of messages
        num_messages = processed_data.shape[0]
        #fetch teh total number of words
        words = []
        for message in processed_data['message']:
            words.extend(message.split())

        num_media_messages = processed_data[processed_data['message'] == '<Media omitted>\n'].shape[0]
        #fetch number of links shared
        return num_messages , len(words), num_media_messages'''
'''def fetch_stats(selected_user, processed_data):
    if selected_user != 'Overall':
        processed_data_user = processed_data[processed_data['user'] == selected_user]
        num_messages = processed_data_user.shape[0]
        words = sum(len(message.split()) for message in processed_data_user['message'])
        num_media_messages = processed_data_user[processed_data_user['message'] == '<Media omitted>\n'].shape[0]
        return num_messages, words, num_media_messages
    else:
        num_messages = processed_data.shape[0]
        words = sum(len(message.split()) for message in processed_data['message'])
        num_media_messages = processed_data[processed_data['message'] == '<Media omitted>\n'].shape[0]
        return num_messages, words, num_media_messages'''


import os
import emoji
import pandas as pd
from wordcloud import WordCloud
from collections import Counter
def fetch_stats(selected_user, processed_data):
    if selected_user != 'Overall':
        processed_data_user = processed_data[processed_data['user'] == selected_user]
        num_messages = processed_data_user.shape[0]
        words = sum(len(message.split()) for message in processed_data_user['message'])
        num_media_messages = processed_data_user[processed_data_user['message'] == '<Media omitted>\n'].shape[0]
        num_links_shared = processed_data_user['message'].str.count('http').sum()
        return num_messages, words, num_media_messages, num_links_shared
    else:
        num_messages = processed_data.shape[0]
        words = sum(len(message.split()) for message in processed_data['message'])
        num_media_messages = processed_data[processed_data['message'] == '<Media omitted>\n'].shape[0]
        num_links_shared = processed_data['message'].str.count('http').sum()
        return num_messages, words, num_media_messages, num_links_shared


def most_busy_users(processed_data):
    x = processed_data['user'].value_counts().head()
    df = round((processed_data['user'].value_counts()/processed_data.shape[0])*100 , 2).reset_index().rename(columns = {'index': 'name' , 'user':'percent'})
    return x,df


def create_wordcloud(selected_user , processed_data):
    if selected_user != 'Overall':
        processed_data = processed_data[processed_data['user']== selected_user]
    #wc = WordCloud(width=500 , height=500,min_font_size=10 ,background_color='white')
    # WordCloud
    wc = WordCloud(
        width=800, height=400,
        background_color='white',
        colormap='viridis'
    )
    df_wc = wc.generate(processed_data['message'].str.cat(sep=" "))


   # df_wc = wc.generate(processed_data['message'].str.cat(sep= " "))
    return df_wc


def most_common_words(selected_user, processed_data):
    f = open('stop_hinglish.txt', 'r')
    stop_words = f.read()
    if selected_user != 'Overall':
        processed_data = processed_data[processed_data['user'] == selected_user]
    temp = processed_data[processed_data['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)
    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

'''def emoji_helper(selected_user, processed_data):
    if selected_user != 'Overall':
        df = processed_data[processed_data['user'] == selected_user]
    emojis = []
    for message in processed_data['message']:
        emojis.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])
    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emoji_df
#import emoji '''
def emoji_helper(selected_user, processed_data):
    if selected_user != 'Overall':
        df = processed_data[processed_data['user'] == selected_user]
    emojis = []
    for message in processed_data['message']:
        emojis.extend([c for c in message if c in emoji.UNICODE_EMOJI['en']])
    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emoji_df






'''def monthly_timeline(selected_user , processed_data):
    if selected_user != 'Overall':
        df = processed_data[processed_data['user'] == selected_user]
    timeline = processed_data.groupby(['year' , 'month_num' , 'month']).count()['message'].rest_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time
    return timeline '''
def monthly_timeline(selected_user, processed_data):
    if selected_user != 'Overall':
        df = processed_data[processed_data['user'] == selected_user]
    timeline = processed_data.groupby(['year', 'month_num', 'month']).count().reset_index()
    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))
    timeline['time'] = time
    return timeline



def daily_timeline(selected_user,processed_data):

    if selected_user != 'Overall':
        df = processed_data[processed_data['user'] == selected_user]

    daily_timeline = processed_data.groupby('only_date').count()['message'].reset_index()

    return daily_timeline



def week_activity_map(selected_user,processed_data):
    if selected_user != 'Overall':
        processed_data = processed_data[processed_data['user'] == selected_user]
    return processed_data['day_name'].value_counts()


def month_activity_map(selected_user,df):

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()






def activity_heatmap(selected_user,processed_data):

    if selected_user != 'Overall':
        processed_data = processed_data[processed_data['user'] == selected_user]

    user_heatmap = processed_data.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)

    return user_heatmap

