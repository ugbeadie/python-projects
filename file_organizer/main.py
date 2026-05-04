import os
import shutil
def organize(path: str) -> None:
    if not os.path.isdir(path):
        print(f"Not a directory: {path}")
        return

    moved = 0

    for file in os.listdir(path):
        full_path = os.path.join(path, file)

        # touch actual files and ignore existing folders
        if not os.path.isfile(full_path):
            continue

        _, extension = os.path.splitext(file)
        extension = extension[1:].lower()

        if not extension:
            continue 

        extension_folder = os.path.join(path, extension)
        os.makedirs(extension_folder, exist_ok=True)

        shutil.move(full_path, os.path.join(extension_folder, file))
        moved += 1

    print(f"\nDone. Organized {moved} file(s).")


def undo(path: str) -> None:
    if not os.path.isdir(path):
        print(f"Not a directory: {path}")
        return

    moved = 0
    skipped = 0

    for entry in os.listdir(path):
        subfolder = os.path.join(path, entry)
        if not os.path.isdir(subfolder):
            continue

        for file in os.listdir(subfolder):
            src = os.path.join(subfolder, file)
            dst = os.path.join(path, file)

            # Prevent overwrite for a file that already exists in the parent
            if os.path.exists(dst):
                print(f"Skipped (already exists in parent): {file}")
                skipped += 1
                continue

            shutil.move(src, dst)
            moved += 1

        # Remove the subfolder if it's now empty
        try:
            os.rmdir(subfolder)
        except OSError:
            print(f"Folder not empty, left in place: {subfolder}")

    print(f"\nDone. Moved {moved} file(s). Skipped {skipped}.")


if __name__ == "__main__":
    print("1. Organize files into folders by extension")
    print("2. Undo (flatten everything back)")
    choice = input("Choose 1 or 2: ").strip()

    path = input("Enter the directory path: ").strip()

    if choice == "1":
        organize(path)
    elif choice == "2":
        undo(path)
    else:
        print("Invalid choice.")