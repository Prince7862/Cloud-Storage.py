
import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def _init_(self,access_token):
        self.access_token =  access_token

    def upload_file(self, source, destination):
        dbx = dropbox.Dropbox(self.access_token)


        for root, dirs, files in os.walk(source):
            for filename in files:

                local_path = os.path.join(root, filename)


                relative_path = os.path.relpath(local_path, source)
                dropbox_path = os.path.join(destination, relative_path)

                with open(local_path, 'rb') as f:
                    print(local_path)
                    dbx.files_upload(f.read(),dropbox_path, mode = WriteMode('overwrite'))

def main():
    access_token = "sl.A8EvO1-LbPEfberg-5vWz6q2R7JfiSnmJyuvCFT5ANXvar98WSpSLLw44Xw9vtSVBbIC1ZQesXPJvzgdk6J8EblRRwlCMh1Frjx-vDDZ0B9wjCOsq5eLq_qGFbgnJRezS1vhEdA"
    transferData : TransferData(access_token)

    source = str(input("Enter the folder path to transfer: "))
    destination = input("Enter the full path to upload to DropBox: ")

    transferData.upload_file(source, destination)
    print("The folder has been moved successfully")


main()