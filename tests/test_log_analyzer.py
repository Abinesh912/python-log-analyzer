
import tempfile
import unittest
from pathlib import Path

from log_analyzer import analyze_log, generate_report


class TestLogAnalyzer(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.test_dir = Path(self.temp_dir.name)
        self.log_file = self.test_dir / "test.log"

        self.log_file.write_text(
            "2026-10-19 09:00:00 INFO Application started\n"
            "2026-10-19 09:01:00 WARNING High memory usage\n"
            "2026-10-19 09:02:00 ERROR Database failed\n"
            "2026-10-19 09:03:00 ERROR Database failed\n",
            encoding="utf-8",
        )

    def test_counts_log_levels(self):
        result = analyze_log(self.log_file)

        self.assertEqual(result["total_lines"], 4)
        self.assertEqual(result["errors"], 2)
        self.assertEqual(result["warnings"], 1)
        self.assertEqual(result["info"], 1)

    def test_detects_repeated_errors(self):
        result = analyze_log(self.log_file)

        self.assertEqual(
            result["repeated_errors"]["Database failed"],
            2,
        )

    def test_filters_by_severity(self):
        result = analyze_log(self.log_file, severity="ERROR")

        self.assertEqual(len(result["filtered_lines"]), 2)
        self.assertTrue(
            all("ERROR" in line for line in result["filtered_lines"])
        )

    def test_missing_file(self):
        missing_file = self.test_dir / "missing.log"

        with self.assertRaises(FileNotFoundError):
            analyze_log(missing_file)

    def test_generates_report(self):
        result = analyze_log(self.log_file)
        report_path = self.test_dir / "reports" / "report.txt"

        generated_file = generate_report(result, report_path)
        report_content = generated_file.read_text(encoding="utf-8")

        self.assertTrue(generated_file.exists())
        self.assertIn("Errors: 2", report_content)
        self.assertIn("2 occurrences: Database failed", report_content)


if __name__ == "__main__":
    unittest.main()










# first code
# 
#  import tempfile
# import unittest
# from pathlib import Path

# from log_analyzer import analyze_log


# class TestLogAnalyzer(unittest.TestCase):

#     def test_counts_log_levels(self):
#         with tempfile.TemporaryDirectory() as temp_dir:
#             log_file = Path(temp_dir) / "test.log"
#             log_file.write_text(
#                 "INFO Application started\n"
#                 "WARNING High memory usage\n"
#                 "ERROR Database failed\n"
#                 "ERROR Request failed\n",
#                 encoding="utf-8",
#             )

#             result = analyze_log(log_file)

#             self.assertEqual(result["total_lines"], 4)
#             self.assertEqual(result["errors"], 2)
#             self.assertEqual(result["warnings"], 1)
#             self.assertEqual(result["info"], 1)

#     def test_missing_file(self):
#         with self.assertRaises(FileNotFoundError):
#             analyze_log("file_that_does_not_exist.log")


# if __name__ == "__main__":
#     unittest.main()