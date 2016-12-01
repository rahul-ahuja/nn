
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
    
    
    for line in lines:
        for x1,y1,x2,y2 in line:
            m = ((y2-y1)/(x2-x1))
            if m < -0.2:  #left line, negative slope
                x_left.append(x1)
                x_left.append(x2)
                y_left.append(y1)
                y_left.append(y2)
                slope_left.append(m)
            else:
                x_right.append(x1)
                x_right.append(x2)
                y_right.append(y1)
                y_right.append(y2)
                slope_right.append(m)
                
            #f_left = np.polyfit(np.array(x_left),np.array(y_left),1)
            #f_right = np.polyfit(np.array(x_right),np.array(y_right),1)
            #cv2.line(img, (x1, y1), (x2, y2), color, thickness)
            #cv2.line(img, (x1, int(f_left(x1))), (x2, int(f_left(x2))), color, thickness)
            #cv2.line(img, (x1, int(f_right(x1))), (x2, int(f_right(x2))), color, thickness)
    av_slope_left = np.mean(slope_left)
    av_slope_right = np.mean(slope_right)
    av_x_left = np.mean(x_left)
    av_x_right = np.mean(x_right)
    av_y_left = np.mean(y_left)
    av_y_right = np.mean(y_right)
    y_left_intercept = av_y_left - av_x_left * av_slope_left
    y_right_intercept = av_y_right - av_x_right * av_slope_right
    
    x1_left = (y_min - y_left_intercept) / av_slope_left 
    x1_right = (y_min - y_right_intercept) / av_slope_right
    x2_left = (y_max - y_left_intercept) / av_slope_left 
    x2_right = (y_max - y_right_intercept) / av_slope_right
    
    cv2.line(img, (int(x1_left), y_min), (int(x2_left), y_max), color, thickness)
    cv2.line(img, (int(x1_right), y_min), (int(x2_right), y_max), color, thickness)


