import centrosome.otsu
import centrosome.threshold
import numpy
import scipy.interpolate
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

    lower, upper = centrosome.otsu.otsu3(data)

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
    data = image.pixel_data

    if image.volumetric:
        lower = numpy.zeros_like(data)

        upper = numpy.zeros_like(data)

        for index, plane in enumerate(data):
            lower[index], upper[index] = _local_otsu3(plane, image.mask[index], block_size)
    else:
        lower, upper = _local_otsu3(data, image.mask, block_size)

    return lower, upper


def _local_otsu3(data, mask, block_size):
    image_size = numpy.array(data.shape, dtype=int)

    nblocks = image_size / block_size

    increment = (numpy.array(image_size, dtype=float) / numpy.array(nblocks, dtype=float))

    lower_block_threshold = numpy.zeros([nblocks[0], nblocks[1]], dtype=data.dtype)

    upper_block_threshold = numpy.zeros([nblocks[0], nblocks[1]], dtype=data.dtype)

    for i in range(nblocks[0]):
        i0 = int(i * increment[0])

        i1 = int((i + 1) * increment[0])

        for j in range(nblocks[1]):
            j0 = int(j * increment[1])

            j1 = int((j + 1) * increment[1])

            block = data[i0:i1, j0:j1]

            block_mask = mask[i0:i1, j0:j1]

            if len(block[block_mask]) == 0:
                lower_block_threshold[i, j] = upper_block_threshold[i, j] = 0.0

                continue

            block_data, d = centrosome.threshold.log_transform(block[block_mask])

            lower, upper = centrosome.otsu.otsu3(block_data)

            lower_block_threshold[i, j] = centrosome.threshold.inverse_log_transform(lower, d)

            upper_block_threshold[i, j] = centrosome.threshold.inverse_log_transform(upper, d)

    spline_order = min(3, numpy.min(nblocks) - 1)

    x_start = int(increment[0] / 2)

    x_end = int((nblocks[0] - 0.5) * increment[0])

    y_start = int(increment[1] / 2)

    y_end = int((nblocks[1] - 0.5) * increment[1])

    xt_start = .5

    xt_end = data.shape[0] - .5

    yt_start = .5

    yt_end = data.shape[1] - .5

    block_x_coords = numpy.linspace(x_start, x_end, nblocks[0])

    block_y_coords = numpy.linspace(y_start, y_end, nblocks[1])

    lower_adaptive_interpolation = scipy.interpolate.RectBivariateSpline(
        block_x_coords,
        block_y_coords,
        lower_block_threshold,
        bbox=(xt_start, xt_end, yt_start, yt_end),
        kx=spline_order,
        ky=spline_order
    )

    upper_adaptive_interpolation = scipy.interpolate.RectBivariateSpline(
        block_x_coords,
        block_y_coords,
        upper_block_threshold,
        bbox=(xt_start, xt_end, yt_start, yt_end),
        kx=spline_order,
        ky=spline_order
    )

    thresh_out_x_coords = numpy.linspace(.5, int(nblocks[0] * increment[0]) - .5, data.shape[0])

    thresh_out_y_coords = numpy.linspace(.5, int(nblocks[1] * increment[1]) - .5, data.shape[1])

    lower_thresh_out = lower_adaptive_interpolation(thresh_out_x_coords, thresh_out_y_coords)

    upper_thresh_out = upper_adaptive_interpolation(thresh_out_x_coords, thresh_out_y_coords)

    for thresh in (lower_thresh_out, upper_thresh_out):
        thresh[thresh < 0.0] = 0.0

        thresh[thresh > 1.0] = 1.0

    return lower_thresh_out, upper_thresh_out


def robust_background(image, lower=0.05, upper=0.05, average_method="mean", variance_method="sd", n_deviations=2):
    average_fn = {
        "mean": numpy.mean,
        "median": numpy.median,
        "mode": centrosome.threshold.binned_mode
    }.get(average_method, numpy.mean)

    variance_fn = {
        "sd": numpy.std,
        "mad": centrosome.threshold.mad
    }.get(variance_method, numpy.std)

    return centrosome.threshold.get_robust_background_threshold(
        image.pixel_data,
        mask=image.mask,
        lower_outlier_fraction=lower,
        upper_outlier_fraction=upper,
        deviations_above_average=n_deviations,
        average_fn=average_fn,
        variance_fn=variance_fn
    )


def minimum_cross_entropy(image):
    data = image.pixel_data

    mask = image.mask

    if numpy.all(data[mask] == data[mask][0]):
        return data[mask][0]

    return skimage.filters.threshold_li(data[mask])