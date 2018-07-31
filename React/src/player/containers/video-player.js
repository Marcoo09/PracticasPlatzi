import React, {Component} from 'react'
import VideoPlayerLayout from'../components/video-player-layout'
import Video from '../components/video'
import Title from '../components/title'
import PlayPause from '../components/play-pause'
import Timer from '../components/timer'
import VideoPlayerControls from '../components/video-player-control'
import ProgressBar from '../components/progress-bar'
import {formattedTime, leftPad, rightPad} from '../components/formatter'
import Spinner from '../components/spinner'
import Volumen from '../components/volumen'
import FullScreen from '../components/fullScreen'

class VideoPlayer extends Component {
	state = {
		pause: true,
		duration: 0,
		currentTime: 0,
		loading: false,
		lastVolume: null,
		volume: 1,
	}
	togglePlay = event => {
		this.setState({
			pause: !this.state.pause,
		})
	}
	componentDidMount(){
		this.setState({
			pause: (!this.props.autoplay)
		})
	}
	handleloadedMetadata= event =>{
		this.video = event.target
		this.setState({
			duration: this.video.duration
		})
	}

	handleTimeUpdate = event => {
		this.video = event.target
		this.setState({
			currentTime: this.video.currentTime
		})
	}
	timeFormatter = (time) => {
		return formattedTime(time)
	}
	handleProgressChange = event => {
		this.video.currentTime = event.target.value
	}
	handleSeeking = event => {
		this.setState({
			loading:true,
		})
	} 
	handleSeeked = event => {
		this.setState({
			loading:false,
		})
	}
	handleVolumenChange = event => {
		this.setState({
			volume: event.target.value
		})
		this.video.volume = event.target.value
	}
	mute = () => {
		const lastVolumeState = this.video.volume
		this.setState({
			lastVolume: lastVolumeState,
			volume: 0,
		})
		this.video.volume = 0
	}
	unMute = () => {
		this.setState({
			volume: this.state.lastVolume,
		})
		this.video.volume = this.state.lastVolume
	}
	handleIconClick = event => {
		console.log(this.video.volume)
		this.video.volume !== 0 ? this.mute() : this.unMute()
		console.log(this.video.volume)
	}
	handleFullScreenClick = event => {
		if (!document.webkitIsFullScreen){
			this.player.webkitRequestFullscreen()
		}else{
			document.webkitExitFullscreen()
		}
	}
	setRef = element => {
		this.player = element
	}
	render() {
		return (
				<VideoPlayerLayout 
					setRef = {this.setRef}
				>
					<Title title = {this.props.title}/>
					<VideoPlayerControls>
						<PlayPause 
							handleClick = {this.togglePlay}
							pause = {this.state.pause}
						/>
						<Timer 
							duration ={this.timeFormatter(this.state.duration)}
							currentTime = {this.timeFormatter(this.state.currentTime)}

						/>
						<ProgressBar
							duration = {this.state.duration}
							value = {this.state.currentTime}
							handleProgressChange = {this.handleProgressChange}
						/>
						<Volumen
							handleVolumenChange = {this.handleVolumenChange}
							iconClick = {this.handleIconClick}
							value = {this.state.volume}
						/>
						<FullScreen
							handleFullScreenClick = {this.handleFullScreenClick}
						/>
					</VideoPlayerControls>
					<Spinner
						active = {this.state.loading}
					/>
					<Video
						src = {this.props.src}
						autoPlay = {this.props.autoplay}
						pause = {this.state.pause}
						handleLoadedMetadata = {this.handleloadedMetadata}
						handleTimeUpdate = {this.handleTimeUpdate}
						handleSeeking = {this.handleSeeking}
						handleSeeked = {this.handleSeeked}
					/>
				</ VideoPlayerLayout>
			)
	}
}

export default VideoPlayer