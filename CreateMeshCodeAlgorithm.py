# -*- coding: utf-8 -*-

"""
/***************************************************************************
 CreateMeshCodeAlgorithm
                                 A QGIS plugin
Add Mesh data to the table
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-09-27
        copyright            : (C) 2021 by Y.Kayama/Aeroasahi Corporation
        email                : yoichi.kayama@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Y.Kayama/Aeroasahi Corporation'
__date__ = '2021-09-27'
__copyright__ = '(C) 2021 by Y.Kayama/Aeroasahi Corporation'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

import json 
from  .jpmeshmain  import  generate_meshes

#from  .japanmesh\main  import  generate_meshes



from qgis.PyQt.QtCore import ( QCoreApplication ,
                           QVariant)

from qgis.core import (QgsProcessing,
                       QgsFeatureSink,
                       QgsProcessingAlgorithm,
                       QgsProcessingParameterFeatureSource,
                       QgsProcessingParameterFeatureSink,
                       QgsProcessingParameterExtent,
                       QgsProcessingParameterProviderConnection,
                       QgsProcessingParameterDatabaseSchema,
                       QgsProcessingParameterDatabaseTable,
                       QgsProcessingParameterBoolean,
                       QgsProcessingParameterEnum,
                       QgsWkbTypes,
                       QgsCoordinateReferenceSystem,
                       QgsFields,
                       QgsField,
                       QgsFeature,
                       QgsGeometry,
                       QgsPointXY,
                       QgsProviderRegistry,
                       QgsProviderConnectionException,
                       QgsProcessingException,
                       QgsProcessingParameterField)


class  CreateMeshCodeAlgorithm(QgsProcessingAlgorithm):
    """
    This is an example algorithm that takes a vector layer and
    creates a new identical one.

    It is meant to be used as an example of how to create your own
    algorithms and explain methods and variables used to do it. An
    algorithm like this will be available in all elements, and there
    is not need for additional work.

    All Processing algorithms should extend the QgsProcessingAlgorithm
    class.
    """

    # Constants used to refer to parameters and outputs. They will be
    # used when calling the algorithm from another algorithm, or when
    # calling from the QGIS console.

    OUTPUT = 'OUTPUT'
    EXTENT = 'EXTENT'
    LEVEL = 'LEVEL'
    #APPEND = 'APPEND'


    def initAlgorithm(self, config):
        """
        Here we define the inputs and output of the algorithm, along
        with some other properties.
        """

        # We add the input vector features source. It can have any kind of
        # geometry.
        self.addParameter(
            QgsProcessingParameterExtent(
                self.EXTENT,
                self.tr('extent')
            )
        )

        self.addParameter(
        QgsProcessingParameterEnum(
            self.LEVEL,
            self.tr('Mesh level'),
            ["1次メッシュ", "2次メッシュ","3次メッシュ","500mメッシュ","250mメッシュ","125mメッシュ","100mメッシュ","50mメッシュ","10mメッシュ","5mメッシュ"]
            )
        )

        #self.addParameter(QgsProcessingParameterBoolean(self.APPEND,
       #                                                 self.tr('append'), True))

        # We add a feature sink in which to store our processed features (this
        # usually takes the form of a newly created vector layer when the
        # algorithm is run in QGIS).
        sinkp =    QgsProcessingParameterFeatureSink(
                self.OUTPUT,
                self.tr('Output')
            )

        sinkp.setSupportsAppend( True )
        self.addParameter(
             sinkp
        )
        

    def processAlgorithm(self, parameters, context, feedback):
        """
        Here is where the processing itself takes place.
        """

        extent = self.parameterAsExtent(parameters, self.EXTENT , context)

        level = self.parameterAsInt(parameters, self.LEVEL , context)

        #append = self.parameterAsBoolean(parameters, self.APPEND, context)

        ext = [[float(extent.xMinimum ()) ,float(extent.yMinimum ())] ,[float(extent.xMaximum()) ,float(extent.yMaximum())] ]

      
        print(level)
        print(extent)
        # Return the results of the algorithm. In this case our only result is
        # the feature sink which contains the processed features, but some
        # algorithms may return multiple feature sinks, calculated numeric
        # statistics, etc. These should all be included in the returned
        # dictionary, with keys matching the feature corresponding parameter
        # or output names.

        fields = QgsFields()
        fields.append(QgsField("code", QVariant.String))
        fields.append(QgsField("exmin", QVariant.Double))
        fields.append(QgsField("eymin", QVariant.Double))
        fields.append(QgsField("exmax", QVariant.Double))
        fields.append(QgsField("eymax", QVariant.Double))
                        
        crs = QgsCoordinateReferenceSystem("EPSG:6668")
        (sink, dest_id) = self.parameterAsSink(parameters, self.OUTPUT,
                context, fields , QgsWkbTypes.NoGeometry , crs)

        # Compute the number of steps to display within the progress bar and
        # get features from source
        for cmesh in generate_meshes( level+1,ext):
            if feedback.isCanceled():
                break
            #print( cmesh['geometry'] )
            #feature = json.load( cmesh )
            fet = QgsFeature(fields)

            fet["code"] = cmesh['code']   
            fet["exmin"] = cmesh['geometry'][0][0][0] 
            fet["eymin"] = cmesh['geometry'][0][0][1]   
            fet["exmax"] = cmesh['geometry'][0][3][0] 
            fet["eymax"] = cmesh['geometry'][0][2][1]  

            #Polygon1 = QgsGeometry.fromPolygonXY([[QgsPointXY(cmesh['geometry'][0][0][0],cmesh['geometry'][0][0][1]),
            #                            QgsPointXY( cmesh['geometry'][0][1][0],cmesh['geometry'][0][1][1]),
            #                              QgsPointXY( cmesh['geometry'][0][2][0],cmesh['geometry'][0][2][1]),
            #                                QgsPointXY( cmesh['geometry'][0][3][0],cmesh['geometry'][0][3][1]),
            #                                  QgsPointXY( cmesh['geometry'][0][4][0],cmesh['geometry'][0][4][1])] ])

                               

            #fet.setGeometry(Polygon1)
                                        
            #print( feature )
            sink.addFeature(fet, QgsFeatureSink.FastInsert)

        #total = 100.0 / source.featureCount() if source.featureCount() else 0
        #features = source.getFeatures()

        #for current, feature in enumerate(features):
            # Stop the algorithm if cancel button has been clicked
        #    if feedback.isCanceled():
         #       break

            # Add a feature in the sink
         #   sink.addFeature(feature, QgsFeatureSink.FastInsert)

            # Update the progress bar
        #    feedback.setProgress(int(current * total))
        #"""
        # Return the results of the algorithm. In this case our only result is
        # the feature sink which contains the processed features, but some
        # algorithms may return multiple feature sinks, calculated numeric
        # statistics, etc. These should all be included in the returned
        # dictionary, with keys matching the feature corresponding parameter
        # or output names.
        return {self.OUTPUT: dest_id}
        #return {self.OUTPUT: dest_id}
        #return {"sample"}

    def name(self):
        """
        Returns the algorithm name, used for identifying the algorithm. This
        string should be fixed for the algorithm, and must not be localised.
        The name should be unique within each provider. Names should contain
        lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'CreateMeshCodeAlgorithm'

    def displayName(self):
        """
        Returns the translated algorithm name, which should be used for any
        user-visible display of the algorithm name.
        """
        return self.tr(self.name())

    def group(self):
        """
        Returns the name of the group this algorithm belongs to. This string
        should be localised.
        """
        return self.tr(self.groupId())

    def groupId(self):
        """
        Returns the unique ID of the group this algorithm belongs to. This
        string should be fixed for the algorithm, and must not be localised.
        The group id should be unique within each provider. Group id should
        contain lowercase alphanumeric characters only and no spaces or other
        formatting characters.
        """
        return 'メッシュ'

    def tr(self, string):
        return QCoreApplication.translate('Processing', string)

    def createInstance(self):
        return  CreateMeshCodeAlgorithm()
