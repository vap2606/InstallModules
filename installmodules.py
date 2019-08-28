from pywinauto.application import Application
import time
path = "C:\\Program Files (x86)\\ISS\\SecurOS\\Modules\\"


def test_install_auto():
    app = Application(backend="uia").start(r'C:\\SecurOS_Auto_10.4.64.exe')
    time.sleep(20)
    app.connect(title='Выберите язык установки')
    dlg = app.window(title="Выберите язык установки")
    dlg.OK.click()
    time.sleep(5)
    app = Application(backend="uia")
    app.connect(title='Установка — SecurOS Auto')
    dlg = app.window(title='Установка — SecurOS Auto')
    dlg.Далее.click()
    time.sleep(1)
    dlg.Парольпользователя_Edit.set_text('auto')
    dlg.Подтвердитепарольпользователя_Edit.set_text('auto')
    dlg.Далее.click()
    time.sleep(1)
    dlg.Далее.click()
    time.sleep(1)
    dlg.Далее.click()
    time.sleep(1)
    dlg.Далее.click()
    time.sleep(1)
    dlg.Установить.click()
    time.sleep(30)
    dlg.Завершить.click()

   