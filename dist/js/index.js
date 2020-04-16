Vue.component('nav-bar', {
  template: `
  <nav class="navbar navbar-transparent fixed-top px-3">
    <a class="navbar-brand" href="#">
      <img src="/assets/fotoBrand.png" height="40" alt="IT FOTO Club Logo">
    </a>
  </nav>
`
})

var app = new Vue({
  el: '#app'
})