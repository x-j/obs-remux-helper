import os, argparse
import send2trash


def delete(file, straight_delete=False):
    print("Removing " + file)
    if straight_delete:
        os.remove(file)
    else:
        send2trash.send2trash(file)


def run(target_dir: str, skip_sfk: bool, recurse: bool, global_filesdeleted: list):
    os.chdir(target_dir)

    local_filesdeleted = 0

    for file in os.listdir():
        if file.endswith(".mkv") and file.split('.')[0] + ".mp4" in os.listdir():
            delete(file, straight_delete)
            local_filesdeleted += 1
            global_filesdeleted.append(file)
        if (file.endswith(".sfk") or file.endswith(".sfl")) and not skip_sfk:
            delete(file, straight_delete)
            local_filesdeleted += 1
            global_filesdeleted.append(file)
        if (os.path.isdir(file)) and recurse:
            run(os.path.abspath(file), skip_sfk, recurse, global_filesdeleted)
            os.chdir(target_dir)

    if local_filesdeleted == 0:
        print("No files were ", end='')
    else:
        print(str(local_filesdeleted) + " files were", end=' ')
    if straight_delete:
        print("deleted", end=' ')
    else:
        print("moved to trash", end=' ')
    print(f"from folder {target_dir}")


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
    parser.add_argument('--recurse', dest='recurse',
                        help="add this flag to apply this script to all subdirectories of target dir",
                        action="store_true", required=False)

    args = parser.parse_args()
    filex = None

    straight_delete: bool = vars(args)["straight_delete"]         # <-- DANGEROUS CODE
    straight_delete = True

    target_dir: str = vars(args)["target dir"]
    skip_sfk: bool = vars(args)["skip_sfk"]
    recurse: bool = vars(args)["recurse"]

    files_deleted = []

    run(target_dir, skip_sfk, recurse, files_deleted)

    print("Done. In total,", end=' ')
    if len(files_deleted) == 0:
        print("no files were ", end='')
    else:
        print(f"{len(files_deleted)} files were", end=' ')
    if straight_delete:
        print("deleted.", end=' ')
    else:
        print("moved to trash.", end=' ')
