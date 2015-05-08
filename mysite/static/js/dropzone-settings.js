$(document).ready(function(){
    Dropzone.autoDiscover = false;
    var dropzone = new Dropzone('.dropzone', {
       autoProcessQueue: false,
       parallelUploads: 100,
       maxFiles: 100,
       maxFilesize: 50,
       paramName: 'file',
       acceptedFiles: '.ogg,.ogv,.mov,.MOV,.mpeg4,.mp4,.avi,.wmv,.mpegps,.flv,.3gpp,.webm,.mpeg,.png,.jpg,.jpeg,.gif',
       init:function() {
           myDropzone = this;
           myDropzone.on('sending',function(file,xhr,formData){
           });
        }
    });
});