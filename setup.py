from setuptools import setup

import setuptools_i18n

PROJECT_NAME = 'setuptools_i18n'


def main():
    setup(name=PROJECT_NAME,
          version=setuptools_i18n.__version__,
          py_modules=['setuptools_i18n'],
          entry_points={
              "distutils.commands": [
                  "build_i18n = setuptools_i18n:build_i18n",
              ],
              "distutils.setup_keywords": [
                  "i18n_files = setuptools_i18n:validate_i18n",
              ],
          },
          license='GPLv3',
          author='Tomas Pazderka',
          author_email='tomas.pazderka@nic.cz',
          classifiers=[
              'Development Status :: 4 - Beta',
              'Intended Audience :: Developers',
              'Topic :: Software Development :: Build Tools',
              'License :: OSI Approved :: GPLv3 License',
              'Programming Language :: Python :: 2',
              'Programming Language :: Python :: 2.6',
              'Programming Language :: Python :: 2.7',
              'Programming Language :: Python :: 3',
              'Programming Language :: Python :: 3.5',
              'Programming Language :: Python :: 3.6',
          ],
          )


if __name__ == '__main__':
    main()
