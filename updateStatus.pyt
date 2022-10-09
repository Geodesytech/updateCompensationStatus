# -*- coding: utf-8 -*-

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = "toolbox"

        # List of tool classes associated with this toolbox
        self.tools = [CompensationStatus]


class CompensationStatus(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "CompensationStatus"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        parcelId = arcpy.Parameter(
            displayName="Parcel ID",
            name="parcel_id",
            datatype="GPString",
            parameterType="Required",
            direction="Input")
        docNo = arcpy.Parameter(
            displayName="Document No",
            name="doc_no",
            datatype="GPString",
            parameterType="Required",
            direction="Input")
        postingDate = arcpy.Parameter(
            displayName="Posting Date",
            name="posting_date",
            datatype="GPString",
            parameterType="Required",
            direction="Input")
        comStatus = arcpy.Parameter(
            displayName="Compensation Status",
            name="com_status",
            datatype="GPString",
            parameterType="Required",
            direction="Input")

        params = [parcelId, docNo, postingDate, comStatus]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        for param in parameters:
            arcpy.AddMessage("-----------------------")
            arcpy.AddMessage(f"Parameter ValueAsText: {param.valueAsText}")
            arcpy.AddMessage(f"Parameter Value: {param.value}")
            arcpy.AddMessage(f"Parameter Type: {type(param)}")
            arcpy.AddMessage("-----------------------")

        SQLQuery = "parcel_id={}".format(parameters[0].valueAsText)

        landFC = r"C:\data.gdb\lines"
        updatefield = ["doc_no", "posting_date", "com_status"]

        with arcpy.da.UpdateCursor(landFC, updatefield, where_clause=SQLQuery) as cursor:
            for row in cursor:
                i = 0
                for param in parameters:
                    row[i] = param.valueAsText
                    i = i + 1
                cursor.updateRow(row)
            del cursor
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
