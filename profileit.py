from functools import wraps
import cProfile, pstats, StringIO
import logging

logger = logging.getLogger(__name__)

def profileit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        prof = cProfile.Profile()
        retval = prof.runcall(func, *args, **kwargs)
        s = StringIO.StringIO()
        #ps = pstats.Stats(prof, stream=s).sort_stats('time', 'cumulative')
        ps = pstats.Stats(prof, stream=s).sort_stats('cumtime')
        #ps.print_stats(.25)
        ps.print_stats(100)
        logger.info("profileit: %s", s.getvalue())
        return retval
    return wrapper
