var a_file;

$(document).on('click', '#scroll', function(event){
    event.preventDefault();
   document.getElementById('pre').style.display='block';

    $('html, body').animate({scrollTop: $('#pre').offset().top + $('#pre').height()}, 700,'swing');
    var img = document.createElement('img');
    img.src='/project/img/'+a_file+'.png';
    imgs.appendChild(img);

    $.post("pred.php",
        {
          npy: $.trim(a_file)+'.npy'
        },
        function(data){
            document.getElementById('res').innerHTML=data;
        });
});



function preprocess(link) {  
recorder && recorder.exportWAV(function(blob) {
var formData = new FormData();
formData.append('audio', blob, link.download);
$.ajax({
  url: 'preprocess.php',
  data: formData,
  processData: false,
  contentType: false,
  type: 'POST',
  success: function(data){
    __log('Preprocessing done');
    __log('Features Extracted');
    a_file=data;
    $('#file_name').html(a_file);
    $('#file_npy').html("<a href='npy/"+a_file+".npy'>"+a_file+".npy</a>");
    $('#file_length').html(Math.floor(document.getElementsByTagName('audio')[0].duration)+' sec');
  }
});
});
}


  function __log(e, data) {
    log.innerHTML += "\n" + e + " " + (data || '');
  }

  var audio_context;
  var recorder;

  function startUserMedia(stream) {
    var input = audio_context.createMediaStreamSource(stream);
    __log('Media stream created.');

    // Uncomment if you want the audio to feedback directly
    //input.connect(audio_context.destination);
    //__log('Input connected to audio context destination.');
    
    recorder = new Recorder(input);
    __log('Recorder initialised.');
  }
  // var flag=0;
  function startRecording(button) {
    // if (flag==0) {
    // init();
    // }
    // flag=1;
    var rec=document.getElementById('rec');
    var log=document.getElementById('log');
    var log_label=document.getElementById('log_label');
    rec.style.display="block";
    log.style.display="block";
    log_label.style.display="block";
    recorder && recorder.record();
    button.disabled = true;
    button.nextElementSibling.disabled = false;
    __log('Recording...');
  }

  function stopRecording(button) {
    recorder && recorder.stop();
    button.disabled = true;
    button.previousElementSibling.disabled = false;
    __log('Stopped recording.');
    
    // create WAV download link using audio data blob
    createDownloadLink();
   // recorder.clear();
  }

  function createDownloadLink() {
    recorder && recorder.exportWAV(function(blob) {
      var url = URL.createObjectURL(blob);
      var li = document.createElement('li');
      var au = document.createElement('audio');
      var hf = document.createElement('button');
      
      au.controls = true;
      au.src = url;
      hf.href = url;
      hf.download = Math.floor(Math.random()*10000).toString() + '.wav';
      hf.innerHTML = "Preprocess";
      hf.setAttribute('class','btn btn-primary');
      hf.setAttribute('onclick','preprocess(this)');
      hf.setAttribute('name','Audio');
      li.appendChild(au);
      li.appendChild(hf);
      recordingslist.appendChild(li);

    });
  }
    window.onload = function init() {
    try {
      // webkit shim
      window.AudioContext = window.AudioContext || window.webkitAudioContext;
      navigator.getUserMedia = navigator.getUserMedia || navigator.webkitGetUserMedia;
      window.URL = window.URL || window.webkitURL;
      
      audio_context = new AudioContext;
      __log('Audio context set up.');
      __log('navigator.getUserMedia ' + (navigator.getUserMedia ? 'available.' : 'not present!'));
    } catch (e) {
      alert('No web audio support in this browser!');
    }
    
    navigator.getUserMedia({audio: true}, startUserMedia, function(e) {
      __log('No live audio input: ' + e);
    });
  };




  $(function() {

  // We can attach the `fileselect` event to all file inputs on the page
  $(document).on('change', ':file', function() {
    var input = $(this),
        numFiles = input.get(0).files ? input.get(0).files.length : 1,
        label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.trigger('fileselect', [numFiles, label]);
  });

  // We can watch for our custom `fileselect` event like this
  $(document).ready( function() {
      $(':file').on('fileselect', function(event, numFiles, label) {

          var input = $(this).parents('.input-group').find(':text'),
              log = numFiles > 1 ? numFiles + ' files selected' : label;

          if( input.length ) {
              input.val(log);
          } else {
              if( log ) alert(log);
          }

      });
  });
  
});


