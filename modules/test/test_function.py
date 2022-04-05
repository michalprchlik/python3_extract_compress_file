"""Tests for module.utils"""

import unittest
import os

from modules.function import extract_file
from modules.test.files import create_zip_file, create_tar_gz_file, create_tar_file
from modules.test.files import create_zip_tar_gz_file, create_tar_gz_zip_file, create_zip_zip_zip_zip_file

if os.environ.get('TEST_IN_CONTAINER') == 'True':
	IS_LOCALHOST = False
else:
	IS_LOCALHOST = True

container_test = unittest.skipIf(
	IS_LOCALHOST,
	'Tests are skipped, because environment is not containerized'
)


@container_test
class TestExtractFile(unittest.TestCase):
	"""Tests for extract_file function"""

	def test_zip_file(self):
		"""Test for zip file"""

		archive = create_zip_file('/tmp/')
		self.assertEqual(archive, '/tmp/compressed.zip')

		directory = extract_file(archive)
		self.assertEqual(directory, '/tmp/compressed_zip/')

		result = os.path.isdir(directory)
		self.assertEqual(result, True)

		result = os.path.isfile(directory + '/filename.txt')
		self.assertEqual(result, True)

	def test_tar_gz_file(self):
		"""Test for tar.gz file"""

		archive = create_tar_gz_file('/tmp/')
		self.assertEqual(archive, '/tmp/compressed.tar.gz')

		directory = extract_file(archive)
		self.assertEqual(directory, '/tmp/compressed_tar_gz/')

		result = os.path.isdir(directory)
		self.assertEqual(result, True)

		result = os.path.isfile(directory + '/filename.txt')
		self.assertEqual(result, True)

	def test_tar_file(self):
		"""Test for tar file"""

		archive = create_tar_file('/tmp/')
		self.assertEqual(archive, '/tmp/compressed.tar')

		directory = extract_file(archive)
		self.assertEqual(directory, '/tmp/compressed_tar/')

		result = os.path.isdir(directory)
		self.assertEqual(result, True)

		result = os.path.isfile(directory + '/filename.txt')
		self.assertEqual(result, True)

	def test_zip_tar_gz_file(self):
		"""Test for zip + tar.gz file"""

		archive = create_zip_tar_gz_file('/tmp/')
		self.assertEqual(archive, '/tmp/compressed.zip')

		directory = extract_file(archive)
		self.assertEqual(directory, '/tmp/compressed_zip/')

		result = os.path.isdir(directory)
		self.assertEqual(result, True)

		directory = f"{directory}compressed_tar_gz/"
		result = os.path.isdir(directory)
		self.assertEqual(result, True)

		result = os.path.isfile(directory + 'filename.txt')
		self.assertEqual(result, True)

	def test_tar_gz_zip_file(self):
		"""Test for tar.gz + zip file"""

		archive = create_tar_gz_zip_file('/tmp/')
		self.assertEqual(archive, '/tmp/compressed.tar.gz')

		directory = extract_file(archive)
		self.assertEqual(directory, '/tmp/compressed_tar_gz/')

		result = os.path.isdir(directory)
		self.assertEqual(result, True)

		directory = f"{directory}compressed_zip/"
		result = os.path.isdir(directory)
		self.assertEqual(result, True)

		result = os.path.isfile(directory + 'filename.txt')
		self.assertEqual(result, True)

	def test_zip_zip_zip_zip_file(self):
		"""Test for zip + zip + zip + zip file"""

		archive = create_zip_zip_zip_zip_file('/tmp/')
		self.assertEqual(archive, '/tmp/compressed4.zip')

		directory = extract_file(archive)
		self.assertEqual(directory, '/tmp/compressed4_zip/')

		result = os.path.isdir(directory)
		self.assertEqual(result, True)

		directory = f"{directory}compressed3_zip/"
		result = os.path.isdir(directory)
		self.assertEqual(result, True)

		directory = f"{directory}compressed2_zip/"
		result = os.path.isdir(directory)
		self.assertEqual(result, True)

		directory = f"{directory}compressed1_zip/"
		result = os.path.isdir(directory)
		self.assertEqual(result, True)

		result = os.path.isfile(directory + 'filename.txt')
		self.assertEqual(result, True)
		