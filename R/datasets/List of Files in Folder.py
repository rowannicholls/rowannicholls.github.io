"""LIST FILES IN FOLDER."""
import os

#
# CREATES LIST WITH THE NAMES OF THE FILES IN THE FOLDER
#
files = os.listdir()
files.remove(os.path.basename(__file__))
# REMOVE .rmd FILES
for filename in list(files):
    if filename.endswith('.rmd'):
        files.remove(filename)
files.remove('aaa_Pre-Loaded-Datasets - Wrapper.html')
# FINISH
files = sorted(files, key=str.lower)
for file in files:
    print('  <td style="width:150%;" valign="top"><iframe width=100% height="6000" src="' + file + '" seamless></iframe></td>')
