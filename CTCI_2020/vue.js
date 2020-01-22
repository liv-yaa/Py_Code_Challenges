// Not used
// Vue.component('button', {
//   data: function () {
//     return {
//       count: 0
//     }
//   },
//   template: '<button v-on:click="count++">You clicked me {{ count }} times.</button>'
// })





// Other simple option
Vue.component('my-button', {
  props: ['message'],
  template: 
  	'<button>{{ message }}</button>'
})
