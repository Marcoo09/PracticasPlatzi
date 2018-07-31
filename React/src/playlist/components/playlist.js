import React, {Component} from 'react'
import Media from './media'
import './playlist.css'

class Playlist extends Component {
	render(){
		return(
			<div className = "Playlist">
				{
					this.props.playlist.map((item) => {
						return <Media {...item} key= {item.id} openModal = {this.props.handleOpenModal} />
						
					})
				}
			</div>
			
			)
	}
}

export default Playlist