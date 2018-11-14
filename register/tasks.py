import os, glob, shutil
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
After clone the project repository, you may not be able to run celery beat. This is solved by deleting `celerybeat.pid` in project directory.
Setting Up:
$ pip install celery==3.1.18
$ pip freeze > requirements.txt
$ pip install redis==2.10.3
$ pip freeze > requirements.txt
@Sokunthaneth
"""

# run_every(crontab(*args)). Accepted arguments are minute, hour, day_of_week, day_of_month, month_of_year.
# final configuration, execute every day at midnight: run_every=(crontab(minute=0, hour=0))
@periodic_task(
    # testing: run_every 5 minutes
    run_every=(crontab(minute='*/5')),
    name="concatenate_video",
    ignore_result=True
)
def concatenate_video():
    """
    Concatenate pieces of videos uploaded by candidates during examination
    """
    # Change videos path according to the system
    # Add environment variable for ffmpeg
    candidates = []
    os.chdir("D:/Project/Online-Examination-System/media/temp_videos/")
    for file in glob.glob("*.webm"):
        candidate = file.split("_")[0]
        candidates.append(candidate)

    videos = ""
    previousCandidate = None
    initial = True
    count = 0
    newCandidate = True
    os.chdir("D:/Project/Online-Examination-System/ffmpeg/bin/")
    for candidate in candidates:
        if candidate == previousCandidate:
            # print "Previous candidate: " + previousCandidate
            count += 1
            videos += "D:/Project/Online-Examination-System/media/temp_videos/"+candidate+"_"+str(count)+".webm|"
        elif newCandidate is True:
            if initial is False:
                # print "New Candidate: "+candidate
                # Remove `|` at the end of videos list for concatenation
                os.system('ffmpeg -i concat:"'+videos[:-1]+'" -c copy D:/Project/Online-Examination-System/media/videos/'+previousCandidate+'.webm')
            initial = False
            videos = ""
            videos += "D:/Project/Online-Examination-System/media/temp_videos/"+candidate+"_1.webm|"
            newCandidate = False
        else:
            # print "+++Reset to new candidate+++"
            previousCandidate = candidate
            count = 0
            newCandidate = True
    os.system('ffmpeg -i concat:"'+videos[:-1]+'" -c copy D:/Project/Online-Examination-System/media/videos/'+candidate+'.webm')
    
    # Remove all files in `temp_videos` after completing concatenation
    shutil.rmtree('D:/Project/Online-Examination-System/media/temp_videos/')
    os.mkdir('D:/Project/Online-Examination-System/media/temp_videos/')