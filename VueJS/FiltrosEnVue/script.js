
let app = new Vue({
	el: '#app',
	data: {
		titulo: 'Están en Platzi',
		subtitulo: 'están viendo el curso de vue.JS'
	},
	filters: {
		mayuscula: function (str) {
			return str.toUpperCase()
		},
		minuscula: function (str){
			return str.toLowerCase()
		},
		capitalize: function (str){
			return str.charAt(0).toUpperCase()  + str.slice(1)
		}
	}
})