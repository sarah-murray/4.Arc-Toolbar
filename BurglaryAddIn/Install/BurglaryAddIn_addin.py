import arcpy
import pythonaddins

class RiskButton(object):
    """Implementation for BurglaryAddIn_addin.RiskButton (Button)"""
    def __init__(self):
        self.enabled = True
        self.checked = False
    def onClick(self):
        pythonaddins.GPToolDialog("M:/All_GIS_work/Programming2/Prac1/Models.tbx", "TraffordModelScript")