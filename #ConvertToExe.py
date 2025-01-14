#program:       ConvertToExe
#purpose:       is a game
#progamer:      Madison Arndt 10/26/2023

import PyInstaller.__main__
import os

_FP = os.path.dirname(os.path.abspath(__file__))


#old specs
try:
    os.remove(f"{_FP}/Main.spec")
except:
    print("failed run")


opt = [f'{_FP}/Main.py',
       '--noconsole',
       '--noconfirm',
       '--onefile',
       #icon
       #f"--add-data={_FP}/_Graphics/Game_icon.ico:_Graphics",
       #f'--icon={_FP}/_Graphics/Game_icon.ico'
       ]


#cleen app
opt.append("--clean")

#run app maker
PyInstaller.__main__.run(opt)





















