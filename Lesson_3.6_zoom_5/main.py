# import  services
# import ui.windows
# import ui.unix

from services import very_big_function
from ui import windows
from ui import unix


if __name__ == '__main__':
    result = very_big_function()
    print('result =', result)

    design = windows.get_windows_desing()
    print('design =', design)

    design = unix.get_unix_desing()
    print('design =', design)