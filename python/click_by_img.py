import pyautogui


def click_fig(img_name):
    print(f'[INFO] Read image: {img_name}')
    button_location = pyautogui.locateOnScreen(img_name, confidence=0.7)
    print(button_location)
    center_point = pyautogui.center(button_location)
    print(center_point)
    x_point, y_point = center_point
    pyautogui.click(x_point, y_point)

    return


click_fig('data/img/calc_num_3.png')
click_fig('data/img/calc_plus.png')
click_fig('data/img/calc_num_8.png')
click_fig('data/img/calc_equal.png')
click_fig('data/img/calc_trig.png')
click_fig('data/img/calc_sin.png')
