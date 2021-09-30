<template>
  <div id="app">
    <button @click="hello">python-service2button</button><br>
    <button>python</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name:'TestComponent',
  data(){
    return{
    }
  },
  methods: {
    hello:() =>{
      console.log('hello')
      axios.get('/users')
      .then(res => {
        console.log(res)
      })
    },
  }
}
</script>

<style scoped lang="scss"> //scopedをつけるとこのcomponentだけで使用される（普通つける）
.red-b{
  border:1px red solid;
}

.border{
  &__blue{
    border:1px blue solid;
  }
}

.background__primary{
  background-color: $color-primary;
}


</style>