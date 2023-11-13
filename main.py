import argparse
import os
import shutil
import re


def move(source_path, dest_path, is_verbose, is_dry_run, is_move, verbose_prefix):
    if is_verbose or is_dry_run:
        print(f"{verbose_prefix} From:", source_path)
        print(f"{verbose_prefix} To:  ", dest_path)
    if not is_dry_run:
        if is_move:
            shutil.move(source_path, dest_path)
        else:
            shutil.copy(source_path, dest_path)


def main():
    parser = argparse.ArgumentParser(
        prog='File Resequencer',
        description='Combines numberings of two sets of pictures in different folders. Files are copied by default.',
        epilog='By Eric C. https://github.com/ricetech'
    )
    parser.add_argument('folder_1', nargs=1,
                        help='first folder, keeps its numbering')
    parser.add_argument('folder_2', nargs=1,
                        help='second folder, re-numbered to follow after the last number in folder 1')
    parser.add_argument('output_folder', nargs=1,
                        help='destination folder for files from both folders')
    parser.add_argument('-m', '--move', dest='move', action='store_true',
                        help='move the files instead of copying them')
    parser.add_argument('-v', '--verbose', dest='verbose', action='store_true',
                        help='print original and new paths for each file')
    parser.add_argument('-d', '--dry-run', dest='dry_run', action='store_true',
                        help='shows the result of what would happen without moving/copying any files')

    args = parser.parse_args()

    folder_1 = args.folder_1[0]
    folder_2 = args.folder_2[0]
    output_folder = args.output_folder[0]

    while True:
        try:
            if len(os.listdir(output_folder)) == 0:
                break
            else:
                input(">> ERROR: Output Directory must be empty: " + output_folder +
                      "\nPress Enter once the folder is empty.")
        except FileNotFoundError:
            os.makedirs(output_folder)  # Create output folder if it doesn't exist

    folder_1_files = sorted(os.listdir(folder_1))
    folder_2_files = sorted(os.listdir(folder_2))

    # Get last number of folder 1
    last_num = int(re.search(r"(\d+)\.[a-zA-Z]+$", folder_1_files[(len(folder_1_files) - 1)]).group(1))

    # Copy or move folder 1 to output folder
    for file in folder_1_files:
        source_path = os.path.join(folder_1, file)
        dest_path = os.path.join(output_folder, file)
        move(source_path=source_path, dest_path=dest_path, is_verbose=args.verbose, is_dry_run=args.dry_run,
             is_move=args.move, verbose_prefix='[FOLDER 1]')

    # Copy or move folder 2 to output folder with numbering offset
    for file in folder_2_files:
        split_filename = re.split(r"(\d+)\.([a-zA-Z]+)$", file)
        # Original file number
        file_num = int(split_filename[1])
        # Length of original number section (to add padding zeroes later)
        num_section_len = len(split_filename[1])
        # Avoid duplicate filename if numbering starts from 0
        if file_num == 0:
            last_num += 1
        new_num = last_num + file_num
        # Re-combine filename, add zeroes for padding to match original length
        new_file = (split_filename[0] + ('0' * (num_section_len - len(str(new_num)))) + str(new_num) + '.'
                    + split_filename[2])
        source_path = os.path.join(folder_2, file)
        dest_path = os.path.join(output_folder, new_file)
        move(source_path=source_path, dest_path=dest_path, is_verbose=args.verbose, is_dry_run=args.dry_run,
             is_move=args.move, verbose_prefix='[FOLDER 2]')


if __name__ == '__main__':
    main()

