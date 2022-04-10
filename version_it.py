# this file should be run whenever the package version is incremented

quit = "n"
while str.lower(quit) != "y":
    version = input("enter your version number here (e.g. x.x.x): ")
    print(f"are you sure you want to version to {version}?")
    answer = input("enter y/n: ")
    if str.lower(answer) == "y":
        with open("README_template.md", "r") as f:
            readme = f.read().format(version=version)

        with open("README.md", "w") as f:
            f.write(readme)

        with open("definitions.py", "w") as f:
            f.write(f"version='{version}'")

        quit = "y"
    else:
        quit = input("exit? y/n: ")

