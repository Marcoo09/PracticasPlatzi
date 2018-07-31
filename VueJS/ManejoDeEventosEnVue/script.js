
let app = new Vue({
	el: '#app',
	data: {
		count: 0
	},
	methods: {
		sumar: function (){
			this.count++
		},
		restar : function (){
			this.count--
		}
	}
})