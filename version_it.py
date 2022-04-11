# this file should be run whenever the package version is incremented

quit = "n"
while str.lower(quit) != "y":
    version = input("Enter your version number here (e.g. x.x.x): ")
    print(f"Are you sure you want to version to {version}?")
    answer = input("Enter y/n: ")
    if str.lower(answer) == "y":
        with open("README_template.md", "r") as f:
            readme = f.read().format(version=version)

        with open("README.md", "w") as f:
            f.write(readme)

        with open("definitions.py", "w") as f:
            f.write(f"version='{version}'")

        print("Don't forget to update the docs via `make html`...")
        quit = "y"
    else:
        quit = input("Exit? y/n: ")

