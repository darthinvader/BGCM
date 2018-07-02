# BGCM
BGCM(Board Game Card Maker) is a simple python app to allow you to build complicated cards for Board Games that you want to create.

It has three components to add to a card:

Images, One Line Text and Multiline Text

Only those 3 components are required to make all the cards you will ever need.

It also contains a parser for an input file that has the latter format:

&

Folder to be saved

!

SizeX SizeY Name to be saved

@Image_Path SizeX SizeY LocationX LocationY@

$One Line Text SizeX SizeY LocationX LocationY font$
 
%Multiline Text SizeX SizeY LocationX LocationY font%

!

&

You can add as many images and texts as you want and they will always be added in order
(if  two components occupy the same space the latter will always show on top)