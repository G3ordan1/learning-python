import pathlib

def rename_files():
    path = pathlib.Path(".")

    for folder in path.iterdir():
        if folder.is_dir():
            counter = 1
            for file in folder.iterdir():
                if file.is_file():
                    new_file = folder.name + str(counter) + file.suffix
                    file.rename(path / folder.name / new_file)
                    counter += 1
def prepend_number():
    path = pathlib.Path(".")

    counter = 1
    for file in path.iterdir():
        if file.name != "rename.py":
            if file.is_file():
                new_file =f"{counter}. {file.name}"
                file.rename(path / new_file)
                counter += 1

def remove_suffix():
    path = pathlib.Path(".")

    for file in path.iterdir():
        if file.name != "rename.py":
            if file.is_file():
                new_name = file.name[:-4]
                file.rename(path / new_name)

