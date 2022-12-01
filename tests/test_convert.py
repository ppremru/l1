"""MVP """
import shutil
import tempfile
from os import path
import unittest

from src.convert_bat_to_tackle import Convert


class TestConvert(unittest.TestCase):
    """start here"""

    tackle_string = "Record Type 1,Application Name,Description,Comments,Business Service,Dependency,Dependency Direction,Binary Group,Binary Artifact,Binary Version,Binary Packaging,Repository Type,Repository URL,Repository Branch,Repository Path,Tag Type 1,Tag 1,Tag Type 2,Tag 2,Tag Type 3,Tag 3,Tag Type 4,Tag 4,Tag Type 5,Tag 5,Tag Type 6,Tag 6,Tag Type 7,Tag 7,Tag Type 8,Tag 8,Tag Type 9,Tag 9,Tag Type 10,Tag 10,Tag Type 11,Tag 11,Tag Type 12,Tag 12,Tag Type 13,Tag 13,Tag Type 14,Tag 14,Tag Type 15,Tag 15,Tag Type 16,Tag 16,Tag Type 17,Tag 17,Tag Type 18,Tag 18,Tag Type 19,Tag 19,Tag Type 20,Tag 20"
    bat_string = '"one","two","three","four","five","six","seven","eight","nine","ten"'

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        # TODO
        # create fake output
        temp = open(path.join(self.test_dir, "out.csv"), "w")
        temp.write(self.tackle_string)
        temp.write("\n")
        temp.close()
        # create fake input
        temp = open(path.join(self.test_dir, "in.csv"), "w")
        temp.write(self.bat_string)
        temp.write("\n")
        temp.write(self.bat_string)
        temp.write("\n")
        temp.write(self.bat_string)
        temp.write("\n")
        temp.close()

    def tearDown(self):
        # Remove the directory after the test
        shutil.rmtree(self.test_dir)

    def test_open_input_fail(self):
        """easy stuff"""
        try:
            Convert.open_input(self, "nofileexists")
        except ValueError as ex:
            self.assertEqual("Could not open input file [nofileexists]", str(ex))
        else:
            self.fail("ValueError not raised")

    def test_open_input_success(self):
        """easy stuff"""
        try:
            # Create a file in the temporary directory
            fname = self.test_dir + "/test.txt"
            fn = open(path.join(self.test_dir, "test.txt"), "w")
            fn.write("Hello Dolly")
            Convert.open_input(self, fname)
        except ValueError as ex:
            self.fail(str(ex))
        else:
            self.assertTrue(True)

    def test_open_output_fail(self):
        """easy stuff"""
        try:
            Convert.open_output(self, "/no/fakefile")
        except ValueError as ex:
            self.assertEqual("Could not open output file [/no/fakefile]", str(ex))
        else:
            self.fail("ValueError not raised")

    def test_open_output_success(self):
        """easy stuff"""
        try:
            Convert.open_output(self, "fakefile")
        except ValueError as ex:
            self.fail(str(ex))
        else:
            self.assertTrue(True)

    def test_convert_nada(self):
        """easy stuff"""
        fin = self.test_dir + "/in.csv"
        fout = self.test_dir + "/two"
        try:
            # Create a file in the temporary directory
            cv = Convert(fin, fout)
            cv.convert()
        except ValueError as ex:
            self.fail(str(ex))
        else:
            # so much to do here
            # self.assertListEqual(list(io.open(ftst)), list(io.open(fout)))
            self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
