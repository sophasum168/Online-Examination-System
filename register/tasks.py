from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="concatenate_video",
    ignore_result=True
)
def concatenate_video():
    """
    Concatenate pieces of videos uploaded from a particualr candidate during examination
    """
    print "Hiii"