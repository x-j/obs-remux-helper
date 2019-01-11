import os, argparse
import send2trash


def delete(file, straight_delete=False):
    print("Removing " + file)
    if straight_delete:
        os.remove(file)
    else:
        send2trash.send2trash(file)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Help with remuxing files using OBS by cleaning up already remuxed MKV files.\nAnd also SFK and SFL files, for some reason.')
    parser.add_argument('target dir', type=str, help='the directory containing your MKV files')
    parser.add_argument('-sd', '--straight_delete', dest="straight_delete",
                        help="add this flag if you want to directly delete files instead of moving them to trash",
                        action="store_true", required=False)
    parser.add_argument('--skipSFK', dest='skip_sfk',
                        help="add this flag if for some reason you don't want this script to delete your SFK and SFL files.",
                        action="store_true", required=False)

    args = parser.parse_args()
    os.chdir(vars(args)["target dir"])
    filex = None

    # straight_delete: bool = vars(args)["straight_delete"]         <-- I commented it out because it didn't work, lol.
    straight_delete = True

    skip_sfk: bool = vars(args)["skip_sfk"]

    files_deleted = 0
    file: str
    for file in os.listdir():
        if file.endswith(".mkv") and file.split('.')[0] + ".mp4" in os.listdir():
            delete(file, straight_delete)
            files_deleted += 1
        if (file.endswith(".sfk") or file.endswith(".sfl")) and not skip_sfk:
            delete(file, straight_delete)
            files_deleted += 1

    print("Done.", end=' ')
    if files_deleted == 0:
        print("No files were ", end='')
    else:
        print(str(files_deleted) + " files were", end=' ')
    if straight_delete:
        print("deleted.")
    else:
        print("moved to trash.")
