from __future__ import annotations

from typing import Union

from fastapi_camelcase import CamelModel

from telus_bulk.models.worker_job.place import Place, PlaceAMS
from telus_bulk.models.worker_job.service_specification import ServiceSpecification


class AddressProcessingJob(CamelModel):
    csq_id: str
    instant_sync_qualification: bool
    provide_alternative: bool
    place: Union[PlaceAMS, Place]
    service_specification: ServiceSpecification
