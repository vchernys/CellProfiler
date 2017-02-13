import cellprofiler.image
import cellprofiler.thresholding
import centrosome.threshold
import numpy
import numpy.random
import numpy.testing
import pytest


numpy.random.seed(73)


def test_otsu_zeros():
    image = cellprofiler.image.Image(numpy.zeros((10, 10), dtype=numpy.float32))

    threshold = cellprofiler.thresholding.otsu(image)

    assert threshold == 0.0


def test_otsu_masked_zeros():
    data = numpy.random.rand(10, 10)

    data[2:5, 2:5] = 0.0

    mask = numpy.zeros_like(data, dtype=numpy.bool)

    mask[2:5, 2:5] = True

    image = cellprofiler.image.Image(data, mask=mask)

    threshold = cellprofiler.thresholding.otsu(image)

    assert threshold == 0.0


def test_otsu_image():
    data = numpy.random.rand(10, 10)

    image = cellprofiler.image.Image(data)

    threshold = cellprofiler.thresholding.otsu(image)

    assert threshold >= 0.0

    assert threshold <= 1.0


def test_otsu_volume():
    data = numpy.random.rand(10, 10, 10)

    image = cellprofiler.image.Image(data, dimensions=3)

    threshold = cellprofiler.thresholding.otsu(image)

    assert threshold >= 0.0

    assert threshold <= 1.0


def test_local_otsu_image_zeros():
    image = cellprofiler.image.Image(numpy.zeros((10, 10), dtype=numpy.float32))

    threshold = cellprofiler.thresholding.local_otsu(image, 3)

    assert numpy.all(threshold == 0.0)


def test_local_otsu_masked_image_zeros():
    data = numpy.random.rand(10, 10)

    data[2:5, 2:5] = 0.0

    mask = numpy.zeros_like(data, dtype=numpy.bool)

    mask[2:5, 2:5] = True

    image = cellprofiler.image.Image(data, mask=mask)

    threshold = cellprofiler.thresholding.local_otsu(image, 3)

    assert numpy.all(threshold == 0.0)


def test_local_otsu_image():
    data = numpy.random.rand(10, 10)

    image = cellprofiler.image.Image(data)

    threshold = cellprofiler.thresholding.local_otsu(image, 3)

    assert numpy.all(threshold >= 0.0)

    assert numpy.all(threshold <= 1.0)


def test_local_otsu_volume():
    data = numpy.random.rand(10, 10, 10)

    image = cellprofiler.image.Image(data, dimensions=3)

    threshold = cellprofiler.thresholding.local_otsu(image, 3)

    assert numpy.all(threshold >= 0.0)

    assert numpy.all(threshold <= 1.0)


def test_otsu3_zeros():
    image = cellprofiler.image.Image(numpy.zeros((10, 10), dtype=numpy.float32))

    lower, upper = cellprofiler.thresholding.otsu3(image)

    numpy.testing.assert_almost_equal(lower, 0.0, decimal=5)

    numpy.testing.assert_almost_equal(upper, 0.0, decimal=5)


def test_otsu3_masked_zeros():
    data = numpy.random.rand(10, 10)

    data[2:5, 2:5] = 0.0

    mask = numpy.zeros_like(data, dtype=numpy.bool)

    mask[2:5, 2:5] = True

    image = cellprofiler.image.Image(data, mask=mask)

    lower, upper = cellprofiler.thresholding.otsu3(image)

    numpy.testing.assert_almost_equal(lower, 0.0, decimal=5)

    numpy.testing.assert_almost_equal(upper, 0.0, decimal=5)


def test_otsu3_image():
    data = numpy.random.rand(10, 10)

    image = cellprofiler.image.Image(data)

    lower, upper = cellprofiler.thresholding.otsu3(image)

    assert lower >= 0.0

    assert upper >= 0.0

    assert lower <= 1.0

    assert upper <= 1.0


def test_otsu3_volume():
    data = numpy.random.rand(10, 10, 10)

    image = cellprofiler.image.Image(data, dimensions=3)

    lower, upper = cellprofiler.thresholding.otsu3(image)

    assert lower >= 0.0

    assert upper >= 0.0

    assert lower <= 1.0

    assert upper <= 1.0


