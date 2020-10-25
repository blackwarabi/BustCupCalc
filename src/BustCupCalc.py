# coding: utf-8
'''
Created on 2020/01/25

@author: gon
'''
import PySimpleGUI as sg
import re
import os

opai = ['AAAカップ未満(無乳)',
            'AAAカップ(微乳)',
            'AAカップ(微乳)',
            'Aカップ(微乳)',
            'Bカップ(普乳)',
            'Cカップ(普乳)',
            'Dカップ(適乳)',
            'Eカップ(巨乳)',
            'Fカップ(巨乳)',
            'Gカップ(爆乳)',
            'Hカップ(爆乳)',
            'Iカップ(爆乳)',
            'Jカップ(魔乳)',
            'Kカップ(魔乳)',
            'Lカップ(魔乳)',
            'Mカップ(魔乳)',
            'Nカップ(超乳)',
            'Oカップ(超乳)',
            'Pカップ(超乳)',
            'Pカップ以上(神乳)',
            '身長が未入力、または不正な値です',
            'バストが未入力、または不正な値です',
            'ウエストが未入力、または不正な値です']

def calcMain():
    sg.theme('DarkAmber')

    layout = [
                [sg.Text('各パラメータを入力',size=(32,1))],
                [sg.Text('身長',size=(8,1)), sg.InputText('', size=(8,1),key='height')],
                [sg.Text('バスト',size=(8,1)), sg.InputText('', size=(8,1), key='bust')],
                [sg.Text('ウエスト',size=(8,1)), sg.InputText('', size=(8,1), key='waist')],
                [sg.Button('測定', key='measurement'),sg.Button('クリア', key='clear')],
                [sg.Button('一つ前の測定値を復元', key='history')],
                [sg.Output(size=(30, 10),key='output')]
            ]
    window = sg.Window('おっぱいスクリプト Ver1.2', layout)
    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == 'clear':
            window['height'].update('')
            window['bust'].update('')
            window['waist'].update('')
            window['output'].update('')

        if event == 'measurement':
            #入力値をfloatへ型変換
            f_height = 0.0
            f_bust = 0.0
            f_waist = 0.0
            difference = 0.0
            #正規表現
            regex = re.compile(r'[0-9\.]')

            if regex.search(values['height']) != None and regex.search(values['bust']) != None and regex.search(values['waist']) != None:
                f_height = float(values['height'])
                f_bust = float(values['bust'])
                f_waist = float(values['waist'])
                #バストカップ数計算
                difference = (f_bust - (f_height * 0.54)) + (((f_height * 0.38) - f_waist) * 0.73) + ((f_height - 158.8) * 0.1087)

                #計算結果から何カップか判定
                if  f_height <= 0.0:
                    num = 20
                elif f_bust <= 0.0:
                    num = 21
                elif f_waist <= 0.0:
                    num = 22
                elif difference < -13.75:
                    num = 0
                elif difference < -11.25:
                    num = 1
                elif difference < -8.75:
                    num = 2
                elif difference < -6.25:
                    num = 3
                elif difference < -3.75:
                    num = 4
                elif difference < -1.25:
                    num = 5
                elif difference < 1.25:
                    num = 6
                elif difference < 3.75:
                    num = 7
                elif difference < 6.25:
                    num = 8
                elif difference < 8.75:
                    num = 9
                elif difference < 11.25:
                    num = 10
                elif difference < 13.75:
                    num = 11
                elif difference < 16.25:
                    num = 12
                elif difference < 18.75:
                    num = 13
                elif difference < 21.25:
                    num = 14
                elif difference < 23.75:
                    num = 15
                elif difference < 26.25:
                    num = 16
                elif difference < 28.75:
                    num = 17
                elif difference < 31.25:
                    num = 18
                else:
                    num = 19
                os.makedirs('./history', exist_ok=True)
                textwrite('old.txt', values['height'],values['bust'],values['waist'])
                print(opai[num])

            else:
                print('不正な値が入力されています。')
        if event == 'history':
            readlist = textread('old.txt').split('\n')
            oldheight =  readlist[0]
            oldbust = readlist[1]
            oldwaist = readlist[2]
            window['height'].update(oldheight)
            window['bust'].update(oldbust)
            window['waist'].update(oldwaist)

    window.close()

def textread(filename):
    readtext = open('./history/'+filename)
    readlist = readtext.read()
    return readlist

def textwrite(filename,writeheight,writebust,writewaist):
    writetext = open('./history/'+filename, 'w')
    writetext.write(writeheight+'\n'+writebust+'\n'+writewaist)
    writetext.close()

calcMain()