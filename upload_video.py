#https://learndataanalysis.org/google-py-file-source-code/
#https://console.cloud.google.com/apis/api/youtube.googleapis.com/quotas?project=youtube-automation-382503

import datetime
from google_apis import create_service
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload, MediaIoBaseUpload
from googleapiclient.errors import HttpError
import io
import os
import time

API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']
client_file = 'client-secret.json'

service = create_service(client_file, API_NAME, API_VERSION, SCOPES)

def upload_video(title, description, video_file, tags): #, thumbnail
    upload_time = (datetime.datetime.now() + datetime.timedelta(days=10)).isoformat() + '.000Z'
    request_body = {
        'snippet': {
            'title': title,
            'description': description,
            'categoryId': '10',
            'tags': tags,
        },
        'status': {
            'privacyStatus': 'public',
            'selfDeclaredMadeForKids': False
        },
        'notifySubscribers': False
    }

    media_file = MediaFileUpload(video_file, chunksize=-1, resumable=True)

    response_video_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media_file
    )

    response = None
    while response is None:
        status, response = response_video_upload.next_chunk()
        if status:
            print("Uploaded %d%%." % int(status.progress() * 100))
    print("Upload Complete!")

    uploaded_video_id = response.get('id')

    # response_thumbnail_upload = service.thumbnails().set(
    #     videoId=uploaded_video_id,
    #     media_body=MediaFileUpload(thumbnail)
    # ).execute()