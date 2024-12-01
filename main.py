#!/usr/bin/python

import random
import requests
from time import sleep
import os, signal, sys
from pyfiglet import figlet_format
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.text import Text
from rich.style import Style
import pystyle
from pystyle import Colors, Colorate

from carparktool import CarParkTool

__CHANNEL_USERNAME__ = "Klowee24"
__GROUP_USERNAME__   = "Klowee24"

def signal_handler(sig, frame):
    print("\n Bye Bye...")
    sys.exit(0)

def gradient_text(text, colors):
    lines = text.splitlines()
    height = len(lines)
    width = max(len(line) for line in lines)
    colorful_text = Text()
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char != ' ':
                color_index = int(((x / (width - 1 if width > 1 else 1)) + (y / (height - 1 if height > 1 else 1))) * 0.5 * (len(colors) - 1))
                color_index = min(max(color_index, 0), len(colors) - 1)  # Ensure the index is within bounds
                style = Style(color=colors[color_index])
                colorful_text.append(char, style=style)
            else:
                colorful_text.append(char)
        colorful_text.append("\n")
    return colorful_text

def banner(console):
    os.system('cls' if os.name == 'nt' else 'clear')
    brand_name = figlet_format('klowee24', font='bloody')
    colors = [
        "rgb(255,0,0)", "rgb(255,69,0)", "rgb(255,140,0)", "rgb(255,215,0)", "rgb(173,255,47)", 
        "rgb(0,255,0)", "rgb(0,255,255)", "rgb(0,191,255)", "rgb(0,0,255)", "rgb(139,0,255)",
        "rgb(255,0,255)"
    ]
    colorful_text = gradient_text(brand_name, colors)
    console.print(colorful_text)
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))
    print(Colorate.Horizontal(Colors.rainbow, '\t         𝐏𝐋𝐄𝐀𝐒𝐄 𝐋𝐎𝐆𝐎𝐔𝐓 𝐅𝐑𝐎𝐌 𝐂𝐏𝐌 𝐁𝐄𝐅𝐎𝐑𝐄 𝐔𝐒𝐈𝐍𝐆 𝐓𝐇𝐈𝐒 𝐓𝐎𝐎𝐋'))
    print(Colorate.Horizontal(Colors.rainbow, '    𝐒𝐇𝐀𝐑𝐈𝐍𝐆 𝐓𝐇𝐄 𝐀𝐂𝐂𝐄𝐒𝐒 𝐊𝐄𝐘 𝐈𝐒 𝐍𝐎𝐓 𝐀𝐋𝐋𝐎𝐖𝐄𝐃 𝐀𝐍𝐃 𝐖𝐈𝐋𝐋 𝐁𝐄 𝐁𝐋𝐎𝐂𝐊𝐄𝐃')) 
    print(Colorate.Horizontal(Colors.rainbow, '      𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐌𝐄 𝐓𝐎 𝐁𝐔𝐘 𝐔𝐍𝐋𝐈𝐌𝐈𝐓𝐄𝐃 𝐁𝐀𝐋𝐀𝐍𝐂𝐄 𝐓𝐆 @Kloweee24 ')) 
    print(Colorate.Horizontal(Colors.rainbow, f' ‌           𝐓𝐞𝐥𝐞𝐠𝐫𝐚𝐦: @{Klowee} 𝐎𝐫 @{Klowee}'))
    print(Colorate.Horizontal(Colors.rainbow, '=================================================================='))
            elif login_response == 101:
                print(Colorate.Horizontal(Colors.rainbow, 'WRONG PASSWORD.'))
                sleep(2)
                continue
            elif login_response == 103:
                print(Colorate.Horizontal(Colors.rainbow, 'INVALID ACCESS KEY.'))
                sleep(2)
                continue
            else:
                print(Colorate.Horizontal(Colors.rainbow, 'TRY AGAIN.'))
                print(Colorate.Horizontal(Colors.rainbow, '! Note: make sure you filled out the fields !.'))
                sleep(2)
                continue
        else:
            print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL.'))
            sleep(2)
        while True:
            banner(console)
            load_player_data(cpm)
            load_key_data(cpm)
            load_client_details()
            choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
            print(Colorate.Horizontal(Colors.yelloe, '{01}: Increase Money           1.000K'))
            print(Colorate.Horizontal(Colors.yellow, '{02}: Increase Coins           3.500K'))
            print(Colorate.Horizontal(Colors.yellow, '{03}: King Rank                4.000K'))
            print(Colorate.Horizontal(Colors.yellow, '{04}: Change ID                3.500K'))
            print(Colorate.Horizontal(Colors.yellow, '{05}: Change Name              1.00'))
            print(Colorate.Horizontal(Colors.yellow, '{06}: Change Name (Rainbow)    1.00'))
            print(Colorate.Horizontal(Colors.yellow, '{07}: Number Plates            2.000K'))
            print(Colorate.Horizontal(Colors.yellow, '{08}: Account Delete           FREE'))
            print(Colorate.Horizontal(Colors.yellow, '{09}: ccount Register          FREE'))
            print(Colorate.Horizontal(Colors.yellow, '{10}: Delete Friends           5.00'))
            print(Colorate.Horizontal(Colors.yellow, '{11}: Unlock Paid Cars         4.000K'))
            print(Colorate.Horizontal(Colors.yellow, '{12}: Unlock all Cars          3.000K'))
            print(Colorate.Horizontal(Colors.yellow, '{13}: Unlock all Cars Siren    2.000K'))
            print(Colorate.Horizontal(Colors.yellow, '{14}: Unlock w16 Engine        3.000K'))
            print(Colorate.Horizontal(Colors.yellow, '{15}: Unlock All Horns         3.000K'))
            print(Colorate.Horizontal(Colors.yellow, '{16}: Unlock Disable Damage    2.000K'))
            print(Colorate.Horizontal(Colors.yellow, '{17}: Unlock Unlimited Fuel    2.000K'))
            print(Colorate.Horizontal(Colors.yellow, '{18}: Unlock House 3           3.500K'))
            print(Colorate.Horizontal(Colors.yellow, '{19}: Unlock Smoke             2.000K'))
            print(Colorate.Horizontal(Colors.yellow, '{20}: Change Race Wins         1.000K'))
            print(Colorate.Horizontal(Colors.yellow, '{21}: Change Race Loses        1.000K'))
            print(Colorate.Horizontal(Colors.yellow, '{22}: Clone Account            5.000K'))
            print(Colorate.Horizontal(Colors.yellow, '{0} : Exit'))
            print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐂𝐏𝐌☆ ]==============='))
            
            service = IntPrompt.ask(f"[bold][?] Select a Service [red][1-{choices[-1]} or 0][/red][/bold]", choices=choices, show_choices=False)
            
            print(Colorate.Horizontal(Colors.rainbow, '===============[ 𝐂𝐏𝐌☆ ]==============='))
            
            if service == 0: # Exit
                print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channel: @{__CHANNEL_USERNAME__}.'))
            elif service == 1: # Increase Money
                print(Colorate.Horizontal(Colors.rainbow, '[?] Insert how much money do you want.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 999999999:
                    if cpm.set_player_money(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 2: # Increase Coins
                print(Colorate.Horizontal(Colors.rainbow, '[?] Insert how much coins do you want.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Saving your data: ", end=None)
                if amount > 0 and amount <= 999999999:
                    if cpm.set_player_coins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 3: # King Rank
                console.print("[bold red][!] Note:[/bold red]: if the king rank doesn't appear in game, close it and open few times.", end=None)
                console.print("[bold red][!] Note:[/bold red]: please don't do King Rank on same account twice.", end=None)
                sleep(2)
                console.print("[%] Giving you a King Rank: ", end=None)
                if cpm.set_player_rank():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 4: # Change ID
                print(Colorate.Horizontal(Colors.rainbow, '[?] Enter your new ID.'))
                new_id = Prompt.ask("[?] ID")
                console.print("[%] Saving your data: ", end=None)
                if len(new_id) >= 0 and len(new_id) <= 999999999 and (' ' in new_id) == False:
                    if cpm.set_player_localid(new_id.upper()):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid ID.'))
                    sleep(2)
                    continue
            elif service == 5: # Change Name
                print(Colorate.Horizontal(Colors.rainbow, '[?] Enter your new Name.'))
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                if len(new_name) >= 0 and len(new_name) <= 999999999:
                    if cpm.set_player_name(new_name):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 6: # Change Name Rainbow
                print(Colorate.Horizontal(Colors.rainbow, '[?] Enter your new Rainbow Name.'))
                new_name = Prompt.ask("[?] Name")
                console.print("[%] Saving your data: ", end=None)
                          answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 16: # Disable Engine Damage
                console.print("[%] Unlocking Disable Damage: ", end=None)
                if cpm.disable_engine_damage():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 17: # Unlimited Fuel
                console.print("[%] Unlocking Unlimited Fuel: ", end=None)
                if cpm.unlimited_fuel():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 18: # Unlock House 3
                console.print("[%] Unlocking House 3: ", end=None)
                if cpm.unlock_houses():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 19: # Unlock Smoke
                console.print("[%] Unlocking Smoke: ", end=None)
                if cpm.unlock_smoke():
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                    sleep(2)
                    continue
            elif service == 20: # Change Races Wins
                print(Colorate.Horizontal(Colors.rainbow, '[!] Insert how much races you win.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999999999:
                    if cpm.set_player_wins(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, 'Please try again.'))
                        sleep(2)
                        continue
                else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 21: # Change Races Loses
                print(Colorate.Horizontal(Colors.rainbow, '[!] Insert how much races you lose.'))
                amount = IntPrompt.ask("[?] Amount")
                console.print("[%] Changing your data: ", end=None)
                if amount > 0 and amount <= 999999999999999999999:
                    if cpm.set_player_loses(amount):
                        print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                        print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                        answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                        if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                        else: continue
                    else:
                        print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                        print(Colorate.Horizontal(Colors.rainbow, '[!] Please use valid values.'))
                        sleep(2)
                        continue
                      else:
                    print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Please use valid values.'))
                    sleep(2)
                    continue
            elif service == 22: # Clone Account
                print(Colorate.Horizontal(Colors.rainbow, '[!] Please Enter Account Detalis.'))
                to_email = prompt_valid_value("[?] Account Email", "Email", password=False)
                to_password = prompt_valid_value("[?] Account Password", "Password", password=False)
                console.print("[%] Cloning your account: ", end=None)
                if cpm.account_clone(to_email, to_password):
                    print(Colorate.Horizontal(Colors.rainbow, 'SUCCESSFUL'))
                    print(Colorate.Horizontal(Colors.rainbow, '======================================'))
                    answ = Prompt.ask("[?] Do You want to Exit ?", choices=["y", "n"], default="n")
                    if answ == "y": print(Colorate.Horizontal(Colors.rainbow, f'Thank You for using our tool, please join our telegram channe: @{__CHANNEL_USERNAME__}.'))
                    else: continue
            else:
                    
                print(Colorate.Horizontal(Colors.rainbow, 'FAILED.'))
                    print(Colorate.Horizontal(Colors.rainbow, '[!] Please use valid values.'))
                    sleep(2)
                    continue
            else: continue
            break
                      
