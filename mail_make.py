# import os
import df_check as dc

nowusedisk = dc.now_usedisk()
disk_total = nowusedisk[0]
disk_used = nowusedisk[1]
disk_free = nowusedisk[2]

disk_total = float(disk_total)
disk_used = float(disk_used)
disk_free = float(disk_free)

df = dc.check_df()
df = int(df)

# print(disk_total, disk_used, disk_free, df)

paddingmargin = 'padding:0;margin:0;'

# print(os.path.isfile("html_test.html"))


def make_main():
    file = open('/root/script/disk_alert/html_test.html',
                'w', encoding='UTF-8')

    body = """ <style type="text/css">p {paddingmargin}
    </style>
    <div class="sensEdContentAreaCls" data-id="sensEdContentArea" style="color:#000;line-height:150%;font-size:10pt;font-family:굴림 !important;padding:0;margin:0;">
    <style type="text/css">p {paddingmargin}
    </style>
    <div class="sensEdContentAreaCls" data-id="sensEdContentArea" style="color:#000;line-height:150%;font-size:10pt;font-family:굴림 !important;padding:0;margin:0;">
    <div class="sensEdContentAreaCls" data-id="sensEdContentArea" style="color:#000;line-height:150%;font-size:10pt;font-family:굴림 !important;padding:0;margin:0;">
    <div class="sensEdContentAreaCls" data-id="sensEdContentArea" style="color:#000;line-height:150%;font-size:10pt;font-family:굴림 !important;padding:0;margin:0;">&nbsp;</div>
    <x-meta charset="utf-8"></x-meta> <x-meta content="IE=Edge" http-equiv="X-UA-Compatible"></x-meta>

    <div style="margin:0 auto; width:700px; font-family: '맑은고딕',Malgun Gothic,'돋움',Dotum,Helvetica,'Apple SD Gothic Neo',Sans-serif; border:1px solid #e0e0e0;border-width: 0 1px 1px 1px;white-space: normal; word-spacing: 0px; color: rgb(0,0,0); letter-spacing: normal; text-indent: 0px; -webkit-text-size-adjust: auto; -webkit-text-stroke-width: 0px;">
    <table cellpadding="0" cellspacing="0" style="width:100%;margin:0;word-break:break-all;">
        <tbody>
            <tr>
                <td style="margin:0;padding:0">
                <table cellpadding="0" cellspacing="0" style="width:100%;margin:0;padding: 0; background-color:#fafafa;border-bottom:1px solid #ddd;border-top: 3px solid #333;">
                    <tbody>
                        <tr>
                            <td style="padding: 15px 30px;"><a href="" rel="" style="" target="_blank"> <img alt="sensmail" height="auto" src="http://119.206.195.166/images/imoxion.com_logo_top.png" style="" width="110" /> </a></td>
                        </tr>
                    </tbody>
                </table>
                </td>
            </tr>
            <tr>
                <td style="padding: 30px 30px;">
                <table cellpadding="0" cellspacing="0" style="width:100%;margin:0;padding:0;">
                    <tbody>
                        <tr>
                            <td colspan="2" style="font-size: 30px; font-weight: bold; vertical-align: middle; text-align: left; line-height: 38px; letter-spacing: -1px; font-family: 맑은고딕, &quot;Malgun Gothic&quot;, 돋움, Dotum, Helvetica, &quot;Apple SD Gothic Neo&quot;, sans-serif;" width="70%">센스호스팅<br />
                            <font color="#1097bf">단독형 메일서버 용량&nbsp;</font><span style="color: rgb(0, 0, 0);">안내</span></td>
                            <td height="24" style="font-size:0px;padding-right: 20px;vertical-align:middle;text-align: right;"><img alt="Mail" data-="" height="auto" src="http://119.206.195.166/images/top_visual_191202.jpg" title="Mail" width="100" /></td>
                        </tr>
                    </tbody>
                </table>
                </td>
            </tr>
            <tr>
                <td style="padding:0px 30px 30px 30px;">
                <table cellpadding="0" cellspacing="0" style="width:100%;margin:0;padding:0;">
                    <tbody>
                        <tr>
                            <td style="font-size: 14px;color: #333;vertical-align:middle;text-align: left;font-family:'맑은고딕',Malgun Gothic,'돋움',Dotum,Helvetica,'Apple SD Gothic Neo',Sans-serif;line-height: 1.5;">
                            <p style="margin:4px 0;">안녕하세요. 아이모션 운영실입니다.</p>
                            <p style="margin:4px 0;">메일서버 용량이 부족하여 안내드립니다.</p>
                            <p style="margin:4px 0;">용량이 100% 차게 되면 메일수발신이 불가합니다.</p>
                            </td>
                        </tr>
                        <tr>
                            <td height="10">&nbsp;</td>
                        </tr>
                        <tr>
                            <td style="color: #333;vertical-align:middle;text-align: left;font-family:'맑은고딕',Malgun Gothic,'돋움',Dotum,Helvetica,'Apple SD Gothic Neo',Sans-serif;">
                            <table cellpadding="0" cellspacing="0" style="width:100%; border-collapse:collapse;font-size:12px;">
                                <colgroup>
                                    <col width="150px" />
                                    <col width="auto" />
                                </colgroup>
                                <thead style="background-color:#f8f8f8; color:#000000;text-align:center;">
                                    <tr>
                                        <th style="padding:7px 0;border-top:1px solid #333;border-bottom:1px solid #e6e6e6;">경로</th>
                                        <th style="padding:7px 0;border-top:1px solid #333;border-bottom:1px solid #e6e6e6;border-left:1px solid #e6e6e6;">총 용량</th>
                                        <th style="padding:7px 0;border-top:1px solid #333;border-bottom:1px solid #e6e6e6;border-left:1px solid #e6e6e6;">사용량</th>
                                        <th style="padding:7px 0;border-top:1px solid #333;border-bottom:1px solid #e6e6e6;border-left:1px solid #e6e6e6;">남은 용량</th>
                                    </tr>
                                </thead>
                                <tbody style="color:#333;text-align:center;">
                                    <tr>
                                        <th style="padding:7px 0;border-bottom:1px solid #e6e6e6;">/maildata</th>
                                        <td style="padding:7px 20px;border-bottom:1px solid #e6e6e6;border-left:1px solid #e6e6e6;line-height:18px;">{disk_total} GB</td>
                                        <td style="padding:7px 20px;border-bottom:1px solid #e6e6e6;border-left:1px solid #e6e6e6;line-height:18px;">{disk_used} GB ({df}%)</td>
                                        <td style="padding:7px 20px;border-bottom:1px solid #e6e6e6;border-left:1px solid #e6e6e6;line-height:18px;">{disk_free} GB</td>
                                    </tr>
                                </tbody>
                            </table>
                            </td>
                        </tr>
                        <tr>
                            <td height="10">&nbsp;</td>
                        </tr>
                        <tr>
                            <td style="font-size: 14px;color: #333;vertical-align:middle;text-align: left;font-family:'맑은고딕',Malgun Gothic,'돋움',Dotum,Helvetica,'Apple SD Gothic Neo',Sans-serif;line-height: 1.5;">
                            <p style="margin:4px 0;">오랜된 메일이나 불필요한 메일을 정리하여 메일용량 확보 바랍니다.</p>
                            <p style="margin:4px 0;">더 이상 정리하실 메일이 없다면 용량 증설이 필요합니다.</p>
                            <p style="margin:4px 0;">문의사항이 있으시다면 아이모션 운영실로 연락 주시기 바랍니다.</p>
                            <p style="margin:4px 0;">&nbsp;</p>
                            <p style="margin:4px 0;">감사합니다.</p>
                            <p style="margin:4px 0;">&nbsp;</p>
                            <p style="margin:4px 0;font-weight:bold;color: #dc831c;">아이모션 운영실</p>
                            <p style="margin:4px 0;font-weight:bold;color: #dc831c;">전화 : 1644-9617 내선1번</p>
                            <p style="margin:4px 0;font-weight:bold;color: #dc831c;">메일주소 : help@senshosting.co.kr</p>
                            </td>
                        </tr>
                    </tbody>
                </table>
                </td>
            </tr>
        </tbody>
    </table>
    </div>
    </div>
    </div>
    </div>
    """

    body = body.format(paddingmargin=paddingmargin, df=df, disk_total=disk_total,
                       disk_used=disk_used, disk_free=disk_free)

    file.write(body)

    file.close()
