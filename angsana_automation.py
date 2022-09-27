import requests
import sys

#Your Access Keys
page_id_1 = 104311632452675 # The Angsana Network FB page
facebook_access_token_1 = 'EABMyuDjV64cBAGrgVbYH6Vzd6aVCRhV8A9jAGyNCgAxL7NM9yZBQ8hoRS56hpaZCwUpDtnoALKF7ydtzd6y1nuqW1vmmNCrPB4NGcXrOZCWWIwL3UAsa0eW1OvSM42gKVhRjzcAsB18T0wEKuiyxJrwkG8ZCrZCKHO1RZC3PQynGZAMQRK5n32Cgb6OJoqSZCHk4kOgDudVG7QZDZD'
if len(sys.argv) < 3:
  print('Missing parameters')
  print('Format: python3 angsana_automation.py <"image"/"textonly"> <post message filename> [<image filename if in image mode>]')
  exit()

post_type = sys.argv[1]
msg_filename = sys.argv[2]
# Read post message
with open(msg_filename) as msg_file:
  msg = msg_file.read()
  print(msg)

if post_type == 'image' and len(sys.argv) < 4:
  print('Missing image filename')
  print('Format: python3 angsana_automation.py <"image"/"textonly"> <post message filename> [<image filename if in image mode>]')
elif post_type == 'image':
  image_url = 'https://graph.facebook.com/{}/photos'.format(page_id_1)
  img_payload = {
    'access_token': facebook_access_token_1,
    'caption': msg
  }

  image_filename = sys.argv[3]
  files = {
    'source': open(image_filename, 'rb')
  }

  r = requests.post(image_url, data=img_payload, files=files)
  print(r.text)
else:
  post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)
  payload = {
    'message': msg,
    'access_token': facebook_access_token_1
  }
  r = requests.post(post_url, data=payload)
  print(r.text)
  
