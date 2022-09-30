''' This file contains all of the utility functions for the ingestion application'''

import json

def alter(mixtape, changes):
    # Add a new playlist; the playlist should contain at least one song
    # Add an existing song to an existing playlist
    # Remove a playlist
    for change in changes:
        if change['type'] == 'add_playlist':
            mixtape = add_playlist(mixtape, change)
        elif change['type'] == 'add_song_to_playlist':
            mixtape = add_song(mixtape, change)
        elif change['type'] == 'remove_playlist':
            mixtape = remove_playlist(mixtape, change)
        else:
            print('ERROR: INVALID CHANGE REQUEST')
    return mixtape

def add_playlist(mixtape, change_obj):
    new_playlist = {} # new dictionary to append
    new_playlist['id'] = str(len(mixtape['playlists']) + 1) 

    # check if user exists  
    if change_obj['user_id'] not in [m['id'] for m in mixtape['users']]:
        print('ERROR: USER DOES NOT EXIST')
        return mixtape
    new_playlist['user_id'] = change_obj['user_id']

    # check if songs exist
    for ids in change_obj['song_ids']:
        # if the song_id does not exist, remove it from the list
        if not any(ids in i['id'] for i in mixtape['songs']):
            change_obj['song_ids'].remove(ids)
    new_playlist['song_ids'] = change_obj['song_ids']

    mixtape['playlists'].append(new_playlist)
    return mixtape

def add_song(mixtape, change_obj):
    # check if song exists
    for ids in change_obj['song_id']:
        # if the song_id does not exist, remove it from the list
        if not any(ids in i['id'] for i in mixtape['songs']):
            print('ERROR: SONG DOES NOT EXIST')
            return mixtape

    # look for corresponding playlist_id, then append song to list of song_ids
    for playlist in mixtape['playlists']:
        if playlist['id'] == change_obj['playlist_id']:
            playlist['song_ids'].append(change_obj['song_id'])

    return mixtape

def remove_playlist(mixtape, change_obj):
    for playlist in mixtape['playlists']:
        if playlist['id'] == change_obj['playlist_id']:
            mixtape['playlists'].pop(mixtape['playlists'].index(playlist))
            print('SUCCESS: PLAYLIST REMOVED')
    return mixtape

def output(mixtape, filename):
    # create the file if it doesn't exist then open it in write mode
    with open(filename, 'w+') as output_file:
        json.dump(mixtape, output_file)


