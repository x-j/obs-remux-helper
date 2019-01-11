This is a tool I made for myself for cleaning up my OBS recordings folder.
For each MP4 video file in the given folder it checks if there is a MKV file with the same filename, and deletes the MKV file.
Also deletes SFK and SFL files for some reason.

## Usage
Pass the directory as a command line parameter.
Optional parameter -skipSFK can be added if you don't want to have your SFK and SFL files deleted. Default behaviour is: purging SFK and SFL files
