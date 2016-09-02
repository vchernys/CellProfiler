"""<b>ImageTemplate</b> - an example image processing module
<hr>
This is an example of a module that takes one image as an input and
produces a second image for downstream processing. You can use this as
a starting point for your own module: rename this file and put it in your
plugins directory.

The text you see here will be displayed as the help for your module. You
can use HTML markup here and in the settings text; the Python HTML control
does not fully support the HTML specification, so you may have to experiment
to get it to display correctly.

In this example, we'll create a module that performs a morphological operation
(closing, dilation, erosion, opening) on an image.
"""

# List the libraries this module uses at the top of the file.
# Add imports as you need them while you're developing this module.
# Remove any unused imports when you're finished developing.
import cellprofiler.image
import cellprofiler.module
import cellprofiler.setting
import skimage.morphology


# All modules inherit from cellprofiler.module.Module, which defines the base functionality of all modules.
# Some functionality is specific to this module, and we'll define it in the methods below.
class ImageTemplate(cellprofiler.module.Module):
    # A module starts by declaring the following information:
    #
    #   module_name: name used for display in the CellProfiler GUI
    #   category: the category under which this module can be found
    #   variable_revision_number: the latest version of this module
    #
    # The variable revision number starts at 1 and must be incremented whenever your module is modified.
    module_name = "ImageTemplate"
    category = "Image Processing"
    variable_revision_number = 1

    # Declare user interface selements (called "settings").
    # Every setting your module uses must be declared here.
    # You can look at other modules and in cellprofiler.settings for other available settings.
    def create_settings(self):
        # Most CellProfiler settings have use the following structure:
        #
        #   self.option = cellprofiler.setting.SettingType(
        #     text="Text briefly describing this setting",
        #     value=some_value,
        #     doc="""Helpful information about this setting."""
        #   )
        #
        # where:
        #    self.option: saves the setting as the variable self.option which you can reference in other methods.
        #    cellprofiler.setting.SettingType: is the type of setting (e.g., cellprofiler.setting.Choice).
        #    some_value: is the initial value of the setting. Usually this is optional but can be used to set defaults.
        #
        # This module uses a few very common settings. We describe how to use them below.

        # Image processing modules need an image to process.
        # Use cellprofiler.setting.ImageNameSubscriber to provide users with a list of names of available images.
        # The list of names is automatically generated based on earlier modules.
        # The selected name is the name of the image this module will process.
        self.input_image_name = cellprofiler.setting.ImageNameSubscriber(
            "Input image name",
            doc="""This is the image that the module operates on. You can
            choose any image that is made available by a prior module.
            <br>
            <b>ImageTemplate</b> will do something to this image.
            """
        )

        #
        # The ImageNameProvider makes the image available to subsequent
        # modules.
        #
        self.output_image_name = cellprofiler.setting.ImageNameProvider(
            "Output image name",
            # The second parameter holds a suggested name for the image.
            "OutputImage",
            doc="""This is the image resulting from the operation."""
        )

        self.operation = cellprofiler.setting.Choice(
            "Operation",
            [
                "closing",
                "dilation",
                "erosion",
                "opening"
            ]
        )

        self.structuring_element = cellprofiler.setting.StructuringElement()

    #
    # The "settings" method tells CellProfiler about the settings you
    # have in your module. CellProfiler uses the list for saving
    # and restoring values for your module when it saves or loads a
    # pipeline file.
    #
    def settings(self):
        return [
            self.input_image_name,
            self.output_image_name,
            self.operation,
            self.structuring_element
        ]

    #
    # visible_settings tells CellProfiler which settings should be
    # displayed and in what order.
    #
    # You don't have to implement "visible_settings" - if you delete
    # visible_settings, CellProfiler will use "settings" to pick settings
    # for display.
    #
    def visible_settings(self):
        return [
            self.input_image_name,
            self.output_image_name,
            self.operation,
            self.structuring_element
        ]

    #
    # CellProfiler calls "run" on each image set in your pipeline.
    # This is where you do the real work.
    #
    def run(self, workspace):
        #
        # Get the input and output image names. You need to get the .value
        # because otherwise you'll get the setting object instead of
        # the string name.
        #
        input_image_name = self.input_image_name.value

        output_image_name = self.output_image_name.value

        operation = self.operation.value

        structuring_element = self.structuring_element.value

        #
        # Get the image set. The image set has all of the images in it.
        #
        image_set = workspace.image_set

        #
        # Get the input image object. We want a grayscale image here.
        # The image set will convert a color image to a grayscale one
        # and warn the user.
        #
        input_image = image_set.get_image(input_image_name, must_be_grayscale=True)

        #
        # Get the pixels - these are a 2-d Numpy array.
        #
        pixels = input_image.pixel_data

        if operation == "closing":
            output_pixels = skimage.morphology.closing(pixels, structuring_element)
        elif operation == "dilation":
            output_pixels = skimage.morphology.dilation(pixels, structuring_element)
        elif operation == "erosion":
            output_pixels = skimage.morphology.erosion(pixels, structuring_element)
        else:
            output_pixels = skimage.morphology.opening(pixels, structuring_element)

        #
        # Make an image object. It's nice if you tell CellProfiler
        # about the parent image - the child inherits the parent's
        # cropping and masking, but it's not absolutely necessary
        #
        output_image = cellprofiler.image.Image(output_pixels, parent_image=input_image)

        image_set.add(output_image_name, output_image)

        #
        # Save intermediate results for display if the window frame is on
        #
        if self.show_window:
            workspace.display_data.input_pixels = pixels

            workspace.display_data.output_pixels = output_pixels

    #
    # display lets you use matplotlib to display your results.
    #
    def display(self, workspace, figure):
        #
        # the "figure" is really the frame around the figure. You almost always
        # use figure.subplot or figure.subplot_imshow to get axes to draw on
        # so we pretty much ignore the figure.
        #
        figure = workspace.create_or_find_figure(subplots=(3, 1))

        #
        # Show the user the input image
        #
        figure.subplot_imshow_grayscale(
            0,
            0,
            workspace.display_data.input_pixels,
            title=self.input_image_name.value
        )

        lead_subplot = figure.subplot(0, 0)

        #
        # Show the user the final image
        #
        figure.subplot_imshow_grayscale(
            2,
            0,
            workspace.display_data.output_pixels,
            title=self.output_image_name.value,
            sharex=lead_subplot,
            sharey=lead_subplot
        )
