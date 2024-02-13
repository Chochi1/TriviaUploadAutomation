#https://console.cloud.google.com/apis/credentials?highlightClient=43783410636-1njq5oiuddlhejvbdn2e3jfcu768lk1k.apps.googleusercontent.com&project=youtube-automation-382503&supportedpurview=project

import os
import random
import shutil
import logging
import mysql.connector
from datetime import datetime
from dotenv import load_dotenv

from upload_video import upload_video
from create_description import create_youtube_description, create_youtube_tags

import mysql.connector
from datetime import datetime

# Connect to the database
mydb = mysql.connector.connect(
  host=os.getenv('DB_HOST'),
  user=os.getenv('DB_USER'),
  passwd=os.getenv('DB_PASS'),
  database=os.getenv('DB_NAME')
)

mycursor = mydb.cursor()

# Step 1: Select a random row where 'uploaded' is NULL
try:
    mycursor.execute("SELECT short_id, title, hook, body, video_path FROM shorts WHERE uploaded IS NULL ORDER BY RAND() LIMIT 1")
    row = mycursor.fetchone()
    if row:
        id, title, hook, body, video_path = row
        print("Selected Row:", video_path)

        seo_desc = create_youtube_description(hook, body)
        tags = create_youtube_tags(hook, body)
        print("SEO Description:", seo_desc)
        print("Tags:", tags)

        # Convert the input string to a list of words/tags
        tags = tags.split(', ')

        # Words to filter out
        filter_words = ['shorts', 'youtubeshorts', 'shortschannel']

        # Filter and format the remaining words as hashtags
        hashtags = ['#' + word.replace(" ", "") for word in tags if word not in filter_words]

        # Join the hashtags into a single string
        output = ' '.join(hashtags)

        
        print("\n TikTok")
        print("\n" + seo_desc + "\n \n"+ output + " #fyp")

        print("\n Instagram")
        print("\n" + seo_desc + "\n \n"+ output)        

        # Upload the video
        upload_video(title  + ' #trivia', hook, video_path, tags)

        logging.info("Video uploaded.")

        # Step 2: Update the 'uploaded' column for the selected row with the current date
        current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        update_query = "UPDATE shorts SET uploaded = %s WHERE short_id = %s"
        mycursor.execute(update_query, (current_date, id))
        mydb.commit()
        print(f"Row with id {id} has been marked as uploaded on {current_date}.")
    else:
        print("No rows found where 'uploaded' is NULL.")
except mysql.connector.Error as err:
    print(f"Error: {err}")
    mydb.rollback()

# Close the cursor and connection
mycursor.close()
mydb.close()


# Set up logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s',
                    handlers=[logging.FileHandler("log.txt"),
                              logging.StreamHandler()])
error_log = logging.FileHandler("error.txt")
