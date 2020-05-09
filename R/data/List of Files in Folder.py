"""LIST FILES IN FOLDER."""
import os

#
# CREATES LIST WITH THE NAMES OF THE FILES IN THE FOLDER
#
files = os.listdir('datasets')
# REMOVE .rmd FILES
for filename in list(files):
    if filename.endswith('.rmd'):
        files.remove(filename)
# REMOVE HIDDEN FILES
hidden_files = [file for file in files if file.startswith('.')]
if hidden_files:
    files = list(set(files) - set(hidden_files))
# FINISH
files = sorted(files, key=str.lower)
for file in files:
    print(
        '  <td style="width:150%;" valign="top">' +
        '<iframe width=100% height="6000" src="datasets/' + file +
        '" seamless></iframe></td>'
    )
