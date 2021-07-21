from distutils.core import setup
import py2exe

setup(
    console=[
        {
            "script": 'Simple_Backup.py',
            "icon_resources": [(0, "icon.ico")]
        }
    ],
)
