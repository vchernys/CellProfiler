# Changelog

## [Unreleased]
### Added
- [2169](https://github.com/CellProfiler/CellProfiler/pull/2326) GammaCorrection. ([2371](https://github.com/CellProfiler/CellProfiler/pull/2371))
- [2170](https://github.com/CellProfiler/CellProfiler/pull/2325) HistogramEqualization.
- [2171](https://github.com/CellProfiler/CellProfiler/pull/2328) MedianFilter.
- [2172](https://github.com/CellProfiler/CellProfiler/pull/2332) NoiseReduction.
- [2177](https://github.com/CellProfiler/CellProfiler/pull/2329) Thresholding. Also introduces an odd integer setting. ([2414](https://github.com/CellProfiler/CellProfiler/pull/2415))
- [2179](https://github.com/CellProfiler/CellProfiler/pull/2189) Support loading `.dm4` files by [@magnunor](https://github.com/magnunor).
- [2250](https://github.com/CellProfiler/CellProfiler/pull/2322) Visualize a volume. ([2412](https://github.com/CellProfiler/CellProfiler/pull/2413), [2436](https://github.com/CellProfiler/CellProfiler/pull/2437), [2512](https://github.com/CellProfiler/CellProfiler/pull/2513))
- [2306](https://github.com/CellProfiler/CellProfiler/pull/2398) BlobDetection.
- [2266](https://github.com/CellProfiler/CellProfiler/pull/2280) Introduce a structuring element setting. ([2348](https://github.com/CellProfiler/CellProfiler/pull/2433))
- [2314](https://github.com/CellProfiler/CellProfiler/pull/2324) Erosion.
- [2316](https://github.com/CellProfiler/CellProfiler/pull/2327) Dilation.
- [2317](https://github.com/CellProfiler/CellProfiler/pull/2331) Closing.
- [2318](https://github.com/CellProfiler/CellProfiler/pull/2330) Opening.
- [2319](https://github.com/CellProfiler/CellProfiler/pull/2323) ImageGradient.
- [2321](https://github.com/CellProfiler/CellProfiler/pull/2336) Watershed. ([2405](https://github.com/CellProfiler/CellProfiler/pull/2409), [2411](https://github.com/CellProfiler/CellProfiler/pull/2417), [2421](https://github.com/CellProfiler/CellProfiler/pull/2422), [2429](https://github.com/CellProfiler/CellProfiler/pull/2430), [2472](https://github.com/CellProfiler/CellProfiler/pull/2473))
- [2334](https://github.com/CellProfiler/CellProfiler/pull/2335) Represent a volume as an image.
- [2340](https://github.com/CellProfiler/CellProfiler/pull/2344) MedialAxis.
- [2342](https://github.com/CellProfiler/CellProfiler/pull/2342) Add `multichannel` property to `cellprofiler.image.Image`.
- [2345](https://github.com/CellProfiler/CellProfiler/pull/2346) DistanceTransform (removed by [2411](https://github.com/CellProfiler/CellProfiler/pull/2417)).
- [2354](https://github.com/CellProfiler/CellProfiler/pull/2369) GaussianFilter.
- [2355](https://github.com/CellProfiler/CellProfiler/pull/2366) Open a volume.
- [2380](https://github.com/CellProfiler/CellProfiler/pull/2381) Visualize segmentation of a volume.
- [2390](https://github.com/CellProfiler/CellProfiler/pull/2391) RandomWalker. ([2472](https://github.com/CellProfiler/CellProfiler/pull/2473))
- [2395](https://github.com/CellProfiler/CellProfiler/pull/2396) Add contributing guidelines to project.
- [2408](https://github.com/CellProfiler/CellProfiler/pull/2428) ActiveContourModel. ([2472](https://github.com/CellProfiler/CellProfiler/pull/2473))
- [2410](https://github.com/CellProfiler/CellProfiler/pull/2410) EdgeDetection. ([2423](https://github.com/CellProfiler/CellProfiler/pull/2424))
- [2416](https://github.com/CellProfiler/CellProfiler/pull/2418) Assign names to loaded volumes.
- [2434](https://github.com/CellProfiler/CellProfiler/pull/2435) LaplacianOfGaussian.
- [2476](https://github.com/CellProfiler/CellProfiler/pull/2479) Add `volumetric` property to `cellprofiler.image.Image`.
- [2480](https://github.com/CellProfiler/CellProfiler/pull/2481) Add `mask` function to `cellprofiler.image.Image`, returns masked image data.

### Changed
- [2202](https://github.com/CellProfiler/CellProfiler/pull/2212) Move tests from `cellprofiler/tests` to `tests`.
- [2230](https://github.com/CellProfiler/CellProfiler/pull/2236) Use implicit getters and setters in `cellprofiler.image`.
- [2231](https://github.com/CellProfiler/CellProfiler/pull/2241) Use implicit getters and setters in `cellprofiler.object`.
- [2382](https://github.com/CellProfiler/CellProfiler/pull/2384) Volumetric support for ConvertObjectsToImage. ([2419](https://github.com/CellProfiler/CellProfiler/pull/2420))
- [2447](https://github.com/CellProfiler/CellProfiler/pull/2448) Upgrade to scikit-image 0.12.3.
- [2453](https://github.com/CellProfiler/CellProfiler/pull/2484) Volumetric support for MeasureImageIntensity ([2487](https://github.com/CellProfiler/CellProfiler/pull/2487)).
- [2488](https://github.com/CellProfiler/CellProfiler/pull/2490) Decouple GUI from `cellprofiler.workspace`.
- [2489](https://github.com/CellProfiler/CellProfiler/pull/2493) Decouple GUI from `cellprofiler.pipeline`.
- [2520](https://github.com/CellProfiler/CellProfiler/pull/2521) Exclude pyamg 3.2.0.

### Deprecated
-- none --

### Removed
- [1926](https://github.com/CellProfiler/CellProfiler/pull/2265) Remove `cellprofiler.utilities.version`. ([2509](https://github.com/CellProfiler/CellProfiler/pull/2510))
- [2078](https://github.com/CellProfiler/CellProfiler/pull/2270) Remove support for reading Cellomics files through `cellprofiler.image`.
- [2198](https://github.com/CellProfiler/CellProfiler/pull/2210) Remove module CreateWebPage.
- [2199](https://github.com/CellProfiler/CellProfiler/pull/2211) Remove module InputExternal.
- [2200](https://github.com/CellProfiler/CellProfiler/pull/2212) Remove module OutputExternal.
- [2201](https://github.com/CellProfiler/CellProfiler/pull/2214) Remove module SendEmail.
- [2205](https://github.com/CellProfiler/CellProfiler/pull/2212) Remove caching from `cellprofiler.image`, `cellprofiler.object`, and `cellprofiler.workspace`.
- [2237](https://github.com/CellProfiler/CellProfiler/pull/2238) Remove memoization from `cellprofiler.object`.
- [2485](https://github.com/CellProfiler/CellProfiler/pull/2492) Remove `cellprofiler.media`.
- [2486](https://github.com/CellProfiler/CellProfiler/pull/2491) Remove `cellprofiler.volume`.

### Fixed
- [1156](https://github.com/CellProfiler/CellProfiler/pull/2440) Document artifacting in IdentifyPrimaryObjects by [@AnneCarpenter](https://github.com/AnneCarpenter).
- [2150](https://github.com/CellProfiler/CellProfiler/pull/2161) Add `figure` parameter to image template `display` function.
- [2193](https://github.com/CellProfiler/CellProfiler/pull/2296) Calculate Zernike features only when prompted by [@tomgreen66](https://github.com/tomgreen66).
- [2257](https://github.com/CellProfiler/CellProfiler/pull/2257) Documentation correction for MeasureImageQuality by [@AnneCarpenter](https://github.com/AnneCarpenter).
- [2259](https://github.com/CellProfiler/CellProfiler/pull/2259) Documentation correction for measurement template by [@AnneCarpenter](https://github.com/AnneCarpenter).
- [2277](https://github.com/CellProfiler/CellProfiler/pull/2277) Documentation correction for ExportToDatabase by [@dlogan](https://github.com/dlogan).
- [2287](https://github.com/CellProfiler/CellProfiler/pull/2287) Link to developer's wiki by [@AnneCarpenter](https://github.com/AnneCarpenter).
- [2299](https://github.com/CellProfiler/CellProfiler/pull/2299) Documentation correction by [@AnneCarpenter](https://github.com/AnneCarpenter).
- [2359](https://github.com/CellProfiler/CellProfiler/pull/2360) Documentation enhancement for PlateViewer by [@bethac07](https://github.com/bethac07).
- [2361](https://github.com/CellProfiler/CellProfiler/pull/2361) Documentation correction for MeasureTexture by [@AnneCarpenter](https://github.com/AnneCarpenter).
- [2367](https://github.com/CellProfiler/CellProfiler/pull/2368) Re-expose option for alternate colormaps in 8-bit images by [@bethac07](https://github.com/bethac07).
- [2387](https://github.com/CellProfiler/CellProfiler/pull/2388) Load help in welcome screen.
- [2406](https://github.com/CellProfiler/CellProfiler/pull/2407) Update deprecated features in setup.py.
- [2499](https://github.com/CellProfiler/CellProfiler/pull/2500) Correct radian conversion in IdentifyDeadWorms by [@bethac07](https://github.com/bethac07).

### Security
-- none --