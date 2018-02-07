'''
Write a login event to S3.
'''

import logging
import json
import os

# Initialize objects and set variables that are not invocation specific to
# exploit container reuse.
log_level = os.environ.get('LOG_LEVEL', 'INFO')
logging.root.setLevel(logging.getLevelName(log_level))
_logger = logging.getLogger(__name__)

def handler(event, context):
    '''Lambda entry point.'''
    _logger.info('Event received: {}'.format(json.dumps(event)))

    return {"NoCode": "OK"}
