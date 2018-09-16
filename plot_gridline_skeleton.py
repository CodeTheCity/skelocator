import json
import cv2
import os
from math import sqrt

def dist(pt1, pt2):
    return sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)

# =============================================================================
dirname = 'scanned plans (jpg)'
plan_filename = 'PLAN031.jpg'
 ## Test a skeleton
skeleton_number = 63 # number of the skeleton
body_part = 'ankle' # part of the body of the skeleton to show
# =============================================================================

image = cv2.imread(os.path.join(dirname,plan_filename))

with open('annotations_plan31.json') as json_data:
    annotations = json.load(json_data)
    json_data.close()
    
# =============================================================================
#Find the reference points

list_references_east = []
average_x_east = 0
average_distance_references = 0
for i, mark in enumerate(annotations[0]['annotations']):
    if mark['class'] == 'reference' and mark['position']=='east':
        if list_references_east:
            distance = dist(list_references_east[-1][0], (mark['x'],mark['y']))
            average_distance_references += distance
        average_x_east += mark['x']
        list_references_east.append([(mark['x'],mark['y']),mark['number']])
average_x_east = average_x_east/len(list_references_east)
average_distance_references = average_distance_references/(len(list_references_east)-1)

## align references
list_references_east_aligned = list_references_east.copy()
for i,pos in enumerate(list_references_east):
   list_references_east_aligned[i][0]=(average_x_east,pos[0][1])
   flag_valid_coordinate = True
   acc = 0
   coord = [pos[0][0],pos[0][1]]
   while flag_valid_coordinate:           
       cv2.circle(image,(int(coord[0]),int(coord[1])),20,(255,0,255),-1)
       cv2.putText(image,'('+str(pos[1])+','+str(acc)+')',(int(coord[0]),int(coord[1])),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,255),3)
       coord[0]=coord[0]-average_distance_references
       if coord[0]<0:
           flag_valid_coordinate = False
       acc +=1
           
          

for i, mark in enumerate(annotations[0]['annotations']):
    if mark['class']=='skeleton':
        if mark['subclass']=='sk'+str(skeleton_number) and mark['type']==body_part:
            cv2.circle(image,(int(mark['x']),int(mark['y'])),20,(255,0,0),-1)
            cv2.putText(image,'sk'+str(skeleton_number)+'-'+body_part,(int(mark['x']),int(mark['y'])),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,0),3)
        

           
cv2.imwrite('sk'+str(skeleton_number)+'-'+body_part+"_sanitycheck.jpg", image)
cv2.namedWindow("Markup", cv2.WINDOW_NORMAL)
cv2.imshow("Markup", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

