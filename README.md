# PyLogCheck

A beginner-friendly Python project that analyzes a sample server log and counts `INFO`, `WARNING`, and `ERROR` messages.

## Why this project?

DevOps engineers use logs to investigate problems and understand what applications are doing. PyLogCheck demonstrates a small, simple version of log analysis.

## Features

- Reads a text log file
- Counts INFO, WARNING, and ERROR entries
- Prints a simple summary
- Uses only Python's standard library

## Requirements

- Python 3

No extra packages are required.

## How to run

1. Download or clone this repository.
2. Keep `main.py` and `sample.log` in the same folder.
3. Open a terminal in that folder.
4. Run:

   ```bash
   python main.py
   ```

   If your computer uses the `python3` command, run `python3 main.py` instead.

## Example output

```text
===== PyLogCheck Report =====

INFO: 2
WARNING: 1
ERROR: 2

Total log entries: 5
```

## Project files

- `main.py` — reads the log and creates the report
- `sample.log` — example log entries for testing

## Concepts learned

- Reading files
- Loops and conditions
- Dictionaries
- Functions
- Basic error handling

## Limitations

This is a learning project. It analyzes the provided text log and is not a real-time server monitor.

## Future improvements

- Let users choose a log file
- Show the most common error messages
- Add automated tests
- Add a GitHub Actions workflow

## License

This project is shared under the MIT License. See `LICENSE`.
