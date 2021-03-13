<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>Lista de productos</h2>
    <table>
      <thead>
        <tr>
          <th style="width: 15%">Nombre</th>
          <th style="width: 30%">Descripción</th>
          <th style="width: 40%">Imagen</th>
          <th style="width: 15%">Comprar?</th>
        </tr>
      </thead>
      <tbody v-if="apiData">
        <tr v-for="prop in apiData.data.result" v-bind:key="prop[0]">
          <td :id="'name-' + prop[0]"><b>{{ prop[0] }}</b></td>
          <td :id="'desc-' + prop[0]">{{ prop[1] }}</td>
          <td><img height="50" width="100" :src="prop[2]" :alt="prop[0]"/></td>
          <td><button :id="'buy-' + prop[0]" v-on:click="registerOrder(prop[0])">Comprar</button></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Shop',
  props: {
    msg: String
  },
  data () {
    return {
      apiData: null,
      errors: []
    }
  },
  mounted () {
    axios
      .get(process.env.BACKEND_API + '/items')
      .then(response => (this.apiData = response))
  },
  methods: {
    fetchData: function (name, email) {
      return axios
        .post(process.env.BACKEND_API + '/register', {'email': email, 'name': name})
        .then((response) => {
          return response.data
        })
        .catch(e => {
          this.errors.push(e)
        })
    },
    registerOrder: function (name) {
      this.$prompt('Email:').then(email => {
        this.fetchData(name, email)
          .then((response) => {
            if (response && response.error) {
              this.$alert('Error', response.msg, 'error')
            } else {
              this.$alert(email, response.msg, 'success')
            }
          })
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
table {
  width: 70%;
  margin-left: 15%;
  margin-right: 15%;
  border-spacing: 5px;
  padding: 10px 0 0 25px;
}

th, td {
  padding: 15px;
}
</style>
