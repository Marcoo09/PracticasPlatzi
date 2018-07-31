
function leftPad(number){
	let numberWithZeros = number >= 10 ? `${number}` : `0${number}`	
	return numberWithZeros
}

function rightPad(number){
	let numberWithZeros = number >= 10 ? `${number}` : `0${number}`	 
	return numberWithZeros

}

function formattedTime(secs){
	const minutes = parseInt(secs / 60, 10)
	const seconds = parseInt(secs % 60,10)

	return  `${leftPad(minutes)}:${rightPad(seconds)}`

	//Otra forma de hacerlo
/*	if((minutes < 10) && (seconds < 10)){
		return  `0${minutes}:0${seconds}`
	}else if((minutes >= 10) && (seconds >= 10)){
		return  `${minutes}:${seconds}`
	}else if((minutes < 10) && (seconds >= 10)){
		return  `0${minutes}:${seconds}`
	}
	else if((minutes >= 10) && (seconds < 10)){
		return  `${minutes}:0${seconds}`
	}*/
}

export {formattedTime, leftPad, rightPad}