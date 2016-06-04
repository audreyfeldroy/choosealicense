# -*- coding: utf-8 -*-

__author__ = 'Audrey Roy Greenfeld'
__email__ = 'aroy@alum.mit.edu'
__version__ = '0.1.0'


from cookiecutter.generate import generate_file
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

    def insert_license():
        """
        Given a license choice, insert the corresponding license file into the
        generated project's root.
        """
        generate_file(
            project_dir="..",
            infile="LICENSE",
            context=self.context,
            env=self.env
        )
