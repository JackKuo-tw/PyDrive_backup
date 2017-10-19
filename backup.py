from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import sys
 
if len(sys.argv) < 2:
    exit()
path = sys.argv[1]
name = sys.argv[2]

gauth = GoogleAuth()
gauth.CommandLineAuth()
drive = GoogleDrive(gauth)
 
try:
    file1 = drive.CreateFile({"title":name,"parents": [{"kind": "drive#fileLink", "id": "1B4GktyQzQmZDRYTHYDUpW"}]})
    file1.SetContentFile(path)
    file1.Upload()
    print "Uploading succeeded!"
except:
    print "Uploading failed."
