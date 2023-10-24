import dropbox
import os

access_token = "sl.BojeVOFp7zGOK7m5fILZJfjCp87ZRlAc7lkdpDVf7o83p6xrbKa2qaAtdKdzxai8yy2yVBMN1jEzl5CGjMr8_bwfcpxDZKy7wzT2bQYlM1ZF-n-AgDtb5oAIpzVN9aTjdki1ZC-UKCEPhKc"

local_file_path = r"C:\Users\BrightsideCapital\PycharmProjects\FieldPROJECT\xbbg\bloomberg_price.csv"

# dropbox location where to be uploaded
dropbox_path = "/C:/BrightsideCapital/New folder/Brightside Capital Dropbox/Brightside Capital (office)/22. INVESTMENT TEAM/Database/bloomberg_price.csv"

dbx = dropbox.Dropbox(access_token)

# Check if the file exists
if os.path.exists(local_file_path):
    # Open the file and upload it
    with open(local_file_path, 'rb') as f:
        dbx.files_upload(f.read(), dropbox_path, mode=dropbox.files.WriteMode.overwrite)
    print("File uploaded successfully.")

else:
    print("Local file not found.")

