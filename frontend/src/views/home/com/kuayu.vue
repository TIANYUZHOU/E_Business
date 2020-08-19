<template>
  <div>
    <p v-for="(item, index) in msg" :key="index">{{item.category}}
    <br>
    <img :src="item.small_image" alt="">
    </p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      msg: null
    };
  },

  created() {
    this.axios.get('/api/get_pd').then(response => {
      var dd =response.data
      this.msg=dd
      console.log(dd)
    })
  }
};
</script>
