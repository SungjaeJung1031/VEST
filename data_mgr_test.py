from lib.nuscenes.nuscenes import NuScenes
import os

dataroot = "/Users/sungjaejung1031/dev/proj/VEST/resource/data/v1.0-mini"
print(dataroot)

nusc = NuScenes(version='v1.0-mini', dataroot=dataroot, verbose=True)

print(len(nusc.sample))