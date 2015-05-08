from .tasks import route_to_transcoder
from .utils import file_cleanup

def route_to_transcoder_signal(sender, **kwargs):
    from .models import Media
    instance = kwargs.get('instance', None)
    if not isinstance(instance, Media):
        return
    elif not instance.video_needs_transcode:
        return
    route_to_transcoder(instance = kwargs['instance'])

def file_cleanup_signal(sender, **kwargs):
    from .models import Media
    if not isinstance(kwargs['instance'], Media):
        return
    file_cleanup(sender=sender , kwargs=kwargs, instance=kwargs['instance'])