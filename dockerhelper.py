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
        for tag in imgTags:
            imgtag = tag.split(":")
            imageName = imgtag[0]
            imageVersion = imgtag[1]
            shabsImageList.append([imageName, imageVersion, imgID, imgDt])

    return shabsImageList