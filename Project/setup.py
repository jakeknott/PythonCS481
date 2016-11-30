from distutils.core import setup

setup(name='PySchedule', # the package/module name
      version='1.0', # the version (an arbitrary string)
      author='Jake Knott', # someone to blame
      author_email='jacob.knott@wsu.edu', # where to flame
      py_modules=[ 'PySchedule', 'PyScheduleLogic', 'Course', 'SchdulerTests'], # modules in the package
      data_files=[('ui', ['./ui/PySchedule.ui'])]
      )