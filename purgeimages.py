#!/usr/bin/env python
import numpy as np
import argparse
import dockerhelper

parser = argparse.ArgumentParser()
parser.add_argument('--Keep', help="Number of containers to keep per service", default=3)
parser.add_argument('--WhatIf', help="Will not remove containers, would just notity what it would be deleting", default=False)
args = parser.parse_args()

numOfContainersToKeep = args.Keep

conImageList = dockerhelper.GetListOfImages()

# Slice multi dimension list to extract just imageName
npArr  = np.array(conImageList)
imgNames  = npArr[:, 0]
print "### Total images found: ", len(imgNames)
uniqueImgNames, counts = np.unique(imgNames, return_counts=True)
print "### Unique images with count: ", len(uniqueImgNames)
uarr = np.column_stack((uniqueImgNames, counts))
imagesWithMoreThan3Version = uarr[uarr[:, 1] > numOfContainersToKeep]
print "### Images with more than 3 version"

for img in imagesWithMoreThan3Version:
    imageName = img[0]
    print "### Image"
    print imageName
    # Gets all the images for this imageName
    versions = npArr[npArr[:, 0] == imageName]
    # Sorting of the date, older first newer later
    versions = versions[versions[:, 3].argsort()]
    print "### Images List"
    print  versions
    # Numbers of rows
    rowCount = versions.shape[0]
    # Skipping last 3 rows
    newRowCount = rowCount - numOfContainersToKeep;
    ImagesToRemove = versions[:newRowCount]
    print "### Image to remove"
    print ImagesToRemove