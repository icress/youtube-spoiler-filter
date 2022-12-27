from UI import UserInterface
from youtube_driver import WebDriver
from threading import Thread

user_interface = UserInterface()
search_this, exclude_this = user_interface.start_window()

youtube_driver = WebDriver(search_for=search_this, exclude_this=exclude_this)
youtube_driver.open_youtube()

if __name__ == '__main__':
    Thread(target=user_interface.curtain).start()
    Thread(target=youtube_driver.search_youtube).start()
