let {PythonShell} = require('python-shell')
// var audioconcat = require('audioconcat')
// const ffmpegInstaller = require('@ffmpeg-installer/ffmpeg');
// const ffmpeg = require('fluent-ffmpeg');
var path = require("path")

function convert() {
    var strInput = document.getElementById("strInput").value

    var options = {
        scriptPath : path.join(__dirname, '/../engine/'),
        args : [strInput]
      }
    try {
        let pyshell = new PythonShell('ttsE.py', options);
        pyshell.on('message', function (message) {
            // received a message sent from the Python script (a simple "print" statement)
            if(message.startsWith('return;')) {
                let arr = message.split(';');
                arr = arr.splice(1, arr.length);
                console.log('arr: ', arr);
                require('child_process').exec('start "" "voices"');
                // ffmpeg.setFfmpegPath(ffmpegInstaller.path);
                // audioconcat(arr)
                // .concat('audio.mp3')
                // .on('error', error => console.log('e: ', error))
                //  .on('end', () => console.log('ee: ',error))
                // crunker
                // .fetchAudio(arr)
                // .then(buffers => {
                //     // => [AudioBuffer, AudioBuffer]
                //     return crunker.concatAudio(buffers);
                // })
                // .then(merged => {
                //     // => AudioBuffer
                //     return crunker.export(merged, "audio/mp3");
                // })
                // .then(output => {
                //     // => {blob, element, url}
                //     crunker.download(output.blob);
                //     // document.body.append(output.element);
                //     // console.log(output.url);
                // })
                // .catch(error => {
                //     // => Error Message
                // });
            }
          });
    } catch (error) {
        document.getElementById("strInput").value = error
    } 
}

function clearText() {
    document.getElementById("strInput").value = ''
}