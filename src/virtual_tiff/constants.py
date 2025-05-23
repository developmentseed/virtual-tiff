from virtual_tiff.imagecodecs import (
    DeflateCodec,
    WebpCodec,
    JpegXLCodec,
    ZstdCodec,
    JetRawCodec,
    LZWCodec,
    PngCodec,
    LercCodec,
    Jpeg2KCodec,
    PackBitsCodec,
    JpegCodec,
    JpegXRCodec,
    Jpeg8Codec,
)
from numcodecs.zarr3 import Zlib, LZMA

ENDIAN = {b"MM": "big", b"II": "little"}
COMPRESSORS = {
    1: None,
    8: Zlib,
    32946: Zlib,
    34925: LZMA,
    50013: DeflateCodec,  # pixtiff
    5: LZWCodec,
    7: JpegCodec,
    22610: JpegXRCodec,
    32773: PackBitsCodec,
    33003: Jpeg2KCodec,
    33004: Jpeg2KCodec,
    33005: Jpeg2KCodec,
    33007: JpegCodec,
    34712: Jpeg2KCodec,
    34887: LercCodec,
    34892: Jpeg8Codec,
    34933: PngCodec,
    34934: JpegXRCodec,
    48124: JetRawCodec,
    50000: ZstdCodec,  # numcodecs.zstd fails w/ unknown sizes
    50001: WebpCodec,
    50002: JpegXLCodec,
    52546: JpegXLCodec,
}

# https://github.com/cgohlke/tifffile/blob/master/tifffile/tifffile.py#L7901-L7986
# Map SampleFormat and BitsPerSample tags to numpy dtype
SAMPLE_DTYPES = {
    # UINT
    (1, 1): "?",  # bitmap
    (1, 2): "B",
    (1, 3): "B",
    (1, 4): "B",
    (1, 5): "B",
    (1, 6): "B",
    (1, 7): "B",
    (1, 8): "B",
    (1, 9): "H",
    (1, 10): "H",
    (1, 11): "H",
    (1, 12): "H",
    (1, 13): "H",
    (1, 14): "H",
    (1, 15): "H",
    (1, 16): "H",
    (1, 17): "I",
    (1, 18): "I",
    (1, 19): "I",
    (1, 20): "I",
    (1, 21): "I",
    (1, 22): "I",
    (1, 23): "I",
    (1, 24): "I",
    (1, 25): "I",
    (1, 26): "I",
    (1, 27): "I",
    (1, 28): "I",
    (1, 29): "I",
    (1, 30): "I",
    (1, 31): "I",
    (1, 32): "I",
    (1, 64): "Q",
    # VOID : treat as UINT
    (4, 1): "?",  # bitmap
    (4, 2): "B",
    (4, 3): "B",
    (4, 4): "B",
    (4, 5): "B",
    (4, 6): "B",
    (4, 7): "B",
    (4, 8): "B",
    (4, 9): "H",
    (4, 10): "H",
    (4, 11): "H",
    (4, 12): "H",
    (4, 13): "H",
    (4, 14): "H",
    (4, 15): "H",
    (4, 16): "H",
    (4, 17): "I",
    (4, 18): "I",
    (4, 19): "I",
    (4, 20): "I",
    (4, 21): "I",
    (4, 22): "I",
    (4, 23): "I",
    (4, 24): "I",
    (4, 25): "I",
    (4, 26): "I",
    (4, 27): "I",
    (4, 28): "I",
    (4, 29): "I",
    (4, 30): "I",
    (4, 31): "I",
    (4, 32): "I",
    (4, 64): "Q",
    # INT
    (2, 8): "b",
    (2, 16): "h",
    (2, 32): "i",
    (2, 64): "q",
    # IEEEFP : 24 bit not supported by numpy
    (3, 16): "e",
    # (3, 24): '',  #
    (3, 32): "f",
    (3, 64): "d",
    # COMPLEXIEEEFP
    (6, 64): "F",
    (6, 128): "D",
    # RGB565
    (1, (5, 6, 5)): "B",
    # COMPLEXINT : not supported by numpy
}

GEO_KEYS = [
    "citation",
    "geog_angular_unit_size",
    "geog_angular_units",
    "geog_azimuth_units",
    "geog_citation",
    "geog_ellipsoid",
    "geog_geodetic_datum",
    "geog_inv_flattening",
    "geog_linear_unit_size",
    "geog_linear_units",
    "geog_prime_meridian",
    "geog_prime_meridian_long",
    "geog_semi_major_axis",
    "geog_semi_minor_axis",
    "geographic_type",
    "model_type",
    "proj_azimuth_angle",
    "proj_center_easting",
    "proj_center_lat",
    "proj_center_long",
    "proj_center_northing",
    "proj_citation",
    "proj_coord_trans",
    "proj_false_easting",
    "proj_false_northing",
    "proj_false_origin_easting",
    "proj_false_origin_lat",
    "proj_false_origin_long",
    "proj_false_origin_northing",
    "proj_linear_unit_size",
    "proj_linear_units",
    "proj_nat_origin_lat",
    "proj_nat_origin_long",
    "proj_scale_at_center",
    "proj_scale_at_nat_origin",
    "proj_std_parallel1",
    "proj_std_parallel2",
    "proj_straight_vert_pole_long",
    "projected_type",
    "projection",
    "raster_type",
    "vertical",
    "vertical_citation",
    "vertical_datum",
    "vertical_units",
]
