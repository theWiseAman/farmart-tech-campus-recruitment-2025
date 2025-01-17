# Discussion.md

## Solutions Considered

### 1. **Loading the Entire File into Memory**
   - **Description**: This approach involved reading the entire log file into memory and filtering entries based on the given date.
   - **Advantages**:
     - Simplicity in implementation.
     - Suitable for small to medium-sized files.
   - **Disadvantages**:
     - Inefficient for a 1 TB file due to excessive memory usage.
     - High risk of crashing the system due to memory overflow.

### 2. **Line-by-Line Processing**
   - **Description**: This method processes the log file line by line, checking for entries that match the target date.
   - **Advantages**:
     - Optimized for large files.
     - Low memory footprint since only one line is loaded into memory at a time.
   - **Disadvantages**:
     - Slightly slower than loading the entire file but more scalable for large files.

### 3. **Indexing the Log File**
   - **Description**: Create an indexed structure (e.g., database or preprocessed index) to quickly retrieve logs for a specific date.
   - **Advantages**:
     - Fast lookups once indexing is complete.
   - **Disadvantages**:
     - Initial indexing would be resource-intensive for a 1 TB file.
     - Added complexity in maintaining and updating the index.

## Final Solution Summary

The chosen solution uses **Loading the Entire File into Memory** to extract logs for a specific date. This approach was selected because despite its inefficiency for very large files, primarily due to its simplicity and direct approach. While not optimal for handling files of 1 TB in size, this method is suitable for smaller log files and serves as a foundational approach. Future implementations can build on this by incorporating index of log files for faster processing and scalability.

## Steps to Run

1. **Download the Log File**:
   - Use the provided `curl` command to download the log file:

     ```bash
     curl -L -o test_logs.log "https://limewire.com/d/90794bb3-6831-4e02-8a59-ffc7f3b8b2a3#X1xnzrH5s4H_DKEkT_dfBuUT1mFKZuj4cFWNoMJGX98"
     ```

2. **Run the Script**:
   - Execute the script with the log file path `test_logs.log` located at the root of the project structure and the target date as arguments:

     ```bash
     python src/extract_logs.py 2024-12-01
     ```

3. **View Output**:
   - Extracted logs will be saved in the `output` directory with the filename `output_2024-12-01.txt`.

4. **Ensure Python Environment**:
   - Ensure Python 3.x is installed and available in your environment.
   - No external libraries are required as the solution uses Python's built-in functionalities.
