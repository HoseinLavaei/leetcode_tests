import sys
import pytest


def main():
    """Run pytest on the entire test suite."""
    # You can customize which directories to test
    test_paths = ["hosein", "amir"]  # or just ["."] for everything

    # Run pytest with verbose output and stop on first failure (optional)
    exit_code = pytest.main(
        test_paths + [
            "-v",  # verbose output
            "--tb=short",  # shorter traceback format
            "-x",  # exit instantly on first failure (remove if you want all tests)
        ]
    )

    # Return the same exit code as pytest (0 = all passed, >0 = failures)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()