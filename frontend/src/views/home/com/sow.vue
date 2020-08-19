<template>
  <div class="luobo">
    <swiper id="ppj" ref="mySwiper" :options="swiperOptions">
      <swiper-slide>
        <img src="../../../../static/myimg/sony~1.jpg" />
      </swiper-slide>
      <swiper-slide>
        <img src="../../../../static/myimg/canon~2.jpg" />
      </swiper-slide>
      <swiper-slide>
        <img src="../../../../static/myimg/nikon~1.jpg" />
      </swiper-slide>
      <swiper-slide>
        <img src="../../../../static/myimg/fujifilm~1.jpg" />
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
    </swiper>

  </div>
</template>

<script>
  import { Swiper, SwiperSlide, directive } from 'vue-awesome-swiper'
  import 'swiper/dist/css/swiper.css'   //这个目录是从node_modules文件夹引入
  export default {
    data() {
      return {
        swiperOptions: {
          notNextTick: true,
          loop: true,
          delay: 1000,
          speed: 100,
          autoplay: {
            //加了它,就自动运行了
            stopOnLastSlide: true,
            disableOnInteraction: false
          },
          pagination: {
            el: '.swiper-pagination',
            clickable: true
          }
          // Some Swiper option/callback...
        }
      }
    },
    computed: {
      swiper() {
        return this.$refs.mySwiper.$swiper
      }
    },
    mounted() {
      console.log('Current Swiper instance object', this.swiper)
      this.swiper.slideTo(3, 1000, false)
    },
    components: {
      Swiper,
      SwiperSlide
    },
    directives: {
      swiper: directive
    }
  }
</script>

<style scoped>
img{
  width:100%;
  height: auto;
}
.luobo{
  margin-top: 3.125rem;
}
  #wai {
    width: 414px;
    height: 250px;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  #jpg55 {
    width: 418px !important;
    height: 250px;
  }
  #ppx {
    /*轮播图大小*/
    width: 100%;
    height: 220px;
  }
  #mydiv {
    /*这里如果不放这个margin,则定位会把轮播盖住*/
    margin-top: 0px;
    width: 100%;
    height: 220px;
    background-color: orangered;
  }
  #myswi {
    width: 100%;
    height: 500px;
  }
  #ppj >>> .swiper-pagination-bullet-active {
    background-color: #907cc8 !important;
  }
</style>
