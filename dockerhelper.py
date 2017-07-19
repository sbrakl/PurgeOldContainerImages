#!/usr/bin/env python

import docker
from datetime import datetime

def GetListOfImages():
    client = docker.from_env()
    conimages = client.images.list()
    #ImageName, Version, imageshortId, ImageDate
    shabsImageList = []
    for img in conimages:
        imgID = img.short_id
        imgTags  = img.tags
        timeelapse = img.attrs["Created"]
        imgDt = datetime.fromtimestamp(timeelapse)
        if imgTags == []:
            print "Tag empty for ", imgID, ", removing non tag Container"
            client.images.remove(imgID)
        for tag in imgTags:
            imgtag = tag.split(":")
            imageName = imgtag[0]
            imageVersion = imgtag[1]
            shabsImageList.append([imageName, imageVersion, imgID, imgDt])

    return shabsImageList


def RemoveContainerImage(short_image_ID):
    client = docker.from_env()
    conimages = client.images.list()
    # ImageName, Version, imageshortId, ImageDate
    for img in conimages:
        if img.short_id == short_image_ID:
            print "Removing Container " + img.short_id
	    try:
            	client.images.remove(img.id)
	    except Exception as e:
		print e.__doc__
		print e.message
