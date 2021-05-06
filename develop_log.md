## Develop log for CoincidenceAnalysis

# 20200912
Stage 1 Requirements:
1. Number of coincidence spots
2. Percentage of coincidence
3. Coincident coefficient

Stage 2 Requirements:
1. Size of spots in Abeta channel
2. Intensity of spots in Abeta channel

Stage 3 Requirement:
Fibiril Abeta length

Input data:
512x512 images
marked with 6E10(Abeta) and F9(ApoE)
3 layers of directory(apart from blank)

Ideas:
- Use fiji or python
- generate report at the root

Progress:
- https://imagej.net/Spots_colocalization_(ComDet)
- https://github.com/ekatrukha/ComDet/wiki/How-does-detection-work%3F
- Colocalization is based on the distance between spots' centres of mass.
- The plugin can only process one FoV at one time. 