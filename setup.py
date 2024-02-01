from setuptools import setup, find_namespace_packages

setup(name='Personal assistant',
      version='1.0',
      description='Your personal digital assistant',
      url='https://github.com/mal4ishka/Team-Project',
      author='Mad hedgehogs',
      author_email='nesterovvlad@gmail.com',
      license='MIT',
      packages=find_namespace_packages(),
      include_package_data=True,
      entry_points={'console_scripts': ['PA = PA.input_handler.handler:handler']})