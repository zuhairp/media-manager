from os import environ as env

DOWNLOADS_DIRECTORY = env.get('DOWNLOADDIR', '/tmp/downloads')
STAGING_DIRECTORY = env.get('STAGINGDIR', '/tmp/staging')