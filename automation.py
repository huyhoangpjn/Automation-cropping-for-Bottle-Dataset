import os 
import cv2

def automation(path, epsillon):
    dir_list = os.listdir(path)
    os.chdir(path)
    out_path = os.path.join(path, ".out")
    try:    
        os.mkdir(out_path)
    except:
        pass

    for file in dir_list:
        os.chdir(path)
        if '.txt' in file:
            with open(file, 'r') as f:
                content = f.read().split(" ")
                index = content[0]
                f.close()
            file = file.split('.')
            img = cv2.imread(file[0]+'.jpg')
            X = int(float(content[2])*img.shape[0])
            Y = int(float(content[1])*img.shape[1])
            W = int(float(content[3])*img.shape[0])
            H = int(float(content[4])*img.shape[1])
            #Convert to square size
            if W>H:
                H = W
            else:
                W = H
            #Avoid overflow the edge, in this case, a problem is on data -> Can't fix the size to square size
            #Now, we call (a,b),(c,d) is 2 coordinates of 2 vertices
            
            a = X-int(W/2) - int(epsillon)
            b = Y-int(H/2) - int(epsillon)
            c = X+int(W/2) + int(epsillon)
            d = Y+int(H/2) + int(epsillon)

            if X-int(W/2) < 0:
                a = 0
            if Y-int(H/2) < 0:
                b = 0
            if X+int(W/2) > img.shape[0]:
                c = img.shape[0]
            if Y+int(H/2) > img.shape[1]:
                d = img.shape[1]
            img = img[a:c,b:d]

            #Save img
            name_img = file[0].replace(",","") + '.jpg'
            os.chdir(out_path)
            cv2.imwrite(name_img, img)

        
