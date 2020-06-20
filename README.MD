# Google Drive File Uploader (GDFU)
GDFU is Python based script that will upload files on your Google Drive using Google Drive API v3

# Usage
1. Enable API for your Google Drive [here](https://developers.google.com/drive/api/v3/quickstart/python).  
2. Downloaded 'credentials.json' move to google_auth directory.  
3. Install Google Client Library  
`pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`  
4. Run main.py from from terminal/command prompt  
#### Linux
`python3 main.py`  
#### Windows
`py main.py`  

GDFU will offer you three options:
- Create folder
- Upload file
- Upload all files  
  
**Note:** Do not change the name of 'uploads' directory, put your files only there!  

# Google Credentials  
Google Drive API will create 2 files:
- credentials.json
- token.pickle  

These files will recognize you and allow you to access your Google Drive through GDFU.  
**Note:** Both files **must** be in google_auth directory!

# License
[MIT](https://github.com/petricbranko/Google-Drive-API-File-Uploader/blob/master/LICENSE)
