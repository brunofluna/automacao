# importar a biblioteca de automação
# NOTE: instale a biblioteca: pip install pyautogui
import pyautogui as auto
import cx_Freeze

# atrasar os comandos da biblioteca em meio segundo
auto.PAUSE = 0.5

auto.press('win') # abre o menu iniciar
auto.write('chrome') # digita a palavra chrome
auto.press('enter')# aperta o enter
auto.hotkey('alt', 'space')
auto.press('x')
auto.write('github.com') # acessa o site do github
auto.press('enter')
# para entrar na página de login do github
for i in range(12):
    auto.press('tab')

auto.press('enter') # aperta o enter
auto.write('brunofluna')
auto.press('enter')
auto.write('R@fael1050')
auto.press('enter')


