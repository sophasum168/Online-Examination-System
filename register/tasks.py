import os, glob
from celery.schedules import crontab
from celery.task import periodic_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

"""
Task scheduling in Django:
Need to install celery, redis. When Run, start redis-server. Open two terminals. One for celery work, another one for celery beat using the command below
`celery -A exam worker -l info`
`celery -A exam beat -l info`
Tutorial: https://realpython.com/asynchronous-tasks-with-django-and-celery/
After clone the project repository, you maynot be able to run celery beat. This is solved by deleting `celerybeat.pid` in project directory.
@Sokunthaneth
"""

# run_every(crontab(*args)). Accepted arguments are minute, hour, day_of_week, day_of_month, month_of_year. 
@periodic_task(
    run_every=(crontab(minute='*/1')),
    name="concatenate_video",
    ignore_result=True
)
def concatenate_video():
    """
    Concatenate pieces of videos uploaded by candidates during examination
    """
    candidates = []
    os.chdir("./media/temp_videos")
    for file in glob.glob("*.webm"):
        candidate = file.split("_")[0]
        candidates.append(candidate)
    print "Candidate list: ", candidates

    videos = ""
    previousCandidate = None
    initial = True
    count = 0
    newCandidate = True
    for candidate in candidates:
        if candidate == previousCandidate:
            print "Previous candidate: " + previousCandidate
            count += 1
            videos += "./media/temp_videos/"+candidate+"_"+str(count)+".webm|"
        elif newCandidate is True:
            print "New Candidate: "+candidate
            if initial is False:
                os.system('/usr/bin/ffmpeg -i concat:"'+videos+'" -c copy ./media/videos/'+candidate+'.webm')
            initial = False
            videos = ""
            videos += "./media/temp_videos/"+candidate+"_1.webm|"
            newCandidate = False
        else:
            print "+++Reset to new candidate+++"
            previousCandidate = candidate
            count = 0
            newCandidate = True
    os.system('/usr/bin/ffmpeg -i concat:"'+videos+'" -c copy ./media/videos/'+candidate+'.webm')

    os.system('/usr/bin/ffmpeg -i concat:"sophasum_1.webm|sophasum_2.webm|sophasum_3.webm" -c copy haha.webm')
    # D:\Projects\Online-Examination-System\media\videos\n