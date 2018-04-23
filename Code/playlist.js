	var audio;
	var playlist;
	var tracks;
	var current;
	init();
	function init(){
		//Start at the first song.
		current = 0;
		audio = $('#audio');
		// load all the playlists
		playlist = $('#playlist');
		tracks = playlist.find('li a');
		link = playlist.find('a')[0]
		len = tracks.length;	//get the length of the playlist
		//Set the volume to 10 percent and start playing music.
		audio[0].volume = .10;
		audio[0].play();
		// If a song on the playlist is clicked start playing that song.
		playlist.find('a').click(function(e){
			e.preventDefault();
			link = $(this);
			current = link.parent().index();
			run(link, audio[0]);	// run music.
		});
		//Go to the next song when the current song is finished.
		audio[0].addEventListener('ended',function(e){
			current++;
			//Go back to the first song.
			if(current == len){
				current = 0;
				link = playlist.find('a')[0];
			}else{
				link = playlist.find('a')[current];   // Play the next song. 
			}
			run($(link),audio[0]);	// run music.
		});
	}
	// The function plays the loads and plays the current song 
	function run(link, player){
			player.src = link.attr('href');
			par = link.parent();
			par.addClass('active').siblings().removeClass('active'); //the active song will be light blue
			audio[0].load();	//load audio
			audio[0].play();	//play audio
			console.log(current);
	}
	// Pressing this button will jump to the next song
	btnNext = $('#btnNext').click(function() {
		current++;
		if(current >= len){
			current = 0;
			link = playlist.find('a')[0];
		}else{
		link = playlist.find('a')[current];   // Play the next song. 
		}
		run($(link),audio[0]);	// run music.
	})
	btnPrev = $('#btnPrev').click(function() {
		current--;
		if(current < 0){
			current = len - 1;
			link = playlist.find('a')[current];
		}else{
		link = playlist.find('a')[current];   // Play the next song. 
		}
		run($(link),audio[0]);	// run music.
	})