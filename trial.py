import ee
from te_schemas.schemas import BandInfo

from . import GEEIOError
from . import stats
from .util import TEImage



def ndvi(year_initial, year_final, ndvi_1yr, logger, sensor):
    """Calculate temporal NDVI analysis.
    Calculates the trend of temporal NDVI using Landsat NDVI data.
    Args:
        year_initial: The starting year (to define the period the trend is
            calculated over).
        year_final: The ending year (to define the period the trend is
            calculated over).
        ndvi_1yr: An example NDVI image for reference.
        logger: Logger object for debugging/logging.
        sensor: Either "landsat5" or "landsat8" to specify the sensor.
    Returns:
        Output of Google Earth Engine task.
    """
    logger.debug("Entering ndvi_trend function.")

    if sensor == "landsat5":
        available_years = range(2000, 2013)
    elif sensor == "landsat8":
        available_years = range(2013, 2024)  # Up to 2023

    img_coll = ee.List([])

    for year in range(year_initial, year_final + 1):
        if year in available_years:
            ndvi_img = (
                ndvi_1yr.select("y" + str(year))
                .addBands(ee.Image(year).float())
                .rename(["ndvi", "year"])
            )
            img_coll = img_coll.add(ndvi_img)

    return ee.ImageCollection(img_coll)
