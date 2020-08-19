<template>
  <div id="yxyx">
    <van-tabs v-model="active">
      <van-tab title="全部">
        <div>
          <Titems />
        </div>
      </van-tab>
      <van-tab title="畅销"><Titems /></van-tab>
      <van-tab title="推荐"><Titems /></van-tab>
      <van-tab title="进口"><Titems /></van-tab>
    </van-tabs>
  </div>
</template>

<script>
import Titems from "./tabbitems";
export default {
  data() {
    return {
      active: 0
    };
  },
  created() {},
  mounted() {},
  methods: {},
  components: {
    Titems
  }
};
</script>

<style scoped>
/*#lsdfjkld {*/
/*  margin-top: 1730px;*/
/*}*/

#yxyx {
  /*height: 1300px;*/
  /*margin-top: -100px;*/
}
</style>
