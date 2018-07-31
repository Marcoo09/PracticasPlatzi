import React from 'react'
import VolumenIcon from '../../icons/components/volume'
import './volumen.css'

function Volumen(props){
	return(
		<button
			className = "Volume"	
		>
			<div 
				className = "VolumeIcon"
				onClick = {props.iconClick}
			>
				<VolumenIcon
					color = "white"
					size ={25}
				/>	
			</div>

			<div className = "Volume-range">
				<input
					type = "range"
					min = {0}
					max = {1}
					step = {.05} 
					onChange = {props.handleVolumenChange}
					value = {props.value}
				/>
			</div>
		</button>
		)
}

export default Volumen