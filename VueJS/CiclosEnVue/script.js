
let app = new Vue({
	el: '#app',
	data: {
		nombre: '',
		cursos: [
			{nombre:'Curso de Vue.Js',value:'vue'},
			{nombre:'Curso de Python',value:'python'},
			{nombre:'Curso de Machine Learning',value:'ml'}
		],
		cursosSeleccionados: []
	},
	methods: {
		submit: function (){
			console.log('Se ejecuta el metodo submit')
			console.log(this.cursosSeleccionados)
		}
	}
})