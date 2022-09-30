'''Command line runner for application'''

import sys
import ingestion
import json

def main(args):
    if len(args) < 3:
        print('ERROR: INCORRECT USAGE')
        print('mixtape.py <input_filename>, <changes_filename>, <output_filename>')

    elif args[0].startswith('mixtape') and args[1].startswith('changes'):
        # string -> file object for input and change files
        input_file, changes_file, output_file = open(args[0]), open(args[1]), args[2]

        try:
            input_file, changes_file = json.load(input_file), json.load(changes_file)
        except ValueError:
            print('ERROR: WRONG FILE FORMAT. TRY JSON')
        
        new_mixtape = ingestion.alter(input_file, changes_file)
        ingestion.output(new_mixtape, output_file)
        print(new_mixtape)
        print('CHANGES SUCCESSFUL')
    else:
        # make sure that filenames aren't swapped, doing so could cause errors during runtime
        print('ERROR: INPUT FILE MUST BE NAMED mixtape.json AND CHANGES FILE MUST BE NAMED changes.json')
    

if __name__=='__main__':
    main(sys.argv[1:])
