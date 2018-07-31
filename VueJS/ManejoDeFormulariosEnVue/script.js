
let app = new Vue({
	el: '#app',
	data: {
		nombre: '',
		cursos: []
	},
	methods: {
		submit: function (){
			console.log('Se ejecuta el metodo submit')
			console.log(this.cursos)
		}
	},
	filters: {
		uppercase: function (str){
			return str.toUpperCase()
		}
	}
})