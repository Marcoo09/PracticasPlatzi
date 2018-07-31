import React, {Component} from 'react'
import Playlist from './playlist'
import './category.css'

class Category extends Component {

	render(){
		const categories = this.props.data.categories

		return (

				<div>

					{
						categories.map((category) => {
							return(

								<div className = " Category" key = {category.id}>

									<h1 className = "Category-title">{category.title}</h1>

									<Playlist data ={category.playlist} />

								</div>

								)
						})
					}

				</div>
			)
	}
}


export default Category