def test_local_otsu3_even_block_size():
    image = cellprofiler.image.Image(numpy.zeros((10, 10), dtype=numpy.float32))

    with pytest.raises(AssertionError) as error:
        cellprofiler.thresholding.local_otsu3(image, 2)

    assert "block_size must be odd, got 2" in str(error.value)


def test_local_otsu3_zeros():
    image = cellprofiler.image.Image(numpy.zeros((10, 10), dtype=numpy.float32))

    lower, upper = cellprofiler.thresholding.local_otsu3(image, 3)

    numpy.testing.assert_almost_equal(lower, 0.0, decimal=5)

    numpy.testing.assert_almost_equal(upper, 0.0, decimal=5)


def test_local_otsu3_masked_zeros():
    data = numpy.random.rand(10, 10)

    data[2:5, 2:5] = 0.0

    mask = numpy.zeros_like(data, dtype=numpy.bool)

    mask[2:5, 2:5] = True

    image = cellprofiler.image.Image(data, mask=mask)

    lower, upper = cellprofiler.thresholding.local_otsu3(image, 3)

    numpy.testing.assert_almost_equal(lower, 0.0, decimal=5)

    numpy.testing.assert_almost_equal(upper, 0.0, decimal=5)


def test_local_otsu3_image():
    data = numpy.random.rand(10, 10)

    image = cellprofiler.image.Image(data)

    lower, upper = cellprofiler.thresholding.local_otsu3(image, 3)

    assert numpy.all(lower >= 0.0)

    assert numpy.all(upper >= 0.0)

    assert numpy.all(lower <= 1.0)

    assert numpy.all(upper <= 1.0)


def test_local_otsu3_volume():
    data = numpy.random.rand(10, 10, 10)

    image = cellprofiler.image.Image(data, dimensions=3)

    lower, upper = cellprofiler.thresholding.local_otsu3(image, 3)

    assert numpy.all(lower >= 0.0)

    assert numpy.all(upper >= 0.0)

    assert numpy.all(lower <= 1.0)

    assert numpy.all(upper <= 1.0)


def test_robust_background_image_mean():
    data = numpy.random.rand(10, 10)

    image = cellprofiler.image.Image(data)

    threshold = cellprofiler.thresholding.robust_background(
        image,
        average_method="mean"
    )

    expected = centrosome.threshold.get_robust_background_threshold(
        data,
        mask=numpy.ones_like(data, dtype=numpy.bool),
        lower_outlier_fraction=0.05,
        upper_outlier_fraction=0.05,
        deviations_above_average=2,
        average_fn=numpy.mean,
        variance_fn=numpy.std
    )

    numpy.testing.assert_almost_equal(threshold, expected)


def test_robust_background_image_median():
    data = numpy.random.rand(10, 10)

    image = cellprofiler.image.Image(data)

    threshold = cellprofiler.thresholding.robust_background(
        image,
        average_method="median"
    )

    expected = centrosome.threshold.get_robust_background_threshold(
        data,
        mask=numpy.ones_like(data, dtype=numpy.bool),
        lower_outlier_fraction=0.05,
        upper_outlier_fraction=0.05,
        deviations_above_average=2,
        average_fn=numpy.median,
        variance_fn=numpy.std
    )

    numpy.testing.assert_almost_equal(threshold, expected)


def test_robust_background_image_mode():
    data = numpy.random.rand(10, 10)

    image = cellprofiler.image.Image(data)

    threshold = cellprofiler.thresholding.robust_background(
        image,
        average_method="mode"
    )

    expected = centrosome.threshold.get_robust_background_threshold(
        data,
        mask=numpy.ones_like(data, dtype=numpy.bool),
        lower_outlier_fraction=0.05,
        upper_outlier_fraction=0.05,
        deviations_above_average=2,
        average_fn=centrosome.threshold.binned_mode,
        variance_fn=numpy.std
    )

    numpy.testing.assert_almost_equal(threshold, expected)


