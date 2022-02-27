import subprocess
import smtplib
from email.mime.text import MIMEText
import pymysql.cursors
import time
import schedule
import mail_make


def hostnameinfo():
    hostname = subprocess.check_output("hostname")

    hostname = hostname.decode('utf-8')

    return hostname


def admin_extraction():
    """ 수신받을 도메인관리자계정 추출 """
    admin_address = []

    # DB연결
    db = pymysql.connect(unix_socket="/tmp/mysql.sock",
                         user='root', db='sensmail', charset='utf8')
    curs = db.cursor()

    # Select Query - 도메인관리자 추출
    adminuser_sql = "select mailid, mhost from ims_userinfo where perms='A'"
    curs.execute(adminuser_sql)
    adminusers = list(curs.fetchall())

    # Select Query - 도메인 추출
    domain_sql = "select mhost, domain from ims_tbldomain order by mhost"
    curs.execute(domain_sql)
    domains = list(curs.fetchall())

    db.commit()

    # print(domains)

    # 주도메인(첫번째 등록한 도메인) 추출
    maindomain = domains[0]
    maindomainname = maindomain[1]

    # 도메인관리자 메일주소 생성
    for adminuser in adminusers:
        userid = adminuser[0]
        userdomainid = adminuser[1]
        for domain in domains:
            domainid = domain[0]
            domainname = domain[1]
            if userdomainid == domainid:
                admin_address.append(f"{userid}@{domainname}")

    # 주도메인, 도메인관리자 주소 리턴
    return maindomainname, admin_address


def check_df():
    """ 현재 디스크 사용량 """
    # 체크할 디스크
    disk_directory = "/maildata"

    # 현재 용량 확인
    df = subprocess.check_output(
        f"df -h {disk_directory} | awk 'NR == 2 {{print $5}}'", shell=True)

    df = df[0: len(df) - 2]

    return df


def now_usedisk():
    """ 현재 디스크 사용량 """

    # 체크할 디스크
    disk_directory = '/maildata'

    total = subprocess.check_output(
        f"df -h {disk_directory} | awk 'NR == 2 {{print $2}}'", shell=True)
    used = subprocess.check_output(
        f"df -h {disk_directory} | awk 'NR == 2 {{print $3}}'", shell=True)
    free = subprocess.check_output(
        f"df -h {disk_directory} | awk 'NR == 2 {{print $4}}'", shell=True)

    total = total[0: len(total) - 2]
    used = used[0: len(used) - 2]
    free = free[0: len(free) - 2]

    return total, used, free


def comparison_df():
    """ 설정된 용량을 넘었는지 체크 """
    df = check_df()
    # space% 이상이면 메일발송
    space = 90

    # 설정용량이 넘었는지 체크 넘었으면 메일발송
    if (int(df) > int(space)):
        mail_make.make_main()

        admin_admin_extraction = admin_extraction()
        admin_address = admin_admin_extraction[1]
        maindomainname = admin_admin_extraction[0]

        # 현재 용량, 주도메인, 도메인관리자주소로 send_mail함수 호출
        send_mail(int(df), maindomainname, admin_address)


def send_mail(space, maindomainname, admin_address=[]):
    """ 메일 발송 """

    # print(disk_total, disk_used, disk_free)
    # 추가 수신받을 메일주소 , 로 구분
    # EX> add_address = ['sywon753@imoxion.com', 'sywon753@ktspeedway.co.kr']
    add_address = ['help@senshosting.co.kr']
    for add in add_address:
        admin_address.append(add)

    # 발송서버 설정

    # 발송할 메일주소
    send_address = f'admin@{maindomainname}'

    # print(admin_address)

    file = open('/root/script/disk_alert/html_test.html',
                'r', encoding='UTF-8')
    mail_body = file.read()

    # print(mail_body)
    hostname = hostnameinfo()

    for recipient in admin_address:
        try:
            # print(f'{recipient}send start')
            smtp = smtplib.SMTP('localhost', 25)

            smtp.ehlo()      # say Hello
            # smtp.starttls()  # TLS 사용시 필요
            # smtp.login('SMTP아이디', '패스워드')

            # msg = MIMEText(f'본문 테스트 메시지!! {space}초과')
            msg = MIMEText(mail_body, 'html')
            msg['Subject'] = f'[아이모션] {hostname} 메일서버 용량 안내드립니다.'
            msg['From'] = send_address
            msg['To'] = recipient
            smtp.sendmail(send_address,
                          recipient, msg.as_string())
        except smtplib.SMTPException:
            pass

        smtp.quit()
        # print(f'{recipient}send ok')


def main():
    # 실행되는 시간
    schedule_time = "10:30"

    # 실행
    comparison_df()  # 시작할때 1회 실행(시작할때 실행되지 않게 하려면 주석 처리)
    schedule.every().day.at(schedule_time).do(comparison_df)  # 이후 설정된 시간에 실행

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
