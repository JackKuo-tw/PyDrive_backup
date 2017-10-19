# PyDrive_backup

作者擔心樹莓派的 SD 卡某一天突然壞掉，所以想要做簡單的備份程式，由於學生的 Google Drive 空間是無限量的，PyDrive 自然是不錯的選擇。壓縮程式預設使用 7z 是因為方便又可以對 metadata 進行加密，也就是沒有密碼是不能看到壓縮檔裡有哪些檔案與目錄。

## 安裝必要套件

- `$sudo pip install pydrive`
- `$brew install p7zip`

## 設定驗證資料

### Google Drive API

PyDrive 這個套件是使用 Google API，因此我們得去申請一下

- 至 APIs console 建立專案
- 啟用 Drive API
- 選取 "憑證" , "OAuth同意畫面"
- 只需在 "向使用者顯示的產品名稱" 輸入即可儲存
- 建立憑證 選取 "OAuth 用戶端ID"
- 類型務必選擇 "其他" 這樣可以用的範圍比較廣
- 接著右邊有個下載符號，即可開啟查看認證資訊

### 填寫設定檔
- 編輯 `settings.yaml`
- 填寫 client_id 與 client_secret 即可

## 自動備份

### 檔案介紹

- file_list 裡面可以寫哪些檔案或目錄要進行備份上傳
- backup.sh 用來建立壓縮檔並且放到 /tmp 資料夾
- backup.py 會抓取 /tmp 中的壓縮檔並上傳

### 使用說明

- file_list 格式範例：

```
/home/
/var/www/html/*.html
/var/log/system.log

```

- backup.sh 使用 7z 進行備份，可以修改為個人偏好的壓縮軟體
- 請將 backup.py 裡面的 id 欄位替換成自己的資料夾
- 執行方式： `$sh backup.sh`
