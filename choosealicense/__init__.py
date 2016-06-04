# -*- coding: utf-8 -*-

__author__ = 'Audrey Roy Greenfeld'
__email__ = 'aroy@alum.mit.edu'
__version__ = '0.1.0'


from cookiecutter.generate import generate_file, generate_block
from cookiecutter.plugins import CookiecutterPlugin


class ChooseALicensePlugin(CookiecutterPlugin):
    """Plugin for choosing a license, then outputting the LICENSE file into
    the generated project's root directory"""

    extra_prompts = {
    	"open_source_license": [
            "MIT",
            "BSD",
            "ISCL",
            "Apache Software License 2.0",
            "Not open source"
        ]
    }

    def insert_license_file():
        """
        Given `context["open_source_license"]`, insert the corresponding
        license file into the generated project's root.
        """
        generate_file(
            project_dir="..",
            infile="LICENSE",
            context=self.context,
            env=self.env
        )

    def insert_trove_classifiers():
        """
        Given a license choice, render the block for the trove classifiers.

        Use in a templated file like this:

            {{ choosealicense.insert_trove_classifiers() }}
        """
        # Like generate_file, but returns the generated string instead of
        # writing the string to a file.
        return generate_block(
            unrendered="_trove_classifiers.txt",
            context=self.context,
            env=self.env
        )
