import dropbox

class transfer:
    def __init__ (self, access_token):
        self.access_token = access_token

    def upload(self,file_from,file_to): 
        ddx = dropbox.Dropbox(self.access_token)   

        f = open(file_from,'rb')
        ddx.files_upload(f.read(),file_to)

def main():
    access_token = 'YOUR_API_KEY'
    transfer1 = transfer(access_token)
    file_from = input("Enter The File Path To Transfer: ")
    file_to = input(" Enter The Full Path To Transfer To Dropbox: ")
    transfer1.upload(file_from,file_to) 
    print("Files Has Been Moved!!!")

# kalrav = transfer('sl.AmgLEiResJOCh_UsRXLdBBM6itn15pINwMinNeCDQh86VibPVk_rm_F9FVYXsQiUA5CzuQnGoU_EeoufVCzORHI4kMWsPxIWi8MvJtKq97zvn3Ya5IfGa49EsLvBJcKY4bcWqB8') 
# kalrav.main()
main()
               

