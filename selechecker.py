import chromedriver_autoinstaller
import os


def driver_check():
    driver_install_path = f'{os.getcwd()}\\lib\\chromedriver'
    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    driver_path = f'{driver_install_path}\\{chrome_ver}\\chromedriver.exe'

    if os.path.exists(driver_path):
        print(f'chrome driver is installed: {driver_path}')
    else:
        print(f'chrome driver is not installed.')
        print(f'install the chrome driver(ver: {chrome_ver})')
        if not os.path.exists(driver_install_path):
            os.makedirs(driver_install_path)
            while not os.path.exists(driver_install_path):
                continue
        chromedriver_autoinstaller.install(False, driver_install_path)
    return driver_path
