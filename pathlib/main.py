from pathlib import Path
from os import chdir

def main()-> None:
    print(f"Current working directory: {Path.cwd()}")
    print(f"Home directory: {Path.home()}")
    
    path = Path("/home") / "tajpouria" / "pro"
    print(f"Does path {path} exists? {path.exists()}")

    settings_path = Path.cwd() / "settings.yaml"
    print(settings_path.read_text())


    settings_path = Path("settings.yaml")
    print(f"Resolved path: {settings_path.resolve()}")


    full_path = settings_path.resolve()
    print(f"Grand parent path of the {full_path.name}: {full_path.parent.parent}")
    print(f"Stem: {full_path.stem} Suffix: {full_path.suffix}")
    print(f"Is directory: {full_path.is_dir()} Is file: {full_path.is_file()}")

    new_file = Path("new_file.txt")
    if new_file.exists():
        new_file.unlink()
        print(f"{new_file} deleted!")
    new_file.write_text("Hello!")
    print(new_file.read_text())

    new_dir = Path("new_dir")
    if new_dir.exists():
        new_dir.rmdir()
    new_dir.mkdir()
    chdir(new_dir)
    print(f"Temporary current working directory: {Path.cwd()}")
    chdir(new_dir.parent)

if __name__ == "__main__":
    main()

