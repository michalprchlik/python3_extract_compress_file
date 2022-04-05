"""Utility functions"""

import os
import zipfile
import tarfile
import logging

def extract_file(directory_or_file):
	"""Recursive function. It extracts all compressed files as a new directories"""

	extract_dir = ''
	base_dir = ''

	if os.path.isfile(directory_or_file):
		if directory_or_file.endswith('.zip'):
			extract_dir = os.path.basename(directory_or_file).replace('.', '_') + '/'
			base_dir = os.path.dirname(directory_or_file) + '/'
			try:
				with zipfile.ZipFile(directory_or_file, 'r') as zip_ref:
					zip_ref.extractall(base_dir + extract_dir)
			except Exception as exc: # pylint: disable=broad-except
				logging.error(f"{exc} ({extract_dir})")
			extract_file(base_dir + extract_dir)
			os.remove(directory_or_file)

		elif directory_or_file.endswith('.tar.gz'):
			extract_dir = os.path.basename(directory_or_file).replace('.', '_') + '/'
			base_dir = os.path.dirname(directory_or_file) + '/'
			try:
				with tarfile.open(directory_or_file, "r:gz") as tar_ref:
					tar_ref.extractall(base_dir + extract_dir)
			except Exception as exc: # pylint: disable=broad-except
				logging.error(f"{exc} ({extract_dir})")
			extract_file(base_dir + extract_dir)
			os.remove(directory_or_file)

		elif directory_or_file.endswith('.tar'):
			extract_dir = os.path.basename(directory_or_file).replace('.', '_') + '/'
			base_dir = os.path.dirname(directory_or_file) + '/'
			try:
				with tarfile.open(directory_or_file, "r:") as tar_ref:
					tar_ref.extractall(base_dir + extract_dir)
			except Exception as exc: # pylint: disable=broad-except
				logging.error(f"{exc} ({extract_dir})")
			extract_file(base_dir + extract_dir)
			os.remove(directory_or_file)

	elif os.path.isdir(directory_or_file):
		for directory_or_file1 in os.listdir(directory_or_file):
			extract_file(directory_or_file + '/' + directory_or_file1)
	else:
		logging.info(f'{directory_or_file} is not a directory, not a file')

	return base_dir + extract_dir
