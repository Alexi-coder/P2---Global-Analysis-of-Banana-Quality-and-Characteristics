# Project 2, Group 5
# Interactive Terminal

# Imports
import os
import library, view, analysis


def main():
    # Process user input

    # Options
    # Select and read in the data file
    # View an individual entry
    # View a sorted or filtered set of data

    data_dir = "data"
    data = None
    source_file = None

    while True:
        # No data selected
        if not data:
            # List files from data directory
            data_files = os.listdir(data_dir)
            choice = view.present_options(data_files, "FILES")
            if choice == -1:
                continue

            # Verify file selected
            source_file = os.path.join(data_dir, data_files[choice])
            if not os.path.exists(source_file):
                print("Error: File not found.")
                continue
            if not source_file.endswith(".csv"):
                print("Error: File not valid.")
                continue

            # Read in data
            data = library.read_csv(source_file)

        # Options menu
        options = [
            f"Unload data: {source_file.split("\\")[1]}",
            "View individual entry",
            "View sorted entries",
            "View filtered entries",
            "Generate analysis report",
            "View report"
        ]
        choice = view.present_options(options, "OPTIONS")
        if choice == -1:
            continue

        # Execute option
        match choice:
            case 0:
                data = None  # unload source
                print("Unloaded source. Please select a new file.")
            case 1:
                view.show_entry(data)
            # TO-DO
            case 2:
                pass
            case 3:
                pass
            case 4:
                analysis.generate_analysis(data)
            case 5:
                analysis.display_report()
            case _:
                # default
                pass


if __name__ == "__main__":
    main()
