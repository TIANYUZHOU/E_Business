<template>
  <div>
    <Headerx />
    <Com />
    <Nav />
    <Flshe />
    <Flashdrug />
    <Tabbs />
    <MarkPage v-if="showBackStatus" :scrollToTop="scrollToTop" />
    <router-view />
  </div>
</template>

<script>
  import PubSub from 'pubsub-js'
  import BScroll from 'better-scroll'
  import { mapMutations } from 'vuex'
  import { showBack, animate } from '../../configs/global'
  import Headerx from './com/header'
  import Com from './com/sow'
  import Nav from './com/Nav'
  import Flshe from './com/flshe'
  import Flashdrug from './com/flashdrug'
  import Tabbs from './com/tabbs'
  import Tabbitems from './com/tabbitems'
  import MarkPage from './com/markPage'
  import Kuayu from './com/kuayu'
  import { Toast } from 'vant'
  export default {
    data() {
      return {
        showBackStatus: false,
      }
    },
    created() {
      this.showloading = false
      showBack((status) => {
        // console.log(status);
        this.showBackStatus = status
      })
    },
    mounted() {
      //监听添加到购物车的消息
      PubSub.subscribe('homeAddToCart', (msg, goods) => {
        if (msg === 'homeAddToCart') {
          this.ADD_GOODS({
            goodsId: goods.id,
            goodsName: goods.name,
            smallImage: goods.small_image,
            goodsPrice: goods.price,
          })
        }
      })
      PubSub.subscribe('homeAddToCart2', (msg, goods) => {
        if (msg === 'homeAddToCart2') {
          this.ADD_GOODS({
            goodsId: goods.id,
            goodsName: goods.name,
            smallImage: goods.small_image,
            goodsPrice: goods.price,
          })
          Toast({
            message:'添加到购物车OK',duration:800
          })
        }
      })
    },
    methods: {
      ...mapMutations(['ADD_GOODS']),
      // 1. 滚回顶部
      scrollToTop() {
        // 做缓动动画返回顶部
        let docB = document.documentElement || document.body
        animate(docB, { scrollTop: '0' }, 400, 'ease-out')
      },
    },
    components: {
      Headerx,
      Com,
      Nav,
      Flshe,
      Flashdrug,
      Tabbs,
      Tabbitems,
      MarkPage,
      Kuayu,
    },
  }
</script>

<style scoped>
</style>
