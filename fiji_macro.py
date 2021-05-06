#@String datapath
#@String resultpath

from __future__ import with_statement
import os
from ij import IJ
from ij import WindowManager as wm


if __name__ == '__main__':

	def extract_FoV(path):
		"""
		get the name of field of views for a sample (format - XnYnRnWnCn)
		para: path - string
		return: fovs - set of string (unique names only)
		"""
		fovs = []
		for root, dirs, files in os.walk(path):
			for name in files:
				if name.endswith('.tif'):
					fovs.append(name[:10])
		fovs = set(fovs)
		return fovs

	fovs = extract_FoV(datapath)
	
	for field in fovs:
		abFile = datapath + '/' + field + '_6E10.tif'
		apoeFile = datapath + '/' + field + '_F9.tif'
		IJ.open(abFile)
		IJ.run("Z Project...", "projection=[Average Intensity]")
		IJ.open(apoeFile)
		IJ.run("Z Project...", "projection=[Average Intensity]")

		IJ.run("Merge Channels...", "c1=AVG_"+field+"_6E10.tif c2=AVG_"+field+"_F9.tif create")
		IJ.selectWindow("Composite")
		IJ.run("Detect Particles", "calculate max=3 rois=Ovals add=Nothing ch1i ch1a=5 ch1s=20 ch2i ch2a=5 ch2s=20")
		IJ.selectWindow('Results')
		IJ.saveAs('table', resultpath+'/'+ field +'_results.csv')
		IJ.selectWindow('Summary')
		IJ.saveAs('text', resultpath+'/'+ field +'_summary.txt')
		IJ.selectWindow("Composite")
		IJ.saveAs('tif', resultpath+'/'+ field +'.tif')
		IJ.run("Close")
		IJ.run("Close")
		IJ.run("Close")


	IJ.run("Quit")

