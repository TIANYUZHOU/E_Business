<template>
  <div id="dvue">
    <Tabbar />
    <router-view />
  </div>
</template>

<script>
import Tabbar from "../../components/tabbar";

export default {
  data() {
    return {};
  },
  created() {},
  mounted() {},
  methods: {},
  components: {
    Tabbar
  }
};
</script>

<style scoped>
#dvue {
  width: 100%;
  height: 100%;
}
</style>
