# import streamlit as st
# import datetime as dt
# import pandas as pd
# import time
# import webbrowser
# import scrapy


# # date and time
# st.sidebar.date_input('date',dt.datetime.now())

# st.title("AlleScraper")

# keyword = st.text_input('What would you like to scrape?','input...')
# st.sidebar.markdown('--debugger--')
# st.sidebar.text(f'keyword = {keyword}')
# url = f'https://allegro.pl/listing?string={keyword}'

# if st.button('open allegro listings'):
#     webbrowser.open_new_tab(url)

# # JSON
# st.text('display JSON')
# st.json({'test':"aaaa",'wooooo':"eeeeeee"})


# if st.button('run scrapy'):
#     pass
