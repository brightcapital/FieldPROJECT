import dropbox
import os

access_token = ""

local_file_path= ""

# dropbox location where to be uploaded
dropbox_path = ""

dbx = dropbox.Dropbox(access_token)

# Check if the file exists
if os.path.exists(local_file_path):
    # Open the file and upload it
    with open(local_file_path, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
    print("File uploaded successfully.")
else:
    print("Local file not found.")

