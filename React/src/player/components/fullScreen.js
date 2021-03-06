import React from 'react'
import FullScreenIcon from '../../icons/components/full-screen'
import './fullScreen.css'

let FullScreen = (props) => {
	return(
		<div 
			className = "FullScreen"
			onClick = {props.handleFullScreenClick}
		>
			<FullScreenIcon
				color = "white"
				size = {25}
			/>
		</div>

		)
}

export default FullScreen