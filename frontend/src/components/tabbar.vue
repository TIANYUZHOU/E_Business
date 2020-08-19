<template>
  <div>
    <van-tabbar @change="onChange" v-model="active" inactive-color="#666262" active-color="#F00E0E">
      <van-tabbar-item v-for="(item, index) in tabbars" :key="index" :to="item.name">
        <span>{{ item.title }}</span>
        <img slot="icon" slot-scope="props" :src="props.active ? item.active : item.normal" />
      </van-tabbar-item>
    </van-tabbar>
<!--    <p v-if="myhuibiao" style="background-color:red">{{goodsNum}}</p>-->
  </div>
</template>

<script>
  import { mapState } from 'vuex'
  import { mapMutations } from 'vuex'
  export default {
    name: 'tabbar',
    data() {
      return {
        active: Number(sessionStorage.getItem('tabBarActiveIndex')) || 0,
        myhuibiao:"",
        tabbars: [
          {
            name: '/dashboard/home', //绑定:to="item.name"跳转
            title: '首页',
            normal: require('./images/home1.png'),
            //"http://sucai.suoluomei.cn/sucai_zs/images/20190910093117-fx2.png",
            active: require('./images/home2.png'),
            // "http://sucai.suoluomei.cn/sucai_zs/images/20190910093117-fx.png"
          },
          {
            name: '/dashboard/category',
            title: '分类',
            normal: require('./images/categroy1.png'),
            //"http://sucai.suoluomei.cn/sucai_zs/images/20190910093117-xx.png",
            active: require('./images/categroy2.png'),
            //"http://sucai.suoluomei.cn/sucai_zs/images/20190910093117-xx2.png"
          },
          {
            name: '/dashboard/cart',
            title: '购物车',
            normal: require('./images/cart1.png'),
            //"http://sucai.suoluomei.cn/sucai_zs/images/20190910093117-wd.png",
            active: require('./images/cart2.png'),
            //"http://sucai.suoluomei.cn/sucai_zs/images/20190910093117-wd2.png"
          },
          {
            name: '/dashboard/main',
            title: '我的',
            normal: require('./images/my1.png'),
            //"http://sucai.suoluomei.cn/sucai_zs/images/20190910093117-wd.png",
            active: require('./images/my2.png'),
            // "http://sucai.suoluomei.cn/sucai_zs/images/20190910093117-wd2.png"
          },
        ],
      }
    },
    methods: {
      ...mapMutations(['INIT_SHOP_CART']),
      onChange() {
        if (this.active ===2) {
          this.myhuibiao = true
        }else{
          this.myhuibiao = false
        }
      }
    },
    //通过路由跳转判断选中的样式
    created() {
      if (this.$route.name == 'index') {
        this.active = 0
      } else if (this.$route.name == 'power') {
        this.active = 1
      } else if (this.$route.name == 'personal') {
        this.active = 2
      }
    },
    mounted(){
      this.INIT_SHOP_CART()
    },
    computed: {
      ...mapState(['shopCart']),
      goodsNum() {
        if (this.shopCart) {
          let num = 0
          console.log(Object.values(this.shopCart))
          Object.values(this.shopCart).forEach((goods, index) => {
            num += goods.num
          })
          return num
        } else {
          return 0
        }
      },
    },

    watch: {
      active(value) {
        //       console.log(value);
        let tabBarActiveIndex = value > 0 ? value : 0
        // 缓存到本地
        sessionStorage.setItem('tabBarActiveIndex', value)
      },
    },
  }
</script>

<style scoped>
  * {
    font-size: 15px;
    color: #0b0000;
    font-family: 'Microsoft Yahei', serif;
  }
</style>
