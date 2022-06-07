import dropbox

class TransferData :

    def __init__(self,access_token):
        self.access_token=access_token
    
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from,'rb') as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token='sl.BHufPWbXlgyPzx2W-AxvwWS6dCpJc4X8t2oQ1SkaUsFQhQ9mjGh5FyIOl1QIHY6s5U57RP0xIEch9E84yTDYzKSAjrHEvWpqDeUfylsQJd56gdoFhmFE0AtQ-p7HHp_GO2uI4NY'
    transfer_class=TransferData(access_token)
    file_from = input('Path of the file to be uploaded: ')
    file_to = input('Path of the file to be uploaded: ')
    transfer_class.upload_file(file_from,file_to)
    
main()


 
    