import os
import unittest
from pyaudioai.RecordQuestion import RecordQuestion

__author__ = "Manuel Eberle (info@manueleberle.de)"

class TestRecordQuestion(unittest.TestCase):

    def test_init(self):
        record_obj = RecordQuestion(5, "question.m4a")
        assert record_obj.recording_time == 5
        assert record_obj.audio_file == "question.m4a"

    def test_delete_file(self):
        mock_file_name = "test.txt"
        record_obj = RecordQuestion(5, mock_file_name)

        mock_file = open(mock_file_name, "w")
        mock_file.close()

        record_obj.delete_file()
        self.assertFalse(os.path.exists(mock_file_name))


if __name__ == '__main__':
    unittest.main()
