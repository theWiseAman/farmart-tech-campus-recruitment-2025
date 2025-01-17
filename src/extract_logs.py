import os
import sys

def extract_logs_by_date(file_path, target_date, output_dir="output"):
    """
    Extracts all logs for a specific date from a large log file and writes them to an output file.

    Args:
        file_path (str): Path to the log file.
        target_date (str): The date (YYYY-MM-DD) for which to extract logs.
        output_dir (str): Directory where the output file will be saved.
    """
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Construct the output file path
    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    try:
        with open(file_path, "r") as input_file, open(output_file, "w") as outfile:
            for line in input_file:
                # Check if the line starts with the target date
                if line.startswith(target_date):
                    outfile.write(line)

        print(f"Logs for {target_date} have been written to {output_file}.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except PermissionError:
        print(f"Error: Permission denied while accessing '{file_path}' or '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Validate command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python src/extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)

    log_file_path = 'test_logs.log'
    date_to_extract = sys.argv[1]

    # Run the extraction function
    extract_logs_by_date(log_file_path, date_to_extract)
