# %%
import pyautogui as ag
import keyboard as kb
import pyperclip as toClipboard
from  pynput.keyboard import Key, Listener
from PIL import ImageGrab
from functools import partial


# %%
atalho = 'ctrl+print_screen'
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)



# %%
def colorpicker():
    x , y = ag.position()
    print("Posição do mouse")
    print("x = "+str(x)+"y = "+str(y))

    #retorna True se x & y estiverem dentro da tela
    print ("\nEsta dentro da tela?")
    resp = ag.onScreen(x, y)
    print (str(resp))

    screen = ag.screenshot()
    screen.save('C:/dev/python/web-developer-suite/prints/print.jpg')
    colorRGB = screen.getpixel((x,y))
    colorHEX = '#%02x%02x%02x' % (colorRGB)

    print(colorRGB)
    print(colorHEX)

    toClipboard.copy(colorHEX)




# %%

# def on_press(key):
#     print('{0} pressed'.format(
#         key))

# def on_release(key):
#     print('{0} release'.format(
#         key))
#     if key == Key.esc:
#         # Stop listener
#         return False

# # Collect events until released
# with Listener(
#         on_press=on_press,
#         on_release=on_release) as listener:
#     listener.join()

# %%
kb.add_hotkey(atalho,colorpicker)
kb.wait('esc')





