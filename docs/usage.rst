=====
Usage
=====

To use Choose a License in a Cookiecutter project template:

1. Add this to hooks/post_gen_project.py

    insert_license_file()

2. If using this for a Python package, add these two arguments to `setup()`
inside of `setup.py`:

    license="{{ cookiecutter.open_source_license }}"

    classifiers=[
        {{ choosealicense.insert_trove_classifiers() }}
    ]

3. Add the license to the generated project's README:

    "Free Software: {{ cookiecutter.open_source_license }}"

4. Add to plugin_requirements.txt:

    choosealicense==0.2.0
