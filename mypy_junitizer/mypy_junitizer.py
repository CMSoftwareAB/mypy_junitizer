import argparse
import fileinput
import re
from typing import List

from junit_xml import TestSuite, TestCase


RESULT_REGEX = re.compile(
    # errors -> error if found only one error
    r"Found (?P<count>\d+) errors?"
)


def process_lines(lines: List[str]) -> None:
    failures = []
    test_cases = []

    for line in lines:
        if line.startswith("Found "):
            match = re.match(RESULT_REGEX, line)
            if match:
                result = match.groupdict()
            continue

        # example: Success: no issues found in 9 source files
        if line.startswith("Success: no issues found in "):
            tc = TestCase(f'no err', f'no err', 0)
            test_cases.append(tc)
            break
        try:
            file_, line, type_, *message = line.split(":")
        except ValueError:
            print(line)
            return None
        type_ = type_.strip()

        if type_ == "error":
            failures.append((file_, line, type_, message))

    for failure in failures:
        msg = f"{failure[0]}:{failure[1]}: {failure[2]}: "
        msg += ":".join(failure[3]).strip()
        tc = TestCase(f'{failure[0]}:{failure[1]}', f'{failure[0]}', 0)
        tc.add_failure_info(f'Mypy error on {failure[0]}:{failure[1]}', {msg}, "Warning")
        test_cases.append(tc)
    ts = TestSuite("MyPy test suite", test_cases)
    print(TestSuite.to_xml_string([ts]))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("files", metavar="FILE", nargs="*", help="files to read, if empty, stdin is used")
    parser.add_argument("--output", type=str, dest="output", help="Filename to output to")
    parser.add_argument("--tee", action="store_true")

    args = parser.parse_args()
    if args.tee and not args.output:
        print("You must specify --output if using --tee")
        return -1

    process_lines(list(fileinput.input(files=args.files if len(args.files) > 0 else ("-",))))


if __name__ == "__main__":
    main()
