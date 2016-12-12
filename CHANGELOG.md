# Change Log

## [Unreleased]
### Added
- Open volumes and assign names to loaded volumes.
- Visualize volumes and segmentation of volumes.
- Support for loading `.dm4` files by [@magnunor](https://github.com/magnunor).
- Image processing modules: 
    - GammaCorrection
    - GaussianFilter
    - HistogramEqualization
    - ImageGradient
    - LaplacianOfGaussian
    - MedianFilter
    - NoiseReduction
    - Thresholding
- Feature detection modules: 
    - BlobDetection
    - EdgeDetection
- Mathematical morphology modules: 
    - Closing
    - Dilation
    - Erosion
    - MedialAxis
    - Opening
- Image segmentation modules:
    - ActiveContourModel
    - RandomWalker
    - Watershed

### Changed
- Generalize image and object classes to support volumes.
- Volumetric support for:
    - ConvertObjectsToImage
    - MeasureImageIntensity
- Decouple GUI from core modules.
- Make image and object classes more pythonic with implicit getters and setters.

### Deprecated
-- none --

### Removed
- Outdated modules:
    - CreateWebPage
    - InputExternal
    - OutputExternal
    - SendEmail
- Memoization and HDF5 caching.

### Fixed
- Document artifacting in IdentifyPrimaryObjects by [@AnneCarpenter](https://github.com/AnneCarpenter).
- Calculate Zernike features only when prompted by [@tomgreen66](https://github.com/tomgreen66).
- Documentation enhancement for PlateViewer by [@bethac07](https://github.com/bethac07).
- Re-expose option for alternate colormaps in 8-bit images by [@bethac07](https://github.com/bethac07).
- Correct radian conversion in IdentifyDeadWorms by [@bethac07](https://github.com/bethac07).

### Security
-- none --