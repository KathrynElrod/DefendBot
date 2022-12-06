import subprocess
import time
import random

def run_script(script: str) -> str:
    new_script = []
    for line in script.splitlines():
        new_script.append('-e')
        new_script.append(line)
    process = subprocess.Popen(['osascript']+new_script, stdout=subprocess.PIPE)
    return process.communicate()[0].decode('ascii','replace')

def open_url(url: str, random_size: bool = True, private: bool = True):
    run_script("""tell application "Safari"
activate
end tell""")
    keystroke('"N" using '+('{shift down, command down}' if private else 'command down'), text=False)
    if random_size:
        run_script("""tell application "Safari"
set bounds of front window to {0, 0, """+str(random.randint(600,900))+', '+str(random.randint(600,900))+"""}
end tell""")
    keystroke(url, humanlike=False)
    keystroke('return', text=False)

def close_tab():
    run_script("""tell application "Safari"
close current tab of front window
end tell""")

def keystroke(keys: str, text: bool = True, humanlike: bool = True):
    if humanlike and text:
        for char in keys:
            keystroke(char, text=True, humanlike=False)
            time.sleep(random.randint(2,25)/100)
    else:
        if text:
            keys = '"'+keys+'"'
        run_script("""tell application "Safari"
tell application "System Events"
keystroke """+keys+"""
end tell
end tell""")

def javascript(command: str) -> str:
    return run_script("""tell application "Safari"
return do JavaScript \""""+command+"""\" in document 1
end tell""")

def get_value_of_id(id: str) -> str:
    return javascript("document.getElementById('"+id+"').value;")

def get_value_of_class(name: str, index: int = 0) -> str:
    return javascript("document.getElementsByClassName('"+name+"')["+str(index)+"].value;")

def set_value_of_id(id: str, value: str, text: bool = True):
    if text: value = "'"+value+"'"
    javascript("document.getElementById('"+id+"').value = "+value+";")

def set_value_of_class(name: str, value: str, index: int = 0, text: bool = True):
    if text: value = "'"+value+"'"
    javascript("document.getElementsByClassName('"+name+"')["+str(index)+"].value = "+value+";")

def click_id(id: str):
    javascript("document.getElementById('"+id+"').click();")

def click_class(name: str, index: int = 0):
    javascript("document.getElementsByClassName('"+name+"')["+str(index)+"].click();")

def focus_id(id: str):
    javascript("document.getElementById('"+id+"').focus();")

def focus_class(name: str, index: int = 0):
    javascript("document.getElementsByClassName('"+name+"')["+str(index)+"].focus();")