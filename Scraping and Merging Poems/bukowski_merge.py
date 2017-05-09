import os
import shutil

def merge():
    filename = 'bukowski_merge.txt'
    fulltext = '\n'
    os.chdir('bukowski poems')
    with open(filename, 'w') as file:
        for poem in os.listdir('.'):
            with open(poem, 'r') as text:
                fulltext += str(text.read())
        print fulltext
        os.chdir('..')
        file.write(fulltext)
    shutil.move('bukowski poems/' + filename, 'C:\PythonScripts\Bukowski Bot\\' + filename)

merge()
