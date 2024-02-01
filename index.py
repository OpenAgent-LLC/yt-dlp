import json

import yt_dlp

def handler(event, context):
    print(f'event: {event}')

    # The body of the request is a JSON string in 'event['body']'
    body = event.get('body')

    if not body:
            return {
                'statusCode': 400,
                'body': json.dumps('No body in request')
            }

    try:
        # The body of the request is a JSON string in 'event['body']'
        url = json.loads(body).get('url')

        if not url or url == '':
            return {
                'statusCode': 400,
                'body': json.dumps('No url in request')
            }

        # Call the YT_DLP processing. Example URL: https://vimeo.com/126035665
        results = yt_dlp._real_main_castera([url])

        # Return the results
        return {
            'statusCode': 200,
            'body': json.dumps(results)
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid JSON')
        }
    except Exception as e:
        # Handle any other exceptions that might occur
        return {
            'statusCode': 500,
            'body': json.dumps(f'An error occurred: {str(e)}')
        }
