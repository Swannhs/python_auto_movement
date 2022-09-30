from multiprocessing import Process
import keyboard

from mouse_mover import fiverr_auto_mouse_mover


def main():
    fiverr_auto_mouse_mover_thread = Process(target=fiverr_auto_mouse_mover)

    if __name__ == '__main__':
        print("-----------------------Press ctrl enter to start action---------------------")
        keyboard.wait('ctrl + enter')
        fiverr_auto_mouse_mover_thread.start()
        keyboard.wait('ctrl + q')
        fiverr_auto_mouse_mover_thread.terminate()
        main()


main()

