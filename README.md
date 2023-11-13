# File Resequencer

A quick-and-dirty tool for a rather specific problem.

Takes two folders containing pictures that follow a standard naming pattern
(for example, DSC00001.ARW) and combines them into 1 folder (copy by default, move by option)
but with the files from the second folder re-numbered to start from after the last file
from the first folder.

For example:
Last file of Folder 1: `DSC02599.jpg`
First file of Folder 2, originally: `DSC00001.jpg`
First file of Folder 2, modified: `DSC02600.jpg`

The script takes care of adding enough zeroes to maintain the format, too.

## Usage

```bash
python3 main.py [-h] [-m] [-v] [-d] folder1 folder2 outputfolder
```

### Positional arguments

| Argument        | Position | Description                                                            |
|-----------------|----------|------------------------------------------------------------------------|
| `folder_1`      | 1        | First folder, keeps its numbering                                      |
| `folder_2`      | 2        | Second folder, re-numbered to follow after the last number in folder 1 |
| `output_folder` | 3        | Destination folder for files from both folders                         |


### Switches

| Short | Long        | Description                                                            |
|-------|-------------|------------------------------------------------------------------------|
| `-h`  | `--help`    | Show the help message and exit                                         |
| `-m`  | `--move`    | Move the files instead of copying them                                 |
| `-v`  | `--verbose` | Print original and new paths for each file                             |
| `-d`  | `--dry-run` | Shows the result of what would happen without moving/copying any files |

