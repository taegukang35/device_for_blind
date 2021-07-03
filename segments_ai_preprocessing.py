import json
import cv2
import numpy as np
import urllib.request


with open('/content/drive/MyDrive/myfile/school_hallway-test.json','r') as f:
  annotations = json.load(f) #dataset from segments.ai 

base_dir = '/content/drive/MyDrive/school_hallway'
images_train_dir = os.path.join(base_dir,'images_train')
#os.mkdir(images_train_dir)
annotation_train_dir = os.path.join(base_dir,'annotation_train')
#os.mkdir(annotation_train_dir)

def url_to_image(url):
  resp = urllib.request.urlopen(url)
  image = np.asarray(bytearray(resp.read()), dtype='uint8')
  image = cv2.imdecode(image, cv2.IMREAD_COLOR)
  return image

for i in range(3000):
  if annotations['dataset']['samples'][i]['labels']['ground-truth']:
    print(annotations['dataset']['samples'][i])
    print(annotations['dataset']['samples'][i].keys())
    img_url = annotations['dataset']['samples'][i]['attributes']['image']['url']
    img = url_to_image(img_url)
    annotation_url = annotations['dataset']['samples'][i]['labels']['ground-truth']['attributes']['segmentation_bitmap']['url']
    annotation = url_to_image(annotation_url)
    cv2.imwrite(os.path.join(images_train_dir,'{0}.png'.format(i)),img)
    cv2.imwrite(os.path.join(annotation_train_dir,'{0}.png'.format(i)),annotation)
