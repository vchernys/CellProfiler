# -*- coding: utf-8 -*-

"""

<strong>Opening</strong> is the dilation of the erosion of an image. It’s used to remove salt noise.

"""

import numpy
import skimage.morphology

import cellprofiler.image
import cellprofiler.module
import cellprofiler.setting


class Opening(cellprofiler.module.ImageProcessing):
    category = "Mathematical morphology"

    module_name = "Opening"

    variable_revision_number = 1

    def create_settings(self):
        super(Opening, self).create_settings()

        self.structuring_element = cellprofiler.setting.StructuringElement()

    def settings(self):
        __settings__ = super(Opening, self).settings()

        return __settings__ + [
            self.structuring_element
        ]

    def visible_settings(self):
        __settings__ = super(Opening, self).settings()

        return __settings__ + [
            self.structuring_element
        ]

    def run(self, workspace):
        x = workspace.image_set.get_image(self.x_name.value)

        if self.structuring_element.value.ndim == 2 and x.volumetric:
            self.function = planewise_opening
        elif x.pixel_data.dtype == numpy.bool:
            self.function = skimage.morphology.binary_opening
        else:
            self.function = skimage.morphology.opening

        super(Opening, self).run(workspace)


def planewise_opening(data, selem):
    if data.dtype == numpy.bool:
        function = skimage.morphology.binary_opening

        opened = numpy.zeros_like(data, dtype=numpy.bool)
    else:
        function = skimage.morphology.opening

        opened = numpy.zeros_like(data)

    for index, plane in enumerate(data):
        opened[index] = function(plane, selem)

    return opened