import AuReIn as Fa
from sys import exit
from math import ceil
from pyperclip import copy
from rich.text import Text
from rich.panel import Panel
from base64 import b64decode
from datetime import datetime
from pickle import load, dump
from webbrowser import open_new
from rich.console import Console
from random import randint, choice
from pygame.mixer import init, music
from os import path, makedirs, system
from time import sleep, strftime, localtime


class Day:
    cdict = {}
    gdict = {}

    def __init__(self):
        self.cdict = {1: u'', 2: u'拾', 3: u'佰', 4: u'仟'}
        self.gdict = {0: u'零', 1: u'壹', 2: u'贰', 3: u'叁', 4: u'肆', 5: u'伍', 6: u'陆', 7: u'柒', 8: u'捌',
                      9: u'玖'}
        self.aab = {1: u'', 2: u'十', 3: u'百', 4: u'千'}
        self.aabc = {0: u'零', 1: u'一', 2: u'二', 3: u'三', 4: u'四', 5: u'五', 6: u'六', 7: u'七', 8: u'八',
                     9: u'九'}

    def cschange(self, cki):
        lenki = len(cki)
        lk = lenki
        chk = u''
        i = 0
        for i in range(lenki):
            if int(cki[i]) == 0:
                if i < lenki - 1:
                    if int(cki[i + 1]) != 0:
                        chk = chk + self.gdict[int(cki[i])]
            else:
                chk = chk + self.gdict[int(cki[i])] + self.cdict[lk]
            lk -= 1
        return chk

    def schange(self, cki):
        lenki = len(cki)
        lk = lenki
        chk = u''
        i = 0
        for i in range(lenki):
            if int(cki[i]) == 0:
                if i < lenki - 1:
                    if int(cki[i + 1]) != 0:
                        chk = chk + self.aabc[int(cki[i])]
            else:
                chk = chk + self.aabc[int(cki[i])] + self.aab[lk]
            lk -= 1
        return chk


ptim = Day()
cs = Console()


