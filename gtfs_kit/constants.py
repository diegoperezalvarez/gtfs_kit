"""
Constants useful across modules.
"""

import pandas as pd

# Record some data from the GTFS reference at https://gtfs.org/reference/static.
columns = ["table", "table_required", "column", "column_required", "dtype"]
rows = [
    ["agency", True, "agency_id", False, "string"],
    ["agency", True, "agency_name", True, "string"],
    ["agency", True, "agency_url", True, "string"],
    ["agency", True, "agency_timezone", True, "string"],
    ["agency", True, "agency_lang", False, "string"],
    ["agency", True, "agency_phone", False, "string"],
    ["agency", True, "agency_fare_url", False, "string"],
    ["agency", True, "agency_email", False, "string"],
    ["attributions", False, "attribution_id", False, "string"],
    ["attributions", False, "agency_id", False, "string"],
    ["attributions", False, "route_id", False, "string"],
    ["attributions", False, "trip_id", False, "string"],
    ["attributions", False, "organization_name", True, "string"],
    ["attributions", False, "is_producer", False, "Int8"],
    ["attributions", False, "is_operator", False, "Int8"],
    ["attributions", False, "is_authority", False, "Int8"],
    ["attributions", False, "attribution_url", False, "string"],
    ["attributions", False, "attribution_email", False, "string"],
    ["attributions", False, "attribution_phone", False, "string"],
    ["calendar", False, "service_id", True, "string"],
    ["calendar", False, "monday", True, "Int8"],
    ["calendar", False, "tuesday", True, "Int8"],
    ["calendar", False, "wednesday", True, "Int8"],
    ["calendar", False, "thursday", True, "Int8"],
    ["calendar", False, "friday", True, "Int8"],
    ["calendar", False, "saturday", True, "Int8"],
    ["calendar", False, "sunday", True, "Int8"],
    ["calendar", False, "start_date", True, "string"],
    ["calendar", False, "end_date", True, "string"],
    ["calendar_dates", False, "service_id", True, "string"],
    ["calendar_dates", False, "date", True, "string"],
    ["calendar_dates", False, "exception_type", True, "Int8"],
    ["fare_attributes", False, "fare_id", True, "string"],
    ["fare_attributes", False, "price", True, "float"],
    ["fare_attributes", False, "currency_type", True, "string"],
    ["fare_attributes", False, "payment_method", True, "Int8"],
    ["fare_attributes", False, "transfers", True, "Int8"],
    ["fare_attributes", False, "transfer_duration", False, "Int16"],
    ["fare_rules", False, "fare_id", True, "string"],
    ["fare_rules", False, "route_id", False, "string"],
    ["fare_rules", False, "origin_id", False, "string"],
    ["fare_rules", False, "destination_id", False, "string"],
    ["fare_rules", False, "contains_id", False, "string"],
    ["feed_info", False, "feed_publisher_name", True, "string"],
    ["feed_info", False, "feed_publisher_url", True, "string"],
    ["feed_info", False, "feed_lang", True, "string"],
    ["feed_info", False, "feed_start_date", False, "string"],
    ["feed_info", False, "feed_end_date", False, "string"],
    ["feed_info", False, "feed_version", False, "string"],
    ["frequencies", False, "trip_id", True, "string"],
    ["frequencies", False, "start_time", True, "string"],
    ["frequencies", False, "end_time", True, "string"],
    ["frequencies", False, "headway_secs", True, "Int16"],
    ["frequencies", False, "exact_times", False, "Int8"],
    ["routes", True, "route_id", True, "string"],
    ["routes", True, "agency_id", False, "string"],
    ["routes", True, "route_short_name", True, "string"],
    ["routes", True, "route_long_name", True, "string"],
    ["routes", True, "route_desc", False, "string"],
    ["routes", True, "route_type", True, "Int8"],
    ["routes", True, "route_url", False, "string"],
    ["routes", True, "route_color", False, "string"],
    ["routes", True, "route_text_color", False, "string"],
    ["shapes", False, "shape_id", True, "string"],
    ["shapes", False, "shape_pt_lat", True, "float"],
    ["shapes", False, "shape_pt_lon", True, "float"],
    ["shapes", False, "shape_pt_sequence", True, "Int32"],
    ["shapes", False, "shape_dist_traveled", False, "float"],
    ["stops", True, "stop_id", True, "string"],
    ["stops", True, "stop_code", False, "string"],
    ["stops", True, "stop_name", True, "string"],
    ["stops", True, "stop_desc", False, "string"],
    ["stops", True, "stop_lat", True, "float"],
    ["stops", True, "stop_lon", True, "float"],
    ["stops", True, "zone_id", False, "string"],
    ["stops", True, "stop_url", False, "string"],
    ["stops", True, "location_type", False, "Int8"],
    ["stops", True, "parent_station", False, "string"],
    ["stops", True, "stop_timezone", False, "string"],
    ["stops", True, "wheelchair_boarding", False, "Int8"],
    ["stop_times", True, "trip_id", True, "string"],
    ["stop_times", True, "arrival_time", True, "string"],
    ["stop_times", True, "departure_time", True, "string"],
    ["stop_times", True, "stop_id", True, "string"],
    ["stop_times", True, "stop_sequence", True, "Int32"],
    ["stop_times", True, "stop_headsign", False, "string"],
    ["stop_times", True, "pickup_type", False, "Int8"],
    ["stop_times", True, "drop_off_type", False, "Int8"],
    ["stop_times", True, "shape_dist_traveled", False, "float"],
    ["stop_times", True, "timepoint", False, "Int8"],
    ["transfers", False, "from_stop_id", True, "string"],
    ["transfers", False, "to_stop_id", True, "string"],
    ["transfers", False, "transfer_type", True, "Int8"],
    ["transfers", False, "min_transfer_time", False, "Int16"],
    ["trips", True, "route_id", True, "string"],
    ["trips", True, "service_id", True, "string"],
    ["trips", True, "trip_id", True, "string"],
    ["trips", True, "trip_headsign", False, "string"],
    ["trips", True, "trip_short_name", False, "string"],
    ["trips", True, "direction_id", False, "Int8"],
    ["trips", True, "block_id", False, "string"],
    ["trips", True, "shape_id", False, "string"],
    ["trips", True, "wheelchair_accessible", False, "Int8"],
    ["trips", True, "bikes_allowed", False, "Int8"],
]
GTFS_REF = pd.DataFrame(rows, columns=columns)

#: Data types for Pandas CSV reads
DTYPE = dict(GTFS_REF[["column", "dtype"]].values)

#: Valid distance units
DIST_UNITS = ["ft", "mi", "m", "km"]

#: Primary feed attributes
FEED_ATTRS_1 = [
    "agency",
    "attributions",
    "calendar",
    "calendar_dates",
    "fare_attributes",
    "fare_rules",
    "feed_info",
    "frequencies",
    "routes",
    "shapes",
    "stops",
    "stop_times",
    "trips",
    "transfers",
    "dist_units",
]

#: Secondary feed attributes; derived from primary ones
FEED_ATTRS_2 = ["_trips_i", "_calendar_i", "_calendar_dates_i"]

#:
FEED_ATTRS = FEED_ATTRS_1 + FEED_ATTRS_2

#: WGS84 coordinate reference system for Geopandas
WGS84 = "EPSG:4326"

#: Colorbrewer 8-class Set2 colors
COLORS_SET2 = [
    "#66c2a5",
    "#fc8d62",
    "#8da0cb",
    "#e78ac3",
    "#a6d854",
    "#ffd92f",
    "#e5c494",
    "#b3b3b3",
]
