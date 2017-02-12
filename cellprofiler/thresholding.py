import centrosome.otsu
import centrosome.threshold
import numpy
import skimage.filters
import skimage.filters.rank
import skimage.morphology


def otsu(image):
    data = image.pixel_data

    mask = image.mask

    if numpy.all(data[mask] == data[mask][0]):
        return data[mask][0]

    return skimage.filters.threshold_otsu(data[mask])


def otsu3(image):
    data = image.pixel_data[image.mask]

    data, d = centrosome.threshold.log_transform(data)

    lower, upper = centrosome.otsu.otsu3(image.pixel_data[image.mask])

    lower = centrosome.threshold.inverse_log_transform(lower, d)

    upper = centrosome.threshold.inverse_log_transform(upper, d)

    return lower, upper


def local_otsu(image, block_size):
    data = skimage.img_as_ubyte(image.pixel_data)

    selem = skimage.morphology.square(block_size)

    if image.volumetric:
        threshold = numpy.zeros_like(data)

        for index, plane in enumerate(data):
            threshold[index] = skimage.filters.rank.otsu(plane, selem, mask=image.mask[index])
    else:
        threshold = skimage.filters.rank.otsu(data, selem, mask=image.mask)

    return skimage.img_as_float(threshold)


def local_otsu3(image, block_size):
    assert block_size % 2 == 1, "block_size must be odd, got {}".format(block_size)

    data = image.pixel_data

    data[~image.mask] = 0

    data, d = centrosome.threshold.log_transform(data)

    if image.volumetric:
        lower = numpy.zeros_like(data)

        upper = numpy.zeros_like(data)

        for index, plane in enumerate(data):
            lower = skimage.filters.threshold_local(
                plane,
                block_size,
                method="generic",
                param=lambda x: centrosome.otsu.otsu3(x)[0]
            )

            upper = skimage.filters.threshold_local(
                plane,
                block_size,
                method="generic",
                param=lambda x: centrosome.otsu.otsu3(x)[1]
            )
    else:
        lower = skimage.filters.threshold_local(
            data,
            block_size,
            method="generic",
            param=lambda x: centrosome.otsu.otsu3(x)[0]
        )

        upper = skimage.filters.threshold_local(
            data,
            block_size,
            method="generic",
            param=lambda x: centrosome.otsu.otsu3(x)[1]
        )

    lower = centrosome.threshold.inverse_log_transform(lower, d)

    upper = centrosome.threshold.inverse_log_transform(upper, d)

    return lower, upper
