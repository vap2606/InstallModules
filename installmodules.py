from pywinauto.application import Application
import time
path = "C:\\Program Files (x86)\\ISS\\SecurOS\\Modules\\"


def test_open_install_file():
    app = Application(backend="uia").start(r'C:\\SecurOS_Auto_10.4.43.exe')
    dlg = app.window(title="Выберите язык установки")
    time.sleep(20)
    #dlg.wait('exists')
    dlg.child_window(auto_id="1").select("Русский")
    dlg.OK.click()
    app1 = Application(backend="uia").connect(title='SecurOS Enterprise - InstallShield Wizard')
    dlg1 = app1.window(title='SecurOS Enterprise - InstallShield Wizard')
    dlg1.wait('exists')
    dlg1.Далее.click()
    dlg1.Япринимаюусловиялицензионногосоглашения.click()
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Далее.click()
    time.sleep(1)
    dlg1.Установить.click()
    time.sleep(150)
    dlg1.Готово.click()

