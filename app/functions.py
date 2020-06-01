import time

from rq import get_current_job

from . import models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

def some_long_function(some_input):
        job = get_current_job()
        time.sleep(10)

        db = SessionLocal()

        result = models.Result(
            job_id=job.id,
            job_enqueued_at=job.enqueued_at,
            job_started_at=job.started_at,
            input=some_input,
            result=some_input
        )

        db.add(result)
        db.commit()
        db.close()

        return {
            "job_id": job.id,
            "job_enqueued_at": job.enqueued_at.isoformat(),
            "job_started_at": job.started_at.isoformat(),
            "input": some_input,
            "result": some_input
        }
