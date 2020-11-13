#Bulk Watermark
#Author KingMarti
#Version 0.1
################################################################################
#                                                                              # 
#                   EDIT THESE DETAILS WITH YOUR INFO                          #
#                                                                              #
################################################################################

#When running on windows, sperate folders with a double slash \\ eg. C:\\Users\\User\\Documents\\File
watermark = '' #Enter The Text You Would Like To Add To Your Images Within The Quotes
directory ='' #Enter The dirercrtory containing your images within the quotes 
save_to = '' #Enter the save to directory within the quotes

watermark_font ='ariblk.ttf' #'Enter the name of the font winthin the quotes and the file type (normally .ttf)'
watermark_size = 0.05 #percentage of the width used to set the font size. Defualt is 0.05 or 5%
################################################################################
#                                                                              #
#               Feel Free to make a copy and play with the code below          #
#                   The code below is what will add the watermark              #
#                                                                              #
################################################################################                 

################################################################################
#                                                                              #
#                               Module Imports                                 #
#                                                                              #
################################################################################
from PIL import Image,ImageDraw,ImageFont
import os

################################################################################
#                                                                              #
#                    Find Images And Add The Watermark                         #
#                                                                              #
################################################################################
for filename in os.listdir(directory):
    if filename.endswith('.jpeg') or filename.endswith('.jpg') or filename.endswith('.png'):
        image = Image.open(os.path.join(directory,filename))        
        print(filename)
        width,height = image.size
        print('The Image Is: ',image.size[0])
        fontsize = round(image.size[0]*watermark_size)
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(watermark_font,fontsize)
        text_width,text_height = draw.textsize(watermark,font)
        
        # Margin defines the spacing from the bottom of the image
        #the decimal number on the end can be changed 
        #rthis number is a percentage of the image height
        #Defualt is 2.5% 
        
        margin=image.size[1]*0.025
        # x defines where across the width of the image the watermark will display
        #to change this change the number value
        x= width/1.75 - text_width
        # y defines where on the height of the image the watermark will display
        #to change this change the margin above. 
        y= height - text_height -margin
        draw.text((x,y),watermark,font=font)
        image.save(save_to+filename)
        print('Saving ',filename,' To ',save_to+filename)