class ZhouZhi:
    def __init__(self):
        self.totalTxt = ''
        cs.print(Panel(Text("【Ok周志】", justify="center", style='bold blink yellow on cyan')))
        print()
        if not path.exists(r'C:\Ok周志\SysOk'):
            makedirs(r'C:\Ok周志\SysOk')
        if not path.exists(r'C:\Okroie'):
            makedirs(r'C:\Okroie')
        if not path.exists(r'C:\Ok周志\SysOk\OldUser.pkl'):
            cs.print(Panel.fit('[bold]'
                               ':handshake:服务协议和隐私政策:\n1. 程序名称:【Ok周志】\n2. 程序版本: 9.0\n3. 模仿不难，创造不易\n4. 版权所有，侵权必究\n'
                               '5. 生命短暂，勿留遗憾\n6. 心怀感恩，砥砺前行\n7. 若未购买本产品，可免费使用三次\n8. 程序发行时间: 2022.11.12 15:50'
                               '\n9. 只要仔细研究问题，答案自然会来找你\n10. 程序完全自主开发，未经授权不得任意修改，发布，售卖'
                               '\n11. 若当您在使用过程中遇到BUG请联系我们，真诚感谢您的反馈\n12. 任何事物都有两面性，写周志也是一个好习惯，希望您只是时间紧迫才使用它\n'
                               '\n即将进入程序主界面...', border_style="green"), '\n')
            sleep(1)
        if not path.exists(r'C:\Okroie\Sys'):
            makedirs(r'C:\Okroie\Sys')
            with open(r'C:\Okroie\Sys\UD20221112.pkl', 'w'):
                pass
            sleep(1)
        if not path.exists(r'C:\Ok周志\SysOk\OldTime.pkl'):
            addy = 2022
            aad2 = 10
            aad1 = 10
        else:
            with open(r'C:\Ok周志\SysOk\OldTime.pkl', 'rb') as ffi:
                addy, aad1, aad2 = load(ffi)
        if not path.exists(r'C:\Ok周志\SysOk\A.mp3'):
            oridde = b64decode(Fa.assa)
            with open(r'C:\Ok周志\SysOk\A.mp3', 'wb') as foutq:
                foutq.write(oridde)
                sleep(1)
        init()
        music.load(r'C:\Ok周志\SysOk\A.mp3')
        music.play()
        if not path.exists(r'C:\Okroie\windows\System.pkl'):
            cs.print('[bold white]:grinning_face_with_smiling_eyes:欢迎来到【Ok周志】(9.0版本)%未购买%')
        else:
            cs.print('[bold yellow]:grinning_face_with_smiling_eyes:欢迎来到【Ok周志】(9.0版本)￥已购买￥')
        cs.print('[bold on blue]程序功能: 自动编写周志，无需安装，即可使用')
        cs.print('[bold on cyan]程序开发: 赵帅，笔名/微信公众号/哔哩哔哩: Okroie')
        cs.print('[bold on yellow]【Ok周志】留言板:[white on black] https://docs.qq.com/form/page/DYUlQaWhVakdXZ0R0')
        cs.print('[bold on red]【Ok周志】最新消息及动态: [bold white on black]https://docs.qq.com/doc/DYUVsdVFZWVZNT2dv')
        cs.rule(":glowing_star:")
        if not path.exists(r'C:\Ok周志\SysOk\OldUser.pkl'):
            cs.print('[bold on purple](温馨提示: 仅初次运行程序结束前，需要进行多次选择)')
        if path.exists(r'C:\Ok周志\SysOk\LongTime.pkl'):
            with open(r'C:\Ok周志\SysOk\LongTime.pkl', 'rb') as fdde:
                babyd = ['宝', '主人', 'Dear', 'Darling', 'Honey', '亲爱的', '甜甜', '乖乖', 'Hey', 'Hello', '嗨', 'Hi',
                         '嘿', '小可爱', '宝贝', '小宝贝', '宝宝']
                babbp = choice(babyd)
                cs.print(f'[bold green on purple]【Ok周志】: {babbp}^_^我们上一次见面的时间是在' + load(fdde))
                with open(r'C:\Ok周志\SysOk\LongTime.pkl', 'wb') as fdde1:
                    dump(strftime('%Y年%m月%d日%H点%M分%S秒', localtime()), fdde1)
        else:
            with open(r'C:\Ok周志\SysOk\LongTime.pkl', 'wb') as fdde1:
                dump(strftime('%Y年%m月%d日%H点%M分%S秒', localtime()), fdde1)
        print('\n')
        if not path.exists(r'C:\Ok周志\SysOk\OldUser.pkl'):
            self.inprr = cs.input(
                f'[bold cyan]一: 程序默认实习开始时间为{addy}.{aad1}.{aad2}是否需要修改？\n1: 不需要，2: 需要\n请选择: ').strip()
            if self.inprr == '1':
                self.inprr = '2'
            elif self.inprr == '2':
                self.inprr = '3'
            else:
                cs.print('[bold on blue]【Ok周志】: 检测到您尚未选择或错选，我已自动执行`不需要`')
                sleep(1)
            # I do not want to change it
        if path.exists(r'C:\Ok周志\SysOk\OldUser.pkl'):
            self.inprr = cs.input(
                f'[bold cyan]一: 主人，当前实习开始时间为{addy}.{aad1}.{aad2}是否需要修改？\n1: 全自动，2: 不需要(可半自动)，3: 需要\n请选择: ').strip()
        if self.inprr != '1':
            try:
                if self.inprr == '3':
                    self.inppp = cs.input(
                        '\n[bold yellow]请输入将要修改的年月日，并以空格分开\n(示例: 若是2051年7月26日，就输入2051 7 26)\n请输入: ').split()
                    timq = str(datetime.now().date()).split('-')
                    year1 = int(timq[0])
                    addy, aad1, aad2 = int(self.inppp[0]), int(self.inppp[1]), int(self.inppp[2])
                    if addy <= year1 and aad1 <= 12 and aad2 <= 31:
                        with open(r'C:\Ok周志\SysOk\OldTime.pkl', 'wb') as fffi1:
                            dump([addy, aad1, aad2], fffi1)
                            cs.print(f'[bold purple]【Ok周志】: 实习开始时间已成功修改为{addy}年{aad1}月{aad2}日')
                            sleep(1)
                    else:
                        cs.print(
                            f'[on blue](【Ok周志]: 您输入的日期{addy}年{aad1}月{aad2}日，格式有误。若仍继续运行程序，则默认实习开始时间不变)')
                        if path.exists(r'C:\Ok周志\SysOk\OldTime.pkl'):
                            with open(r'C:\Ok周志\SysOk\OldTime.pkl', 'rb') as ffi:
                                addy, aad1, aad2 = load(ffi)
                        else:
                            addy = 2022
                            aad1 = 10
                            aad2 = 10
                            sleep(1)
                elif self.inprr != '3' and self.inprr != '2' and path.exists(r'C:\Ok周志\SysOk\OldUser.pkl'):
                    cs.print('[bold on blue]【Ok周志】: 主人，检测到您尚未选择或错选，我已自动进入`全自动`模式')
                    sleep(1)
            except Exception as e:
                cs.print(
                    f'[white]主人，这是错误信息({e})，请根据提示进行正确操作\n[blue](温馨提示: 出现上面的错误信息，说明您输入的日期格式有误。若仍继续运行程序，则默认实习开始时间不变)')
                sleep(1)

            if not path.exists(r'C:\Ok周志\SysOk\OldUser.pkl'):
                inpww = cs.input(
                    '\n[bold blue]【Ok周志】: 是否愿意关注开发人员微信公众号和哔哩哔哩: Okroie\n并将您认为有用有趣的内容分享给更多的人？\n1: 我愿意，2: 不愿意\n请选择: ').strip()
                if inpww == '1':
                    cs.print('[bold purple]【Ok周志】: 感谢您的支持与信任')
                elif inpww == '2':
                    cs.print('[bold yellow]【Ok周志】: 选择`2`，说明你是一个很有个性的娃儿')
                else:
                    cs.print('[bold purple]【Ok周志】: 感谢您的支持与信任')
                    self.inprr = '3'
            if self.inprr == '3' or self.inprr == '2':
                if not path.exists(r'C:\Ok周志\SysOk\OldUser.pkl'):
                    self.inptt = cs.input(
                        '\n[bold green]二: 请选择我的执行模式:\n1: 全自动，2: 半自动\n请选择: ').strip()
                    if self.inptt == '1':
                        cs.print('[bold on purple]【Ok周志】: 见到您我很高兴:grinning_face_with_smiling_eyes:')
                        sleep(1)
                        self.inprr = '1'
                    elif self.inptt == '2':
                        cs.print('[bold on purple]【Ok周志】: 见到您我很高兴:grinning_face_with_smiling_eyes:')
                        sleep(1)
                        self.inprr = '2'
                    else:
                        cs.print('[bold on blue]【Ok周志】: 检测到您尚未选择或错选，我已自动进入`全自动`模式')
                        sleep(1)
                        self.inprr = '1'
                else:
                    self.inptt = cs.input(
                        '\n[bold green]二: 主人，请选择我的执行模式:\n1: 全自动，2: 半自动，3: 游客模式，0: 开发文档\n请选择: ').strip()
                    if self.inptt == '1':
                        self.inprr = '1'
                    elif self.inptt == '2':
                        self.inprr = '2'
                    elif self.inptt == '3':
                        cs.print('[bold on blue]【Ok周志】: 主人，1分钟后我会自动进入`全自动`模式')
                        sleep(2)
                        open_new('https://mp.weixin.qq.com/s/TV411JXeUEXxzitf04d2pw')
                        sleep(10)
                        open_new('https://b23.tv/HiZRvHz')
                        sleep(50)
                        self.inprr = '1'
                    elif self.inptt == '0':
                        cs.print(Panel.fit(
                            '一. 程序功能简介: \n这是一款自动编写周志的程序(无需安装，即可使用)'
                            '\n二. 服务协议和隐私政策:\n1. 程序名称:【Ok周志】\n2. 程序版本: 9.0\n3. 模仿不难，创造不易\n4. 版权所有，侵权必究\n'
                            '5. 生命短暂，勿留遗憾\n6. 心怀感恩，砥砺前行\n7. 程序发行时间: 2022.11.12 15:50\n8. 若未购买本产品，可免费使用三次'
                            '\n9. 只要仔细研究问题，答案自然会来找你\n10. 程序完全自主开发，未经授权不得任意修改，发布，售卖'
                            '\n11. 若当您在使用过程中遇到BUG请联系我们，真诚感谢您的反馈\n12. 任何事物都有两面性，写周志也是一个好习惯，希望您只是时间紧迫才使用它'
                            '\n三. 开发人员:\n赵帅，笔名/微信公众号/哔哩哔哩: Okroie'
                            '\n四.【Ok周志】: \n1. 留言板: https://docs.qq.com/form/page/DYUlQaWhVakdXZ0R0'
                            '\n2. 程序最新消息及动态: https://docs.qq.com/doc/DYUVsdVFZWVZNT2dv'
                            '\n五. 生命不息，奋斗不止...', border_style='yellow'))
                        cs.print('\n[bold on blue]【Ok周志】: 主人，30秒后我会自动进入`半自动`模式')
                        sleep(30)
                    else:
                        cs.print('[bold on blue]【Ok周志】: 主人，检测到您尚未选择或错选，我已自动进入`全自动`模式')
                        sleep(1)
                        self.inprr = '1'

        elif self.inprr == '1' and path.exists(r'C:\Ok周志\SysOk\OldUser.pkl'):
            cs.print('[bold on purple]【Ok周志】: 再次见到您我真高兴:grinning_squinting_face:')
            cs.print(choice(['【Ok周志】: 主人，偷偷告诉您，我和您一样也是有记忆的哦',
                             '【Ok周志】: 主人，当程序运行时，会自动在C盘生成Ok周志文件夹，里面的Sys和SysOk为程序系统文件夹，请勿擅自删除',
                             '【Ok周志】: 主人，身体第一，工作第二',
                             '【Ok周志】: 主人，早睡早起，身体好', '【Ok周志】: 主人，程序结束后，相关内容已经自动复制了',
                             '【Ok周志】: 若想支持我，就关注我的社交媒体账号吧！您的支持，是我们继续优化程序的最大动力',
                             '【Ok周志】: 主人，记得请不要依赖我，写周记也是一个好习惯', '【Ok周志】: 主人，笑一笑， 十年少',
                             '【Ok周志】: 主人，人之所以能，是因为相信能。加油，奥里给']), style='bold on blue')
            sleep(2)
            if path.exists(r'C:\Ok周志\SysOk\OldTime.pkl'):
                with open(r'C:\Ok周志\SysOk\OldTime.pkl', 'rb') as ffi:
                    addy, aad1, aad2 = load(ffi)
            else:
                addy = 2022
                aad1 = 10
                aad2 = 10
        tim = str(datetime.now().date()).split('-')
        year, month, day = int(tim[0]), int(tim[1]), int(tim[2])
        d1 = datetime(addy, aad1, aad2)
        d2 = datetime(year, month, day)
        self.distance = (d2 - d1).days
        self.timeNow = strftime('%Y年%m月%d日，现在是%H点%M分', localtime())
        self.timef = Fa.timeFly[randint(0, len(Fa.timeFly) - 1)]
        self.famou = Fa.famous[randint(0, len(Fa.famous) - 1)]
        self.qqyr = Fa.qyy[randint(0, len(Fa.qyy) - 1)]

        def xe1():
            yyy = ['这周我略读了一本书名叫: ', '这周我粗读了一本书名叫', '这周我细读了一本书名叫',
                   '这周我浏览了一本书名叫',
                   '在这周我略读了一本书名叫', '在这周我粗读了一本书名叫', '在这周我细读了一本书名叫',
                   '在这周我浏览了一本书名叫', '这周我又略读了一本书名叫: ', '这周我又粗读了一本书名叫',
                   '在这周我又浏览了一本书名叫']
            zzz = ['书中大致的内容是: ', '书中讲述了: ', '书中的核心内容是: ', '这本书讲述了: ',
                   '我为什么要读这本书，因为',
                   '我很喜欢这本书，因为', '书中的精华: ', '书中讲了: ', '很不错的一本本书，因为']
            contt = randint(0, 96)
            xxx = choice(yyy) + Fa.title1[contt] + choice(zzz) + Fa.content1[contt]
            yyy1 = ['这周休息的时候，我观看了一部电影名叫: ', '休息的时候，我观看了一部电影名叫: ',
                    '这周休息时，我观看了一部电影名叫:']
            zzz1 = ['电影讲述了: ', '电影描述了: ', '电影的情节是: ', '很不错的一部电影，因为: ',
                    '我很喜欢这部电影，因为: ']
            contt1 = randint(0, 30)
            xxx1 = choice(yyy1) + Fa.moviet[contt1] + choice(zzz1) + Fa.moviec[contt1]
            rrr = '以下是这周我在生活，工作和学习上的总结: \n' + choice([xxx, xxx, xxx1, xxx, xxx])
            self.totalTxt += rrr
            print(rrr)

        self.xeee = xe1

    def write(self):
        timess = self.distance / 7
        dd = ceil(timess)
        sjj = ptim.cschange(str(dd))
        sjj1 = ptim.schange(str(dd))
        print()
        cs.rule("[bold on green]正文开始:writing_hand:")
        cs.print(f'[bold cyan]标题: 第{sjj}次周志')
        self.totalTxt += f'标题: 第{sjj}次周志\n'
        kkk = ['转眼间', '时间真快', '眨眼间', '匆匆又匆匆', '时光飞逝', '日月如梭', '匆匆忙忙', '稍纵即逝', '一瞬间']
        kkk1 = choice(kkk)
        print(f'今天是{self.timeNow}，这是我写的第{sjj1}篇周志。\n{self.timef}，{kkk1}已经实习第{self.distance}天了。')
        self.totalTxt += f'今天是{self.timeNow}，这是我写的第{sjj1}篇周志。\n{self.timef}，{kkk1}已经实习第{self.distance}天了。'
        a1 = '这周过得很充实，'
        b1 = '因为完成了每日的计划清单和一周的小目标'
        a2 = '这周和往常一样，'
        b2 = '完成了自己该做的事情'
        a3 = '这周过得很愉快，'
        b3 = '因为学到了很多有用有趣的知识'

        dic = {a1: b1, a2: b2, a3: b3}
        dd = [a1, a2, a3]
        phase = choice(dd)
        print(phase, dic[phase] + '。')
        self.totalTxt += f'\n{phase}{dic[phase]}。\n'
        if self.inprr == '2':
            vvv = '以下是这周我在生活，工作和学习上的总结: \n'
            sto = "ok"
            txta = ""
            tip = '以下是这周我在生活，工作和学习上的总结: \n(标题/开头/结尾已自动填充，请输入大约60字即可)\n(温馨提示: 输入完成后，在首行输入ok再回车即可结束编辑)'
            print(tip)
            for line in iter(input, sto):
                txta += line
            self.totalTxt += vvv + txta
        elif self.inprr == '1':
            self.xeee()
        else:
            self.xeee()
        print('"' + self.famou + '"')
        self.totalTxt += '\n"' + self.famou + '"'
        lddd = ['加油', '继续努力！', '奋斗吧！', '冲啊', '继续加油', '明天会更好', '奥里给！', '冲冲冲！', '坚持！',
                '加油！',
                '奋斗吧', '冲啊！', '继续加油！', '明天会更好！', '奥里给！', '坚持！', '相信自己，加油！', '明天一定会更好！']
        ccce = choice(lddd)
        print(self.qqyr + ccce)
        self.totalTxt += f'\n{self.qqyr}{ccce}'
        copy(self.totalTxt)
        cs.rule("[bold on green]正文结束:hundred_points:")
        print()
        filen = strftime('%Y%m%d', localtime())
        jjs = sjj1
        namm = f'周志({jjs}){filen}.txt'
        with open(f'C:\Ok周志\{namm}', 'w', encoding='UTF-8') as fhj:
            fhj.write(self.totalTxt)
        with open(f'C:\Okroie\{namm}', 'w', encoding='UTF-8') as fkl:
            fkl.write(self.totalTxt)
        if path.exists(path.join(path.expanduser("~"), 'Desktop')):
            with open(path.join(path.expanduser("~"), f'Desktop\{namm}'), 'w', encoding='UTF-8') as fty:
                fty.write(self.totalTxt)
        self.filename = f'C:/Ok周志/周志({jjs}){filen}.txt'
        texttot = self.totalTxt.replace('\n', '').strip()
        dic2 = {}
        for j in self.totalTxt.replace('\n', '').strip():
            dic2[j] = dic2.get(j, 0) + 1
        lis2 = list(dic2.items())
        lis2.sort(key=lambda x: -x[1])
        cs.print(
            f'[bold white on green](当前文章总字数为: {len(texttot)}，出现次数最多的字符: ' + f'`{lis2[0][0]}` {lis2[0][1]}次。' + f'正文已保存到: `{self.filename}`)')
        cs.print(Panel.fit('[bold blue]主人，我已将正文内容自动复制，只需去粘贴即可', border_style='red'))
        if not path.exists(r'C:\Ok周志\SysOk\OldUser.pkl'):
            with open(r'C:\Ok周志\SysOk\OldUser.pkl', 'w'):
                pass
        sleep(2)
        cs.print('\n[bold on yellow]【Ok周志】: 这是最平凡的一天啊，您也要开心哈:grinning_face_with_smiling_eyes:')
        cs.print(
            '[bold on purple]主人:thumbs_up:，今天您签到了吗？下次再见:hand_with_fingers_splayed:爱您的【Ok周志】:red_heart:')
        if not path.exists(r'C:\Ok周志\SysOk\B.mp3'):
            oridd = b64decode(Fa.assa1)
            with open('C:\Ok周志\SysOk\B.mp3', 'wb') as fout:
                fout.write(oridd)
        sleep(1)
        timb = choice([3, 5, 6, 7, 8, 9, 10, 11, 12])
        cs.print(f'\n[bold on blue]:helicopter:{timb}秒后进入Okroie官网（一个分享学习资料&编程技术的网站）:telescope:')
        sleep(1)
        for i in range(timb, 0, -1):
            cs.print('[bold cyan]:ten_o’clock:倒计时:', i)
            sleep(1)
        music.stop()
        cs.print('\n\n[bold on blue]【Ok周志]: 主人，两分钟后我会自动关闭:zany_face:')
        sleep(1)
        system(r'C:\Ok周志\SysOk\B.mp3')
        open_new('http://okroie.cn')
        sleep(120)
        exit()


def main():
    hsl = ZhouZhi()
    hsl.write()
