[POST method]
Headers:

From Data:
檢視網頁原始碼: viewstate "hidden"


[facebook]
https://developers.facebook.com/

graphic api:
https://developers.facebook.com/tools/explorer/145634995501895/

存取權杖
EAACEdEose0cBANP4m0ZAlZBrOGTRshqgxJ42X79cKkL9h3oM5R5ums6FXua9y4YJn04ZA94rz0OKsVTadRA8So6HcZBLcAJnlMacMGWVUSct3KdcfpraJic4yl99PSL8KOGcfq76xQZA24YTEauNplOenMmMZCUDkOZBVMwJWXaJv60a2NZCFcdMCTW69E8878sZD


[MySql setup for MAC OS]
Set config file
$ sudo vim /etc/my.cnf
[mysqld]
port=3306
bind-address = 0.0.0.0
collation-server = utf8_unicode_ci
init-connect='SET NAMES utf8'
character-set-server = utf8


restart mysql service
kill the old db & create a new db

[face API documentation]
https://developers.facebook.com/docs/graph-api/using-graph-api/#fieldexpansion

[Mac OS scheduler]
$ crontab -e
