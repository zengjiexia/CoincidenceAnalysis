import os
import subprocess
import pandas as pd
import re
from tqdm import tqdm

def map_dict(data_path, result_path):
	"""
	Walk through the root and map all the folders, then create the same structure at the result path
	para: path - string
	return: none
	"""
	paths = []
	for root, dirs, files in os.walk(data_path):
		for d in dirs:
			paths.append(os.path.join(root, d))
	for p in paths:
		p = p.replace(data_path, result_path)
		if os.path.isdir(p) == 0:
			os.mkdir(p)
	return paths


def select_sample_folder(paths):
	"""
	Filter the paths by checking if there is images in the folder
	"""
	valid_paths = []
	for p in paths:
		if os.path.isfile(p+ '/X0Y0R1W1C0_6E10.tif'): #improve condition
			valid_paths.append(p)
	return valid_paths


def ijCalc(fiji_path, data_path, result_path):
	code_path = os.path.dirname(os.path.abspath(__file__))

	try:
		subprocess.call([fiji_path, "--ij2", "--console", "--run", code_path + "\\fiji_macro.py", 'datapath=\''+data_path+'\','+'resultpath=\''+result_path+'\''])
		print('Calculation completed without error.')
	except FileNotFoundError:
		print('Fiji path is incorrect.')


if __name__ == '__main__':

	data_path = '' # parameter

	result_path = data_path + '_results'
	if os.path.isdir(result_path) == 0:
		os.mkdir(result_path)

	fiji_path = r"D:\Fiji.app\ImageJ-win64.exe" # parameter

	paths = map_dict(data_path, result_path)
	paths = select_sample_folder(paths)
	for p in tqdm(paths):
		print('processing: ' + p)
		ijCalc(fiji_path, p, p.replace(data_path, result_path))
	print('Calculation completed.')