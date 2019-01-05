import os, argparse
import send2trash

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Help with remuxing files using OBS by cleaning up already remuxed .mkv files.')
    parser.add_argument('target dir', type=str, help='the directory containing your .mkv files')
    parser.add_argument('-sd', '--straight_delete', dest="straight_delete" , help="add this flag if you want to directly delete files instead of moving them to trash", action="store_true" ,required=False)

    args = parser.parse_args()
    os.chdir(vars(args)["target dir"])
    filex = None

    straight_delete: bool = vars(args)["straight_delete"]

    files_removed = 0
    file: str
    for file in os.listdir():
        if file.endswith(".mkv") and file.split('.')[0]+".mp4" in os.listdir():
            print("Removing "+file)
            # if straight_delete:      <-- I commented it out because it didn't work, lol.
            if True:
                os.remove(file)
            else:
                send2trash.send2trash(file, )
            files_removed +=1

    print("Done.", end=' ')
    if files_removed == 0:
        print("No files were ", end='')
    else:
        print(str(files_removed) + " files were", end=' ')
    if straight_delete:
        print("deleted.")
    else:
        print("moved to trash.")