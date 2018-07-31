import React from 'react'
import './search.css'
/*function Search(props){
	return 
}*/

const Search = (props) => (
	<form 
	className ='Search'
	onSubmit = {props.handleSubmit}
	>
		<input
		 type ='text' 
		 className ='Search-input' 
		 placeholder = 'Busca tu video favorito'
		 name = 'search'
		 ref = {props.setRef}
		 onChange = {props.handleChange}
		 value = {props.value}
		 />
	</form>
)

export default Search 