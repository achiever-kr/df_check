yum groupinstall "Development Tools" -y

sleep 5

yum install python3-pip -y

sleep 5

pip3 install pymysql

sleep 5

pip3 install schedule

sleep 5

wget -P /root/script/disk_alert http://119.206.195.165/patch/singlesensmail/script/disk_alert/df_check.py

sleep 5

wget -P /root/script/disk_alert http://119.206.195.165/patch/singlesensmail/script/disk_alert/mail_make.py

sleep 5

nohup python3 /root/script/disk_alert/df_check.py  1>/dev/null 2>&1 &