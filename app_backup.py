import streamlit as st
import helper
import preprocessor

st.sidebar.title("WhatsApp Chat Analyzer")

# Create a file uploader in the sidebar
uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.read()

    # Decode bytes to text (assuming the file is a text file)
    data = bytes_data.decode('utf-8')

    # Preprocess the data using preprocessor.preprocess() method
    processed_data = preprocessor.preprocess(data)

    # Display the processed data
    st.dataframe(processed_data)

    # Fetch unique users
    user_list = processed_data['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    # Use st.columns instead of st.beta_columns
    selected_user = st.sidebar.selectbox("Show Analysis Wrt", user_list)
    if st.sidebar.button("Show Analysis"):
        # Fetch stats using helper.fetch_stats() method
        num_messages, words, num_media_messages, num_links_shared = helper.fetch_stats(selected_user, processed_data)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words)

        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)

        with col4:
            st.header("Links Shared")
            st.title(num_links_shared)

else:
    st.warning("Unable to fetch statistics for the selected user.")

#backup function 2 same function for app.py

import streamlit as st
import helper
import preprocessor
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import io

st.sidebar.title("WhatsApp Chat Analyzer")

# Create a file uploader in the sidebar
uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.read()

    # Decode bytes to text (assuming the file is a text file)
    data = bytes_data.decode('utf-8')

    # Preprocess the data using preprocessor.preprocess() method
    processed_data = preprocessor.preprocess(data)

    # Display the processed data
    st.dataframe(processed_data)

    # Fetch unique users
    user_list = processed_data['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    # Use st.columns instead of st.beta_columns
    selected_user = st.sidebar.selectbox("Show Analysis Wrt", user_list)
    if st.sidebar.button("Show Analysis"):
        # Fetch stats using helper.fetch_stats() method
        num_messages, words, num_media_messages, num_links_shared = helper.fetch_stats(selected_user, processed_data)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words)

        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)

        with col4:
            st.header("Links Shared")
            st.title(num_links_shared)

        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x, new_df = helper.most_busy_users(processed_data)
            fig, (col1, col2) = plt.subplots(1, 2, figsize=(10, 4))

            col1.bar(x.index, x.values, color='red')
            col1.set_xticklabels(x.index, rotation='vertical')
            col1.set_title('Most Busy Users')
            col1.set_xlabel('Users')
            col1.set_ylabel('Number of Messages')

            col2.dataframe(new_df)

            st.pyplot(fig)

        # WordCloud
        st.header("Word Cloud for {}".format(selected_user))
        wordcloud_image = helper.create_wordcloud(selected_user, processed_data)
        st.image(wordcloud_image)

else:
    st.warning("Unable to fetch statistics for the selected user. Please upload the required file.")
#note correct but not showind WordCloud , this code is with error , first one is correct without wordCloud


#---------------------------------------------------This is correct code save for future need -----------------------------------------------------------------------------------------
import streamlit as st
import helper
import preprocessor
import matplotlib.pyplot as plt
st.sidebar.title("WhatsApp Chat Analyzer")

# Create a file uploader in the sidebar
uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.read()

    # Decode bytes to text (assuming the file is a text file)
    data = bytes_data.decode('utf-8')

    # Preprocess the data using preprocessor.preprocess() method
    processed_data = preprocessor.preprocess(data)

    # Display the processed data
    st.dataframe(processed_data)

    # Fetch unique users
    user_list = processed_data['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    # Use st.columns instead of st.beta_columns
    selected_user = st.sidebar.selectbox("Show Analysis Wrt", user_list)
    if st.sidebar.button("Show Analysis"):
        # Fetch stats using helper.fetch_stats() method
        num_messages, words, num_media_messages, num_links_shared = helper.fetch_stats(selected_user, processed_data)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words)

        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)

        with col4:
            st.header("Links Shared")
            st.title(num_links_shared)


        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x ,new_df= helper.most_busy_users(processed_data)
            fig , ax = plt.subplots()


            col1 , col2  = st.columns(2)
            with col1:
                ax.bar(x.index, x.values,color='red')
                plt.xticks(rotation = 'vertical' )
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        #WordCloud
        df_wc = helper.create_wordcloud(selected_user,processed_data)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)













else:
    st.warning("Unable to fetch statistics for the selected user upload the required file .")





#til now the complete code 12:33 Pm


import streamlit as st
import helper
import preprocessor
import matplotlib.pyplot as plt
st.sidebar.title("WhatsApp Chat Analyzer")

# Create a file uploader in the sidebar
uploaded_file = st.sidebar.file_uploader("Choose a file")

if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.read()

    # Decode bytes to text (assuming the file is a text file)
    data = bytes_data.decode('utf-8')

    # Preprocess the data using preprocessor.preprocess() method
    processed_data = preprocessor.preprocess(data)

    # Display the processed data
    st.dataframe(processed_data)

    # Fetch unique users
    user_list = processed_data['user'].unique().tolist()
    user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0, "Overall")

    # Use st.columns instead of st.beta_columns
    selected_user = st.sidebar.selectbox("Show Analysis Wrt", user_list)
    if st.sidebar.button("Show Analysis"):
        # Fetch stats using helper.fetch_stats() method
        num_messages, words, num_media_messages, num_links_shared = helper.fetch_stats(selected_user, processed_data)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        with col2:
            st.header("Total Words")
            st.title(words)

        with col3:
            st.header("Media Shared")
            st.title(num_media_messages)

        with col4:
            st.header("Links Shared")
            st.title(num_links_shared)


        if selected_user == 'Overall':
            st.title('Most Busy Users')
            x ,new_df= helper.most_busy_users(processed_data)
            fig , ax = plt.subplots()


            col1 , col2  = st.columns(2)
            with col1:
                ax.bar(x.index, x.values,color='red')
                plt.xticks(rotation = 'vertical' )
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        #WordCloud
        df_wc = helper.create_wordcloud(selected_user,processed_data)
        fig,ax = plt.subplots()
        ax.imshow(df_wc)

        st.pyplot(fig)
        #Most Common Words
        most_common_df = helper.most_common_words(selected_user,processed_data)
        st.title("Most Common Words in dataframe form")
        st.dataframe(most_common_df)
        fig , ax = plt.subplots()
        ax.barh(most_common_df[0] , most_common_df[1])
        plt.xticks(rotation= 'vertical')

        st.title("Most Common Words")
        st.pyplot(fig)















else:
    st.warning("Unable to fetch statistics for the selected user upload the required file .")



































