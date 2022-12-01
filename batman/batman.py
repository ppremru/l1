""" MVP """

import csv


from .miro import Miro
from .tackle import Tackle


class Batman:
    """here"""

    input_file = None
    output_file = None

    @staticmethod
    def usage():
        """sanity check"""
        print("hello, let's tackle that bat!!!!!")
        print(f"Default input  file name {Miro.FILENAME}")
        print(f"Default output file name {Tackle.FILENAME}")

    @staticmethod
    def open_input(file_name):
        """open file for input"""
        try:
            return open(file_name, "r", encoding="utf-8")
        except OSError as ex:
            raise ValueError(f"Could not open input file [{file_name}]") from ex

    @staticmethod
    def open_output(file_name):
        """open file for output"""
        try:
            return open(file_name, "w", encoding="utf-8")
        except OSError as ex:
            raise ValueError(f"Could not open output file [{file_name}]") from ex

    def __init__(self, input_file_name, output_file_name):
        self.input_file = Batman.open_input(input_file_name)
        self.output_file = Batman.open_output(output_file_name)

    def __del__(self):
        """mission complete"""
        if self.input_file:
            self.input_file.close()
        if self.output_file:
            self.output_file.close()

    def convert(self):
        """Traverse and format the data"""
        bat_cols = []

        with self.input_file as bat, self.output_file as tackle:
            # setup output file columns
            writer = csv.writer(tackle, quoting=csv.QUOTE_ALL)
            writer.writerow(Tackle.COLUMNS)

            # strip ugly stuff at beginning of file and get header ???
            cvsreader = csv.reader(bat)
            next(cvsreader)
            bat_cols = next(cvsreader)
            print(f"COLUMNS: {bat_cols}")

            for index, row in enumerate(cvsreader):
                print(f"ROW {index}  : {row}")
                tackle_comment = ""
                for key, value in Tackle.COMMENT_MIRO_COLUMNS.items():
                    clean = row[value].replace("\n", " ")
                    tackle_comment += f"{key}: {clean} "
                print(tackle_comment)
                # TODO: Map by names not position
                output = [""] * len(Tackle.COLUMNS)
                output[0] = 1
                output[1] = row[Tackle.APPLICATION].replace("\n", " ")
                output[2] = row[Tackle.DESCRIPTION].replace("\n", " ")
                output[3] = tackle_comment
                output[4] = "Standard"
                writer.writerow(output)

            print(f"Total lines processed: {cvsreader.line_num}")
