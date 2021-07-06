import json
import cv2
import numpy as np
import urllib.request

# https://segments.ai/prgmti1/school_hallway/releases에서 받은 v3 json파일
with open('/content/school_hallway-v3.json','r') as f:
  annotations = json.load(f) 
  
#파일 저장 폴더 지정 및 images, annotation 파일 생성
base_dir = '/content/drive/MyDrive/school_hallway_v2'
images_train_dir = os.path.join(base_dir,'images_train')
os.mkdir(images_train_dir)
annotation_train_dir = os.path.join(base_dir,'annotation_train')
os.mkdir(annotation_train_dir)

def url_to_image(url):
  resp = urllib.request.urlopen(url)
  image = np.asarray(bytearray(resp.read()), dtype='uint8')
  image = cv2.imdecode(image, cv2.IMREAD_COLOR)
  return image

cnt = 0

for i in range(3000):
  if annotations['dataset']['samples'][i]['labels']['ground-truth']:
    print(annotations['dataset']['samples'][i])
    #print(annotations['dataset']['samples'][i].keys())
    img_url = annotations['dataset']['samples'][i]['attributes']['image']['url']
    img = url_to_image(img_url)
    annotation_url = annotations['dataset']['samples'][i]['labels']['ground-truth']['attributes']['segmentation_bitmap']['url']
    annotation = url_to_image(annotation_url)
    cv2.imwrite(os.path.join(images_train_dir,'{0}.png'.format(cnt)),img)
    cv2.imwrite(os.path.join(annotation_train_dir,'{0}.png'.format(cnt)),annotation)
    cnt += 1
    
#https://segments.ai/prgmti1/school_hallway_v2/releases 에서 받은 v.01 json 파일 
with open('/content/school_hallway_ver2-v0.1.json','r') as f:
  annotations = json.load(f) 
cnt += 1
for i in range(440):
  if annotations['dataset']['samples'][i]['labels']['ground-truth']:
    print(annotations['dataset']['samples'][i])
    #print(annotations['dataset']['samples'][i].keys())
    img_url = annotations['dataset']['samples'][i]['attributes']['image']['url']
    img = url_to_image(img_url)
    annotation_url = annotations['dataset']['samples'][i]['labels']['ground-truth']['attributes']['segmentation_bitmap']['url']
    annotation = url_to_image(annotation_url)
    cv2.imwrite(os.path.join(images_train_dir,'{0}.png'.format(cnt)),img)
    cv2.imwrite(os.path.join(annotation_train_dir,'{0}.png'.format(cnt)),annotation)
    cnt += 1
    
