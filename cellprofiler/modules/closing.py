# -*- coding: utf-8 -*-

"""

<strong>Closing</strong> is the erosion of the dilation of an image. It’s used to remove pepper noise.

"""

import numpy
import skimage.morphology

import cellprofiler.image
import cellprofiler.module
import cellprofiler.setting


class Closing(cellprofiler.module.ImageProcessing):
    category = "Mathematical morphology"

    module_name = "Closing"

    variable_revision_number = 1

    def create_settings(self):
        super(Closing, self).create_settings()

        self.structuring_element = cellprofiler.setting.StructuringElement()

    def settings(self):
        __settings__ = super(Closing, self).settings()

        return __settings__ + [
            self.structuring_element
        ]

    def visible_settings(self):
        __settings__ = super(Closing, self).settings()

        return __settings__ + [
            self.structuring_element
        ]

    def run(self, workspace):
        x = workspace.image_set.get_image(self.x_name.value)

        if self.structuring_element.value.ndim == 2 and x.volumetric:
            self.function = planewise_closing
        elif x.pixel_data.dtype == numpy.bool:
            self.function = skimage.morphology.binary_closing
        else:
            self.function = skimage.morphology.closing

        super(Closing, self).run(workspace)


def planewise_closing(data, selem):
    if data.dtype == numpy.bool:
        function = skimage.morphology.binary_closing

        closed = numpy.zeros_like(data, dtype=numpy.bool)
    else:
        function = skimage.morphology.closing

        closed = numpy.zeros_like(data)

    for index, plane in enumerate(data):
        closed[index] = function(plane, selem)

    return closed
