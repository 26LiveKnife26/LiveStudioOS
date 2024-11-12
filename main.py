print("BOOTING...")
import flet as ft
import pynput
import os
import psutil
import socket
import bluetooth
import time
import functions as func
import requests
global keyboard
global true
global false
true = True
false = False
keyboard = pynput.keyboard.Controller()
def main(app: ft.Page):
    app.title = "LiveStudioOS"
    app.theme_mode = "light"
    app.window.full_screen = true
    def up_volume(e):
        keyboard.press(pynput.keyboard.Key.media_volume_up)
        keyboard.release(pynput.keyboard.Key.media_volume_up)
    def down_volume(e):
        keyboard.press(pynput.keyboard.Key.media_volume_down)
        keyboard.release(pynput.keyboard.Key.media_volume_down)
    def toggle_theme(e):
        app.theme_mode = "light" if app.theme_mode == "dark" else "dark"
        app.update()
    def is_connected_to_wifi():
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            return False
    def toogle_Wifi(e):
        if is_connected_to_wifi():
            os.system("nmcli radio wifi off")
        else:
            os.system("nmcli radio wifi on")
    def quit(e):
        app.window.close()
    gl_menu = ft.AlertDialog(
        modal = True,
        title = "LiveStudioOS",
        content = "LiveStudioOS 1.0. Главное меню.",
        actions = [
            ft.TextButton("Выход", on_click = quit)
        ],
    )
    devices = output = """
""".join([f"{key.capitalize()}: {value}" for key, value in func.list_of_devices.items()])
    bluet = ft.AlertDialog(
        title = ft.Text(f"""Найдено: {func.number_of_devices} устройств
{devices}""")
    )
    response = requests.get(url=f'http://ip-api.com/json/').json()
    user_inform = ft.Text(f"""Ваша информация:
IP: {response.get('query')}
Регион времени: {response.get('timezone')}
Организация: {response.get('org')}
Провайдер: {response.get('as')}
ISP: {response.get('isp')}
Город: {response.get('city')}
Страна: {response.get('country')}
Почтовый индекс: {response.get('zip')}
Долгота: {response.get('lat')}
Ширина: {response.get('lon')}""")
    user_information = ft.AlertDialog(
        title = user_inform
    )
    times = ft.Text("", size = 20)
    battery = ft.Text("", size = 20)
    theme = ft.IconButton(icon = ft.icons.LIGHT_MODE, on_click = toggle_theme)
    volume_up_up = ft.IconButton(icon = ft.icons.VOLUME_UP, on_click = up_volume)
    volume_down_down = ft.IconButton(icon = ft.icons.VOLUME_DOWN, on_click = down_volume)
    wifi = ft.IconButton(icon = ft.icons.WIFI, on_click = toogle_Wifi)
    user_info = ft.IconButton(icon = ft.icons.INFO, on_click = lambda e: app.open(user_information))
    bluetooths = ft.IconButton(icon = ft.icons.BLUETOOTH, on_click = lambda e: app.open(bluet))
    process = psutil.Process()
    memory_info = process.memory_info()
    rss = memory_info.rss
    os_used = ft.TextButton(text = "")
    app.add(
        ft.Row(
            [
                ft.Text("❤𝙇𝙞𝙫𝙚𝙎𝙩𝙪𝙙𝙞𝙤𝙊𝙎❤", size = 23, color = "#FF7C7C")
            ], alignment = ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                bluetooths,
                theme,
                volume_down_down,
                times,
                battery,
                volume_up_up,
                wifi,
                user_info
            ], alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                os_used
            ], alignment = ft.MainAxisAlignment.CENTER
        )
    )
    def UPDATE_WHILE_TRUE():
        while True:
            times.value = time.strftime("%H:%M:%S")
            battery.value = f"{int(psutil.sensors_battery().percent)}%"
            if app.theme_mode == "light":
                theme.icon = ft.icons.LIGHT_MODE
            else:
                theme.icon = ft.icons.DARK_MODE
            if is_connected_to_wifi():
                wifi.icon = ft.icons.WIFI
            else:
                wifi.icon = ft.icons.WIFI_OFF
                exit("!!!YOU NOT CONNECTED TO WIFI!!")
            os_used.text = f"𝙊𝙎 𝙐𝙎𝙀𝘿 {rss / (1024 * 1024):.2f} 𝙈𝘽"
            response = requests.get(url=f'http://ip-api.com/json/').json()
            app.update()
    UPDATE_WHILE_TRUE()
print("SYSTEM IS READY!")
ft.app(target = main)
# 𝙍𝘼𝙈 𝙐𝙎𝙀𝘿 {psutil.virtual_memory().used / (1024 ** 2):.2f} 𝙈𝘽 / {psutil.virtual_memory().total / (1024 ** 2):.2f} 𝙈𝘽