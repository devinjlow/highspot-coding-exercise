# highspot-coding-exercise
My submission for Highspot's interview coding exercise

## How-to-Run
This application can be run on command line with python
ex. $ python3 mixtape.json changes.json output.json
mixtape and changes files should named accordingly. 

## Scaling
JSON is handled as a block file, then parsed. In my code example, json.load() loads the entire
file into memory before any functions are run on it.
At scale, it would be viable to parse the JSON data as a stream. Small chunks of the file would 
be loaded into memory, parsed, then repeated. JSON processing APIs/libraries can be used to stream
the large JSON objects.
