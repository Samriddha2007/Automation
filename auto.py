import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'kf4s9N34kTcAAAAAAAAAAXotLMcReqVcKHbf2BXivpqT-vtJnoHgooqYt9CSMTrt'
    transferData = TransferData(access_token)

    print('Please choose the created "studies.txt" file for uploading, and follow the steps prescribed after!')
    file_from = input('Enter the file path: ')
    file_to = input('Enter the full path to upload to dropbox: ')

    # API v2
    transferData.upload_file(file_from, file_to)
    print('The file has been uploaded')


class WM:
    def __init__(self, sub): 
        self.sub = sub
        
        
        sbt = 'Have you studied ' + sub + ' Today: '
        sb = input(sbt)

        if (sb == 'Y'):
            x = 'I have studied ' + sub
        else:
            x = 'I have not studied ' + sub

        fc = open('studies.txt', 'a+')
        fc.write("\n")
        fc.write(x)
        fc.close()

con = input('Do you want to make a list of subjects you have studied today: Y/N ')

if con == 'Y':
    print('Please answer in Y or N')

    WM('Maths')
    WM('Physics')
    WM('Chemistry')
    WM('Biology')
    WM('Geography')
    WM('History')
    WM('English Literature')
    WM('English Grammar')
    WM('Bengali Literature')
    WM('Bengali Grammar')

    w = input('Do you wish to back-up the file to cloud-storage? Y/N: ')
    if(w == 'Y'):
        main()
    else:
        print('Thank you! Your journey ends here')

else:
    print('Your journey ends here!')