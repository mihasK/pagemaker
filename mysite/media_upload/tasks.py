from __future__ import absolute_import
import os
import subprocess
import shlex
from .utils import silent_remove_file
from celery import current_app
from celery.contrib.methods import task_method
from django.conf import settings

from celery.utils.log import get_task_logger



logger = get_task_logger(__name__)

@current_app.task
def delete_files(paths=[]):
    """
    Deletes all files for path in paths
    :param keep:
    :return:
    """
    for path in paths:
        silent_remove_file(path)


class Transcoder(object):

    def __init__(self, file_path, instance=None , to='.flv' , **kwargs):
        self.file_path = file_path
        self.instance = instance
        self.to = to
        self._generate_attributes()

    def _generate_attributes(self):
        self.old_path_absolute = self._add_media_root()
        self.new_file_absolute = self._change_extension(self.old_path_absolute)
        self.new_file_relative = self._change_extension(self.file_path)
        if self.instance:
            self.old_video_relative = self.instance.video.name
            self.old_video_absolute = self.instance.video.file.name

    def transcode_video_route(self):
        if not self.instance.video_needs_transcode:
            return

        self.transcode_video.delay()


    @current_app.task(filter=task_method)
    def transcode_video(self):

        with open(self.old_path_absolute, 'rw+') as f:
            ffmpeg_command = shlex.split('ffmpeg -i '+ '\"'+str(f.name) + '\"' \
                             +' -y -r 30000/1001 -b 2M -bt 4M -vcodec libx264 -acodec copy -pass 1 -preset fast -an '+ \
                              '\"'+self.new_file_absolute +'\"')

            subprocess.call(ffmpeg_command)

        if self.instance:
            self._save_transcoded_video()

        delete_files.delay([self.old_video_absolute])

    def _save_transcoded_video(self):
        self.instance.video =self.new_file_relative
        self.instance.video_needs_transcode = False
        self.instance.save()

    def _change_extension(self, path, to='flv'):
        base = os.path.splitext(path)[0]
        return base+'.'+to

    def _add_media_root(self):
        """
        Turns a relative media path to absolute media path
        :param path:
        :return:
        """
        return os.path.join(settings.MEDIA_ROOT, self.file_path)

def route_to_transcoder(**kwargs):
    if kwargs['instance'].video_needs_transcode:
        transcoder = Transcoder(kwargs['instance'].video.name, instance=kwargs['instance'])
        transcoder.transcode_video_route()

def route_to_delete(**kwargs):
    file_to_delete = 'test'
