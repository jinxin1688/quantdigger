#!/usr/bin/env python

import dependency
import util
import os
import re

# install pip
print("----------- install pip --------------" )
result = os.popen('pip -V').read()
reobj = re.compile("pip.+from.+", re.IGNORECASE)
if reobj.search(result):
	print('pip has be installed')
else:
	print('pip no install')
	dependency.pip_download_install()

print("----------- install dpendencies --------------" )
dependency.handle_dependency()

# generate quantdigger
print("----------- generate QuantDigger --------------" )
result = os.popen('python setup.py bdist_wheel').readlines()
util.printCommandResult(result)

# install quantdigger
print("----------- install QuantDigger --------------" )
pattern = re.compile(r'QuantDigger-.*\.whl$', re.IGNORECASE)
for whl in os.listdir('dist'):
	match = pattern.match(whl)
	if match:
		result = os.popen('pip install ' + os.path.join('dist', whl)).readlines()
		util.printCommandResult(result)
		break
