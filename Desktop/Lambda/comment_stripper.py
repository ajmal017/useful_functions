import easygui
import pandas as pd



def strip_comments():
    script_to_strip = easygui.fileopenbox(title='Upload your script', filetypes= ['*.txt'])

    full_script = pd.read_fwf(script_to_strip)
    full_script.columns = ['lines_of_code']
    comments_only = full_script[full_script['lines_of_code'].str.contains('#')]
    for rows in comments_only['lines_of_code']:
        print(rows)

strip_comments()