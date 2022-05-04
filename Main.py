# this is the local enviroment I am using 
# laser_switch_efrat_shema
# install the following packages:
# 1. pip install pywinauto
# dlg.set_focus()
# conda activate laser_switch_efrat_shema & python d:\github\Efrat_Shema_Switching_Laser_Project\Main.py

# To press Ctrl+Alt+V: send_keys(‘^%V’)
from pywinauto import application, keyboard
from time import sleep

app = application.Application()
app.connect(path=r"C:\windows\system32\win32Calc.exe")
dlg = app['Calculator']
#dlg.set_focus()
#dlg.set_keyboard_focus()

#print(dlg.is_maximized())
dlg.send_keystrokes('%1', with_spaces=False, with_tabs=False, with_newlines=False)
sleep(1)
dlg.send_keystrokes('%2', with_spaces=False, with_tabs=False, with_newlines=False)


'''

sleep(1)
dt = 0.1
for i in range(10):
    keyboard.send_keys('%1')
    #sleep(dt)
    keyboard.send_keys('%2')
    #sleep(dt)
    print(i)
'''

'''
# java beans code that worked to run the file seperately
Runtime r = Runtime.getRuntime();
Process p;

script_path = "D:\\github\\Efrat_Shema_Switching_Laser_Project\\Main.py";
conda_env_name = "laser_switch_efrat_shema";


p = r.exec("cmd /c conda activate " + conda_env_name + " & python " + "\"" + script_path + "\"");
	
BufferedReader stdInput = new BufferedReader(new InputStreamReader(p.getInputStream()));
BufferedReader stdError = new BufferedReader(new InputStreamReader(p.getErrorStream()));
	
// print output from program
while ((s=stdInput.readLine()) != null){print(s);}
	
// print errors from program
while ((s=stdError.readLine()) != null){print(s);}

'''

'''
String urlString = "http://127.0.0.1:80/change_to_Laser_1";
URL url = new URL(urlString);
URLConnection conn = url.openConnection();
InputStream is = conn.getInputStream();

Thread.sleep(1000);

urlString = "http://127.0.0.1:80/change_to_Laser_2";
URL url = new URL(urlString);
URLConnection conn = url.openConnection();
InputStream is = conn.getInputStream();
'''