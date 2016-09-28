#setup.py
from distutils.core import setup
import py2exe

setup(
	console=['tictoc.py'],
	options = {
		'py2exe':{
			'packages' : ['pygame']
		}
	}
)