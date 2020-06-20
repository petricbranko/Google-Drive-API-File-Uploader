import pickle
import os.path
from apiclient.http import MediaFileUpload
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class fileUploader():
    def __init__(self):
        # Permissions
        SCOPES = ['https://www.googleapis.com/auth/drive']
        creds = None
        # Call API
        if os.path.exists('google_auth/token.pickle'):
            with open('google_auth/token.pickle', 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'google_auth/credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('drive', 'v3', credentials=creds)

    def createFolder(self, folder_name):
        self.folder_name = folder_name

        folder_info = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }

        folder = self.service.files().create(body=folder_info, fields='id').execute()
        print('Folder \033[92m ' + folder_name + '\033[0m created!')
        print('Folder ID:', folder.get('id'))

    def uploadFile(self, file_name, folder_id):
        self.file_name = file_name
        self.folder_id = folder_id

        file_info = {
            'name' : file_name,
            'parents' : [folder_id]
        }

        media = MediaFileUpload(('uploads/'+file_name),
                        resumable=False)

        file = self.service.files().create(body=file_info,
                                    media_body=media,
                                    fields='id').execute()

        print('File \033[92m ' + file_name + '\033[0m uploaded!')

    def uploadAll(self, folder_id):
        path = "./uploads"
        self.folder_id = folder_id
        print("\nUploading: ")

        for file in os.listdir(path):
            print(file)
            fileUploader.uploadFile(file, folder_id)

fileUploader = fileUploader()

valid_input = False

menu = """
1. Create folder
2. Upload file
3. Upload all files from 'uploads' folder"""

while not valid_input:
    print(menu)
    user_choice = input("Your choice: ")

    if user_choice == "1":
        fileUploader.createFolder(input("Enter folder name: "))
        valid_input = True
    elif user_choice == "2":
        # Print all files from folder 'uploads'
        print("\nFiles you can upload:")
        path = "./uploads"
        for file in os.listdir(path):
            print(file)

        fileUploader.uploadFile(input("\nEnter file name: "), input("Enter folder ID: "))
        valid_input = True
    elif user_choice == "3":
        fileUploader.uploadAll(input("Enter folder ID: "))
        valid_input = True
    else:
        print("Invalid input, try again!")
        valid_input = False
        