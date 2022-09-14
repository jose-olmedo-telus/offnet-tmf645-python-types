# coding: utf-8

from __future__ import annotations

import re  # noqa: F401
from datetime import date, datetime  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from fastapi_camelcase import CamelModel  # noqa: F401
from pydantic import AnyUrl, Field


class TimePeriod(CamelModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    TimePeriod - a model defined in OpenAPI

        end_date_time: The end_date_time of this TimePeriod [Optional].
        start_date_time: The start_date_time of this TimePeriod [Optional].
        base_type: The base_type of this TimePeriod [Optional].
        schema_location: The schema_location of this TimePeriod [Optional].
        type: The type of this TimePeriod [Optional].
    """

    end_date_time: Optional[datetime] = None
    start_date_time: Optional[datetime] = None
    base_type: Optional[str] = None
    schema_location: Optional[AnyUrl] = None
    type: Optional[str] = Field(default=None, alias='@type')


TimePeriod.update_forward_refs()