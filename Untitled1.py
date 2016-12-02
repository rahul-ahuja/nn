
# coding: utf-8

# In[ ]:

def draw_lines(img, lines, color=[255, 0, 0], thickness=2):
    """
    NOTE: this is the function you might want to use as a starting point once you want to 
    average/extrapolate the line segments you detect to map out the full
    extent of the lane (going from the result shown in raw-lines-example.mp4
    to that shown in P1_example.mp4).  
    
    Think about things like separating line segments by their 
    slope ((y2-y1)/(x2-x1)) to decide which segments are part of the left
    line vs. the right line.  Then, you can average the position of each of 
    the lines and extrapolate to the top and bottom of the lane.
    
    This function draws `lines` with `color` and `thickness`.    
    Lines are drawn on the image inplace (mutates the image).
    If you want to make the lines semi-transparent, think about combining
    this function with the weighted_img() function below
    """
    x_left = []
    y_left = []
    x_right = []
    y_right = []
    slope_left = []
    slope_right = []
    y_max = img.shape[1]
    y_min = min(np.amin(lines,axis=0)[0][1],np.amin(lines,axis=0)[0][3])
    #print ("y_min:", y_min)
    
    
    for line in lines:
        for x1,y1,x2,y2 in line:
            m = ((y2-y1)/(x2-x1))
            if m < -0.5:  #left line, negative slope
                x_left.append(x1)
                x_left.append(x2)
                y_left.append(y1)
                y_left.append(y2)
                #slope_left.append(m)
            elif m > 0.5:
                
                x_right.append(x1)
                x_right.append(x2)
                y_right.append(y1)
                y_right.append(y2)
                #slope_right.append(m)
                
                
    z_left = np.polyfit(np.array(x_left),np.array(y_left),1)
    #f_left = np.poly1d(z_left)
    #print(np.array(x_right),np.array(y_right))
    if x_right != [] and y_right != []:
        
        z_right = np.polyfit(np.array(x_right),np.array(y_right),1)
        av_x_right = np.mean(x_right)
        #cv2.line(img, (int((y_min - z_right[1]) / z_right[0]), y_min), (int((y_max - z_right[1]) / z_right[0]), y_max), color, thickness)
        cv2.line(img, (int(av_x_right), int((av_x_right * z_right[0]) - z_right[1])), (int((y_max - z_right[1]) / z_right[0]), y_max), color, thickness)

    #f_left = np.poly1d(z_right)

            #cv2.line(img, (x1, y1), (x2, y2), color, thickness)
    cv2.line(img, (int((y_min - z_left[1]) / z_left[0]), y_min), (int((y_max - z_left[1]) / z_left[0]), y_max), color, thickness)
