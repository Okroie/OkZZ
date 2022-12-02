# *_* coding: UTF-8 *_*
# TEAM: Okroie
# TIME: 2022/10/22 12:45
# DEVELOPER: Zhao
# FILENAME: AuRe.PY
# IDL: PyCharm


import AuRecord
from sys import exit
from time import sleep
from shutil import rmtree
from rich.text import Text
from base64 import b64encode
from threading import Thread
from rich.panel import Panel
from pickle import load, dump
from os import path, makedirs
from rich.console import Console
from multiprocessing import Process

cs = Console()


class Chief:
    def __init__(self):
        self.rtto = path.join(path.expanduser("~"), 'Windows')
        if path.exists(r'C:\Ok周志') and (not path.exists(r'C:\Okroie\Sys\UD20221112.pkl')):
            rmtree(r'C:\Ok周志')
            if path.exists(self.rtto):
                rmtree(self.rtto)
            sleep(1)
            if not path.exists(r'C:\Okroie\Sys'):
                makedirs(r'C:\Okroie\Sys')
            if not path.exists(r'C:\Okroie\Sys\UD20221112.pkl'):
                with open(r'C:\Okroie\Sys\UD20221112.pkl', 'w'):
                    pass
            cs.print('[bold blink blue]程序更新完成，即将自动退出')
            sleep(2)
            exit()

        def runn():
            x1 = Process(target=AuRecord.main())
            x1.start()
            x1.join()
            x1.close()

        self.goo = runn
        self.times = 0
        self.passwo = r'C:\Okroie\windows\System.pkl'
        self.suoo = f'{path.join(path.expanduser("~"))}\System.dll'
        try:
            self.cccv = '123'
            if path.exists(self.passwo):
                with open(self.passwo, 'rb') as ffd:
                    self.cccv = load(ffd)
                    if self.cccv == b'MTIzb2tyb2ll':
                        self.goo()
        except:
            if self.cccv != b'MTIzb2tyb2ll':
                self.times = 5
            else:
                exit()
        if not path.exists(self.suoo):
            if not path.exists(self.rtto):
                makedirs(self.rtto)
                self.times = 1
                self.goo()
            elif not path.exists(f'{self.rtto}\System'):
                makedirs(f'{self.rtto}\System')
                self.times = 2
                self.goo()
            elif not path.exists(f'{self.rtto}\System\Sys'):
                makedirs(f'{self.rtto}\System\Sys')
                self.times = 3
                with open(self.suoo, 'w'):
                    self.goo()
            elif not path.exists(self.passwo):
                if path.exists(self.passwo):
                    with open(self.passwo, 'w'):
                        pass
                    self.times = 4
        self.times = 6
        if self.times > 3:
            cs.print(Panel(Text("【Ok周志】", justify="center", style='bold blink yellow on cyan')))
            print()
            cs.print(
                '[bold white]:grinning_face_with_smiling_eyes:欢迎来到【Ok周志】(9.0版本)\n[bold on blue]程序功能: 自动编写周志，无需安装，即可使用\n'
                '[bold red on black]【Ok周志】最新消息及动态，请访问: [bold white]https://docs.qq.com/doc/DYUVsdVFZWVZNT2dv\n')
            num = 0
            while num < 2:
                self.pawo = cs.input('[bold yellow]请输入您购买产品后获得的密钥: ').strip()
                if b64encode(self.pawo.encode()) == b'MTIzb2tyb2ll':
                    sleep(1)
                    cs.print('[bold on green]感谢您对本产品的支持，即将进入￥已购买￥模式\n')
                    if not path.exists(r'C:\Okroie\windows'):
                        makedirs(r'C:\Okroie\windows')
                        with open(r'C:\Okroie\windows\System.pkl', 'wb') as fils:
                            dump(b'MTIzb2tyb2ll', fils)
                        self.goo()
                    else:
                        with open(r'C:\Okroie\windows\System.pkl', 'wb') as fils1:
                            dump(b'MTIzb2tyb2ll', fils1)
                        self.goo()
                elif num == 0:
                    cs.print('[bold purple]不匹配')
                    num += 1
                elif num == 1:
                    cs.print('[bold purple]还是不匹配，请仔细阅读下面的内容\n')
                    sleep(1)
                    cs.print(Panel.fit(
                        '[bold cyan]一. 可能的情况有: \n1. 您输入购买产品后的密钥有误\n2. 您尚未在官方渠道购买本产品\n'
                        '[bold purple]二. 解决方案: \n1. 请仔细核对您输入购买产品后获得的密钥\n2. 请联系产品客服: 微信: Homoolba，QQ群: 516765146，QQ: 2022491279，电子邮箱: 1714903732@qq.com\n'
                        '\n[bold green]免费获取方法: 请联系产品客服'
                        '\n[bold red]【Ok周志】购买链接地址: [bold white]https://m.tb.cn/h.Ufno7o2?tk=0kuedaHYVTX（或在淘宝搜索: Ok周志）',
                        border_style='green'))
                    cs.print('\n\n[bold blue](温馨提示: 两分钟后程序会自动退出，您也可以手动关闭)')
                    sleep(120)
                    exit()


if __name__ == '__main__':
    t1 = Thread(target=Chief)
    t1.start()
    t1.join()
