import React, {PureComponent} from 'react'
import PropTypes from 'prop-types'
import './media.css' 

class Media extends PureComponent {
	/*constructor(props){
		super(props)
		//this.handleClick = this.handleClick.bind(this)

		// In ES6 the state could be declared as below
		this.state = {
			author: props.author
		}
	}
	

	// In ES7 the state could be declared as below
	state = {
		author: 'Marco Fiorito'
	}
	
	handleClick = (event) => {
		//console.log(this.props.image)
		this.setState({
			author: 'Bica'
		})
	}
	*/
	render(){
		return (
			<div className="Media" onClick = {this.handleClick}>
				<div className="Media-cover">
					<img
						src = {this.props.cover}
						alt = ""
						width={260}
						height ={160}
						className ="Media-image"
					/>
					<h3 className="Media-title">{this.props.title}</h3>
					<p className ="Media-autor">{this.props.author}</p>
				</div>	
			</div>		
		)
	}
}

Media.propTypes = {
	cover: PropTypes.string,
	title: PropTypes.string.isRequired,
	author: PropTypes.string,
	type: PropTypes.oneOf(['video','audio'])
}

export default Media;
