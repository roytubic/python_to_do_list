# release.py

import os
import sys
from setuptools import setup, find_packages

# Custom version management logic (update your package's version file accordingly)
def bump_version(file_path, part):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith('__version__'):
            old_version = line.split('=')[1].strip().strip('\'"')
            parts = old_version.split('.')
            if part == 'major':
                parts[0] = str(int(parts[0]) + 1)
            elif part == 'minor':
                parts[1] = str(int(parts[1]) + 1)
            elif part == 'patch':
                parts[2] = str(int(parts[2]) + 1)
            new_version = '.'.join(parts)
            lines[i] = f"__version__ = '{new_version}'\n"

    with open(file_path, 'w') as f:
        f.writelines(lines)

# Update your package's version file
version_file_path = 'your_package/__init__.py'  # Adjust to your project's structure
bump_version(version_file_path, 'patch')  # You can use 'major', 'minor', or 'patch' for version bumping

# Your package's metadata
metadata = {
    'name': 'your_package_name',
    'version': new_version,  # Use the updated version
    'description': 'Your package description',
    'author': 'Your Name',
    'author_email': 'your@email.com',
    'url': 'https://github.com/yourusername/your_package',
    # ... other package metadata
}

# Define package details
packages = find_packages()
package_data = {metadata['name']: ['*']}

setup(
    packages=packages,
    package_data=package_data,
    **metadata,
)

if 'upload' in sys.argv:
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
