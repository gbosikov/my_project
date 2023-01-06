# importing the required modules
import os
import shutil
import time
import datetime





# main function
def main():
    # initializing the count
    deleted_folders_count = 0
    deleted_files_count = 0

    # specify the path
    path = 'C:/Users/garry.bosikov/Desktop/New folder'

    # specify the days
    days = 0

    # converting days to seconds
    # time.time() returns current time in seconds
    seconds = time.time() - (days * 24 * 60 * 60)

    # checking whether the file is present in path or not
    if os.path.exists(path):

        # iterating over each and every folder and file in the path
        for files in os.listdir(path):

            file_path = os.path.join(path, files)

            # comparing the days
            if seconds >= get_file_or_folder_age(file_path) and files.find('.pdf') > 1:
                # invoking the remove_file function
                remove_file(file_path)

                # log(path)
                deleted_files_count += 1  # incrementing count

    else:

        # file/folder is not found
        print(f'"{path}" is not found')
        deleted_files_count += 1  # incrementing count

    print(f"Total folders deleted: {deleted_folders_count}")
    print(f"Total files deleted: {deleted_files_count}")


def remove_folder(path):
    # removing the folder
    if not shutil.rmtree(path):

        # success message
        print(f"{path} is removed successfully")

    else:

        # failure message
        print(f"Unable to delete the {path}")


def remove_file(path):
    # removing the file
    if not os.remove(path):
        log(path)
        # success message
        print(f"{path} is removed successfully")

    else:

        # failure message
        print(f"Unable to delete the {path}")


def get_file_or_folder_age(path):
    # getting ctime of the file/folder
    # time will be in seconds
    ctime = os.stat(path).st_ctime

    # returning the time
    return ctime


def log(path):
    hs = open("file_delete_log.txt", "a")
    hs.write(f'{path} | {datetime.date.today()}\n')
    hs.close()


if __name__ == '__main__':
    main()
    print()
