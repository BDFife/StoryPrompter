
SC.initialize({
  client_id: "01c9cf5034b7843aad46f934522ed597",
  redirect_uri: "http://storyprompter-bdfife.herokuapp.com"
});

$("#recorderUI.reset #controlButton").live("click", function(e){
  updateTimer(0);
  SC.record({
	start: function(){
	  setRecorderUIState("recording");
	},
	progress: function(ms, avgPeak){
	  updateTimer(ms);
	}
  });
  e.preventDefault();
});

$("#recorderUI.recording #controlButton, #recorderUI.playing #controlButton").live("click", function(e){
  setRecorderUIState("recorded");
  SC.recordStop();
  e.preventDefault();
});

$("#recorderUI.recorded #controlButton").live("click", function(e){
  updateTimer(0);
  setRecorderUIState("playing");
  SC.recordPlay({
	progress: function(ms){
	  updateTimer(ms);
	},
	finished: function(){
	  setRecorderUIState("recorded");
	}
  });
  e.preventDefault();
});

$("#reset").live("click", function(e){
  SC.recordStop();
  setRecorderUIState("reset");
  e.preventDefault();
});

$("#upload").live("click", function(e){
  setRecorderUIState("uploading");

  SC.connect({
	connected: function(){
	  $("#uploadStatus").html("Uploading...");
	  SC.recordUpload({
		track: {
		  title: "{{story_string}}",
		  sharing: "public",
		  tag_list: [
			'StoryPrompter'
		  ]
		}
	  }, function(track){
		$("#uploadStatus").html("Uploaded: <a href='" + track.permalink_url + "'>" + track.permalink_url + "</a>");
	  });
	}
  });

  e.preventDefault();
});

function updateTimer(ms){
  $("#timer").text(SC.Helper.millisecondsToHMS(ms));
}

function setRecorderUIState(state){
  // state can be reset, recording, recorded, playing, uploading
  // visibility of buttons is managed via CSS
  $("#recorderUI").attr("class", state);
}

