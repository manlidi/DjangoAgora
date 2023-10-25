let options = 
{
    appId: '',
    channel: '',
    token: '',
    uid: 0,
};

let channelParameters =
{
  localAudioTrack: null,
  remoteAudioTrack: null,
  remoteUid: null,
};

async function startBasicCall()
{
  const agoraEngine = AgoraRTC.createClient({ mode: "rtc", codec: "vp9" });
  agoraEngine.on("user-published", async (user, mediaType) =>
  {
    await agoraEngine.subscribe(user, mediaType);
    console.log("subscribe success");

    
    if (mediaType == "audio")
    {
      channelParameters.remoteUid=user.uid;
      channelParameters.remoteAudioTrack = user.audioTrack;
      channelParameters.remoteAudioTrack.play();
      showMessage("Remote user connected: " + user.uid);
    }

    agoraEngine.on("user-unpublished", user =>
    {
      console.log(user.uid + "has left the channel");
      showMessage("Remote user has left the channel");
    });
  });

  window.onload = function ()
  {
    document.getElementById("join").onclick = async function ()
    {
      await agoraEngine.join(options.appId, options.channel, options.token, options.uid);
      showMessage("Joined channel: " + options.channel);
      channelParameters.localAudioTrack = await AgoraRTC.createMicrophoneAudioTrack();
      await agoraEngine.publish(channelParameters.localAudioTrack);
      console.log("Publish success!");
    }
    
    document.getElementById('leave').onclick = async function ()
    {
      channelParameters.localAudioTrack.close();
      await agoraEngine.leave();
      console.log("You left the channel");
      window.location.reload();
    }
  }
}

function showMessage(text){
  document.getElementById("message").textContent = text;
}

startBasicCall();
