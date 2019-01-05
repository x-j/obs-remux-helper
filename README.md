This is a tool I made for myself for cleaning up my OBS recordings folder.
For each MP4 video file in the given folder it checks if there is a MKV file with the same filename, and deletes the MKV file.
Also deletes SFK files for some reason.

## Usage
Pass the directory as a command line parameter.
Optional parameter -skipSFK can be added if you don't want to have your SFK files deleted. Default behaviour is: purging SFK files
