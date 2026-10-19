from pathlib import Path
from collections import Counter


def analyze_log(file_path, severity=None):
    log_file = Path(file_path)

    if not log_file.is_file():
        raise FileNotFoundError(f"Log file not found: {file_path}")

    results = {
        "file_name": log_file.name,
        "total_lines": 0,
        "errors": 0,
        "warnings": 0,
        "info": 0,
        "repeated_errors": {},
        "filtered_lines": [],
    }

    error_messages = Counter()

    with log_file.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            results["total_lines"] += 1
            upper_line = line.upper()

            if "ERROR" in upper_line:
                results["errors"] += 1
                error_message = line.split("ERROR", 1)[1].strip()
                error_messages[error_message] += 1
                level = "ERROR"
            elif "WARNING" in upper_line:
                results["warnings"] += 1
                level = "WARNING"
            elif "INFO" in upper_line:
                results["info"] += 1
                level = "INFO"
            else:
                level = "OTHER"

            if severity is None or level == severity.upper():
                results["filtered_lines"].append(line)

    results["repeated_errors"] = {
        message: count
        for message, count in error_messages.items()
        if count > 1
    }

    return results


def generate_report(results, report_path):
    report_file = Path(report_path)
    report_file.parent.mkdir(parents=True, exist_ok=True)

    with report_file.open("w", encoding="utf-8") as file:
        file.write("===== LOG ANALYSIS REPORT =====\n")
        file.write(f"Log file: {results['file_name']}\n")
        file.write(f"Total lines: {results['total_lines']}\n")
        file.write(f"Errors: {results['errors']}\n")
        file.write(f"Warnings: {results['warnings']}\n")
        file.write(f"Info messages: {results['info']}\n")

        file.write("\n===== REPEATED ERRORS =====\n")

        if results["repeated_errors"]:
            for message, count in results["repeated_errors"].items():
                file.write(f"{count} occurrences: {message}\n")
        else:
            file.write("No repeated errors found.\n")

        file.write("\n===== FILTERED LOG ENTRIES =====\n")

        for line in results["filtered_lines"]:
            file.write(line + "\n")

        file.write("===============================\n")

    return report_file


def main():
    log_file = Path("sample_logs/application.log")

    try:
        results = analyze_log(log_file)
        report_file = generate_report(
            results,
            "reports/analysis_report.txt",
        )

        print("\n===== LOG ANALYSIS REPORT =====")
        print(f"Log file: {results['file_name']}")
        print(f"Total lines: {results['total_lines']}")
        print(f"Errors: {results['errors']}")
        print(f"Warnings: {results['warnings']}")
        print(f"Info messages: {results['info']}")

        print("\nRepeated errors:")
        if results["repeated_errors"]:
            for message, count in results["repeated_errors"].items():
                print(f"{count} occurrences: {message}")
        else:
            print("No repeated errors found.")

        print(f"\nReport saved to: {report_file}")

    except (FileNotFoundError, OSError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()





#second code

#  from pathlib import Path


# def analyze_log(file_path):
#     log_file = Path(file_path)

#     if not log_file.exists():
#         raise FileNotFoundError(f"Log file not found: {file_path}")

#     results = {
#         "total_lines": 0,
#         "errors": 0,
#         "warnings": 0,
#         "info": 0,
#     }

#     with log_file.open("r", encoding="utf-8") as file:
#         for line in file:
#             results["total_lines"] += 1
#             text = line.upper()

#             if "ERROR" in text:
#                 results["errors"] += 1
#             elif "WARNING" in text:
#                 results["warnings"] += 1
#             elif "INFO" in text:
#                 results["info"] += 1

#     return results


# def main():
#     file_path = "sample_logs/application.log"

#     try:
#         results = analyze_log(file_path)

#         print("\n===== LOG ANALYSIS REPORT =====")
#         print(f"Log file: {Path(file_path).name}")
#         print(f"Total lines: {results['total_lines']}")
#         print(f"Errors: {results['errors']}")
#         print(f"Warnings: {results['warnings']}")
#         print(f"Info messages: {results['info']}")
#         print("===============================\n")

#     except FileNotFoundError as error:
#         print(f"Error: {error}")


# if __name__ == "__main__":
#     main()



# first code
# from pathlib import Path

# def analyze_log(file_path):
#     log_file = Path(file_path)

#     if not log_file.exists():
#         print(f"Error: Log file not found: {file_path}")
#         return

#     total_lines = 0
#     errors = 0
#     warnings = 0
#     info = 0

#     with log_file.open("r", encoding="utf-8") as file:
#         for line in file:
#             total_lines += 1
#             text = line.upper()

#             if "ERROR" in text:
#                 errors += 1
#             elif "WARNING" in text:
#                 warnings += 1
#             elif "INFO" in text:
#                 info += 1

#     print("\n===== LOG ANALYSIS REPORT =====")
#     print(f"Log file: {log_file.name}")
#     print(f"Total lines: {total_lines}")
#     print(f"Errors: {errors}")
#     print(f"Warnings: {warnings}")
#     print(f"Info messages: {info}")
#     print("===============================\n")


# if __name__ == "__main__":
#     analyze_log("sample_logs/application.log")