def test_robust_background_image_sd():
    data = numpy.random.rand(10, 10)

    image = cellprofiler.image.Image(data)

    threshold = cellprofiler.thresholding.robust_background(
        image,
        variance_method="sd"
    )

    expected = centrosome.threshold.get_robust_background_threshold(
        data,
        mask=numpy.ones_like(data, dtype=numpy.bool),
        lower_outlier_fraction=0.05,
        upper_outlier_fraction=0.05,
        deviations_above_average=2,
        average_fn=numpy.mean,
        variance_fn=numpy.std
    )

    numpy.testing.assert_almost_equal(threshold, expected)


def test_robust_background_image_mad():
    data = numpy.random.rand(10, 10)

    image = cellprofiler.image.Image(data)

    threshold = cellprofiler.thresholding.robust_background(
        image,
        variance_method="mad"
    )

    expected = centrosome.threshold.get_robust_background_threshold(
        data,
        mask=numpy.ones_like(data, dtype=numpy.bool),
        lower_outlier_fraction=0.05,
        upper_outlier_fraction=0.05,
        deviations_above_average=2,
        average_fn=numpy.mean,
        variance_fn=centrosome.threshold.mad
    )

    numpy.testing.assert_almost_equal(threshold, expected)


def test_robust_background_volume_mean():
    data = numpy.random.rand(10, 10, 10)

    image = cellprofiler.image.Image(data, dimensions=3)

    threshold = cellprofiler.thresholding.robust_background(
        image,
        average_method="mean"
    )

    expected = centrosome.threshold.get_robust_background_threshold(
        data,
        mask=numpy.ones_like(data, dtype=numpy.bool),
        lower_outlier_fraction=0.05,
        upper_outlier_fraction=0.05,
        deviations_above_average=2,
        average_fn=numpy.mean,
        variance_fn=numpy.std
    )

    numpy.testing.assert_almost_equal(threshold, expected)


def test_robust_background_volume_median():
    data = numpy.random.rand(10, 10, 10)

    image = cellprofiler.image.Image(data, dimensions=3)

    threshold = cellprofiler.thresholding.robust_background(
        image,
        average_method="median"
    )

    expected = centrosome.threshold.get_robust_background_threshold(
        data,
        mask=numpy.ones_like(data, dtype=numpy.bool),
        lower_outlier_fraction=0.05,
        upper_outlier_fraction=0.05,
        deviations_above_average=2,
        average_fn=numpy.median,
        variance_fn=numpy.std
    )

    numpy.testing.assert_almost_equal(threshold, expected)


def test_robust_background_volume_mode():
    data = numpy.random.rand(10, 10, 10)

    image = cellprofiler.image.Image(data, dimensions=3)

    threshold = cellprofiler.thresholding.robust_background(
        image,
        average_method="mode"
    )

    expected = centrosome.threshold.get_robust_background_threshold(
        data,
        mask=numpy.ones_like(data, dtype=numpy.bool),
        lower_outlier_fraction=0.05,
        upper_outlier_fraction=0.05,
        deviations_above_average=2,
        average_fn=centrosome.threshold.binned_mode,
        variance_fn=numpy.std
    )

    numpy.testing.assert_almost_equal(threshold, expected)


def test_robust_background_volume_sd():
    data = numpy.random.rand(10, 10, 10)

    image = cellprofiler.image.Image(data, dimensions=3)

    threshold = cellprofiler.thresholding.robust_background(
        image,
        variance_method="sd"
    )

    expected = centrosome.threshold.get_robust_background_threshold(
        data,
        mask=numpy.ones_like(data, dtype=numpy.bool),
        lower_outlier_fraction=0.05,
        upper_outlier_fraction=0.05,
        deviations_above_average=2,
        average_fn=numpy.mean,
        variance_fn=numpy.std
    )

    numpy.testing.assert_almost_equal(threshold, expected)


def test_robust_background_volume_mad():
    data = numpy.random.rand(10, 10, 10)

    image = cellprofiler.image.Image(data, dimensions=3)

    threshold = cellprofiler.thresholding.robust_background(
        image,
        variance_method="mad"
    )

    expected = centrosome.threshold.get_robust_background_threshold(
        data,
        mask=numpy.ones_like(data, dtype=numpy.bool),
        lower_outlier_fraction=0.05,
        upper_outlier_fraction=0.05,
        deviations_above_average=2,
        average_fn=numpy.mean,
        variance_fn=centrosome.threshold.mad
    )

    numpy.testing.assert_almost_equal(threshold, expected)
