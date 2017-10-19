from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
 
gauth = GoogleAuth()
gauth.CommandLineAuth() #透過授權碼認證
drive = GoogleDrive(gauth)
 
 
try:
# id 表示雲端硬碟資料夾的 id
# 可以在網頁畫面網址列看到
    file1 = drive.CreateFile({"title":'Hello.txt',"parents": [{"kind": "drive#fileLink", "id": "1B4GktyQzQmZDRYTHYDUpW"}]})
    file1.SetContentFile('../mail.py')
    file1.Upload() #檔案上傳
    print "Uploading succeeded!"
except:
    print "Uploading failed."
