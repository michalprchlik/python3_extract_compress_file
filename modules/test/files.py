"""Module for example compressed files used in tests"""

import os
import shutil
import tarfile


def create_zip_file(directory):
	"""Create zip file used in tests"""

	directory = directory.rstrip('/')

	work_dir = "/tmp/work"
	os.makedirs(work_dir, exist_ok=True)

	with open(f"{work_dir}/filename.txt", mode="w+", encoding="utf-8") as file:
		file.write("data")
	filename = shutil.make_archive(f"{directory}/compressed", 'zip', work_dir)

	shutil.rmtree(work_dir)

	return filename


def create_tar_gz_file(directory):
	"""Create tar.gz file used in tests"""

	directory = directory.rstrip('/')

	work_dir = "/tmp/work"
	os.makedirs(work_dir, exist_ok=True)

	with open(f"{work_dir}/filename.txt", mode="w+", encoding="utf-8") as file:
		file.write("data")

	filename = f"{directory}/compressed.tar.gz"
	with tarfile.open(filename, "w:gz") as tar_ref:
		tar_ref.add(work_dir, arcname = './')

	shutil.rmtree(work_dir)
	return filename


def create_tar_file(directory):
	"""Create tar file used in tests"""

	directory = directory.rstrip('/')

	work_dir = "/tmp/work"
	os.makedirs(work_dir, exist_ok=True)

	with open(f"{work_dir}/filename.txt", mode="w+", encoding="utf-8") as file:
		file.write("data")

	filename = f"{directory}/compressed.tar"
	with tarfile.open(filename, "w:") as tar_ref:
		tar_ref.add(work_dir, arcname = './')

	shutil.rmtree(work_dir)
	return filename


def create_zip_tar_gz_file(directory):
	"""Create zip + tar.gz file used in tests"""

	directory = directory.rstrip('/')

	work_dir = "/tmp/work"
	os.makedirs(work_dir, exist_ok=True)
	work_dir1 = "/tmp/work1"
	os.makedirs(work_dir1, exist_ok=True)

	with open(f"{work_dir}/filename.txt", mode="w+", encoding="utf-8") as file:
		file.write("data")

	filename = f"{work_dir1}/compressed.tar.gz"
	with tarfile.open(filename, "w:gz") as tar_ref:
		tar_ref.add(work_dir, arcname = './')

	filename = shutil.make_archive(f"{directory}/compressed", 'zip', work_dir1)

	shutil.rmtree(work_dir)
	shutil.rmtree(work_dir1)

	return filename


def create_tar_gz_zip_file(directory):
	"""Create tar.gz + zip file used in tests"""

	directory = directory.rstrip('/')

	work_dir = "/tmp/work"
	os.makedirs(work_dir, exist_ok=True)

	with open(f"{work_dir}/filename.txt", mode="w+", encoding="utf-8") as file:
		file.write("data")

	filename = shutil.make_archive(f"{work_dir}/compressed", 'zip', work_dir)

	filename = f"{directory}/compressed.tar.gz"
	with tarfile.open(filename, "w:gz") as tar_ref:
		tar_ref.add(work_dir, arcname = './')

	shutil.rmtree(work_dir)

	return filename


def create_zip_zip_zip_zip_file(directory):
	"""Create zip + zip + zip + zip file used in tests"""

	directory = directory.rstrip('/')

	work_dir = "/tmp/work"
	os.makedirs(work_dir, exist_ok=True)
	work_dir1 = "/tmp/work1"
	os.makedirs(work_dir1, exist_ok=True)
	work_dir2 = "/tmp/work2"
	os.makedirs(work_dir2, exist_ok=True)
	work_dir3 = "/tmp/work3"
	os.makedirs(work_dir3, exist_ok=True)

	with open(f"{work_dir}/filename.txt", mode="w+", encoding="utf-8") as file:
		file.write("data")

	shutil.make_archive(f"{work_dir1}/compressed1", 'zip', work_dir)
	shutil.make_archive(f"{work_dir2}/compressed2", 'zip', work_dir1)
	shutil.make_archive(f"{work_dir3}/compressed3", 'zip', work_dir2)
	filename = shutil.make_archive(f"{directory}/compressed4", 'zip', work_dir3)

	shutil.rmtree(work_dir)
	shutil.rmtree(work_dir1)
	shutil.rmtree(work_dir2)
	shutil.rmtree(work_dir3)

	return filename
