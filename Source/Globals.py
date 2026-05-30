from datetime import datetime
from enum import Enum

# GUI
DEFAULT_WINDOW_HEIGHT		= 600
DEFAULT_WINDOW_WIDTH		= 800
WINDOW_TITLE 				= "HTML Reader"

# MISCELLANEOUS
EMPTY_STRING = ""

# TODO: Add 'Source' enum

def LOG(text):
	print(f"LOG [{datetime.now()}]: {text}")

def ERROR(text):
	print(f"ERROR [{datetime.now()}]: {text}")

def ERROR_IF(condition, text):
	if condition:
		print(f"ERROR [{datetime.now()}]: {text}")

def WARNING(text):
	print(f"WARNING [{datetime.now()}]: {text}")

def WARNING_IF(condition, text):
	if condition:
		print(f"WARNING [{datetime.now()}]: {text}")