from __future__ import annotations

from typing import Union

from fastapi_camelcase import CamelModel

from src.models.pending_job.place import Place, PlaceAMS
from src.models.pending_job.service_qualification import ServiceSpecification


class AddressProcessingJob(CamelModel):
    csq_id: str
    instant_sync_qualification: bool
    provide_alternative: bool
    place: Union[PlaceAMS, Place]
    service_specification: ServiceSpecification
