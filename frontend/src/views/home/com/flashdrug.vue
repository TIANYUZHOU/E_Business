<template>
  <div id="flashFood">
    <div class="flashItemwrapper">
      <ul class="itemWrapper" ref="ulWrapper">
        <li
          class="itemInCovers"
          v-for="(product, index) in flash_sale_product_list"
          :key="index"
          ref="productItem"
        >
          <img :src="product.small_image" class="itemImage" />
          <span class="title">{{ product.name }}</span>
          <div class="price">
            <p class="nowPrice">{{ product.price | moneyFormat}}</p>
            <p class="originPrice">{{ product.origin_price | moneyFormat }}</p>
            <div class="buyCar" @click="addToCart2(product)">
              <svg viewBox="0 0 52 52" class="icon icon-60">
                <defs>
                  <radialGradient
                    cx="27.0288363%"
                    cy="10.3693483%"
                    fx="27.0288363%"
                    fy="10.3693483%"
                    r="93.8427229%"
                    id="radialGradient-1"
                  >
                    <stop stop-color="#4ECA75" offset="0%" />
                    <stop stop-color="#39B460" offset="100%" />
                  </radialGradient>
                </defs>
                <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd">
                  <g transform="translate(-678.000000, -2742.000000)">
                    <g transform="translate(678.000000, 2742.000000)">
                      <rect
                        fill="url(#radialGradient-1)"
                        x="0"
                        y="0"
                        width="51.8699976"
                        height="51.8699976"
                        rx="25.9349988"
                      />
                      <path
                        fill="#FFFFFF"
                        d="M20.3666667,39 C19.1700497,39 18.2,38.0299503 18.2,36.8333333 C18.2,35.6367164 19.1700497,34.6666667 20.3666667,34.6666667 C21.5632836,34.6666667 22.5333333,35.6367164 22.5333333,36.8333333 C22.5333333,38.0299503 21.5632836,39 20.3666667,39 Z M33.3666667,38.1333333 C32.1700497,38.1333333 31.2,37.1632836 31.2,35.9666667 C31.2,34.7700497 32.1700497,33.8 33.3666667,33.8 C34.5632836,33.8 35.5333333,34.7700497 35.5333333,35.9666667 C35.5333333,37.1632836 34.5632836,38.1333333 33.3666667,38.1333333 Z"
                      />
                      <path
                        stroke="#FFFFFF"
                        stroke-width="2.6"
                        stroke-linecap="round"
                        d="M12.1333333,13.8666667 L13.6768756,13.8666667 C15.4621209,13.8666667 16.9554584,15.222463 17.1274221,16.9994069 L18.2224287,28.314386 C18.4068512,30.2200702 20.1012175,31.6154285 22.0069016,31.431006 C22.0111286,31.4305969 22.0153548,31.4301801 22.0195802,31.4297555 L33.2997819,30.296256 C34.7947282,30.1460352 36.0227397,29.0499108 36.3411182,27.581556 L37.8958814,20.4110205 C38.0987345,19.4754663 37.5047629,18.5526049 36.5692087,18.3497518 C36.3853963,18.3098964 36.1963225,18.3002236 36.0094025,18.3211126 L22.8968424,19.7864909"
                      />
                    </g>
                  </g>
                </g>
              </svg>
            </div>
          </div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
  import BScroll from 'better-scroll'
  import PubSub from 'pubsub-js'
  export default {
    data() {
      return {
        flash_sale_product_list: [
          {
            id: 0,
            small_image: '../../../../static/img2/k1.jpg',
            name: '2盒32元洗液春萌替硝唑栓6粒',
            price: '20',
            origin_price: '18'
          },
          {
            id: 1,
            small_image: '../../../../static/img2/k2.jpg',
            name: '感冒灵颗粒9袋装冲剂',
            price: '20',
            origin_price: '18'
          },
          {
            id: 2,
            small_image: '../../../../static/img2/k3.jpg',
            name: '3盒拜耳力度伸维生素C泡腾片',
            price: '20',
            origin_price: '18'
          },
          {
            id: 3,
            small_image: '../../../../static/img2/k4.jpg',
            name: '华中维生素B6片100片',
            price: '20',
            origin_price: '18'
          },
          {
            id: 4,
            small_image: '../../../../static/img2/k5.jpg',
            name: '普济堂人参归脾丸10丸',
            price: '20',
            origin_price: '18'
          },
          {
            id: 5,
            small_image: '../../../../static/img2/k6.jpg',
            name: '恒健开塞露20ml20支',
            price: '20',
            origin_price: '18'
          },
          {
            id: 6,
            small_image: '../../../../static/img2/k7.jpg',
            name: '白云山风油精3ml止痛驱风止痒晕车',
            price: '20',
            origin_price: '18'
          },
          {
            id: 7,
            small_image: '../../../../static/img2/k8.jpg',
            name: '乐天胃舒宁颗粒5g9袋盒药品',
            price: '20',
            origin_price: '18'
          },
          {
            id: 8,
            small_image: '../../../../static/img2/k9.jpg',
            name: '华南牌维生素B1片维生素B缺乏症',
            price: '20',
            origin_price: '18'
          },
          {
            id: 9,
            small_image: '../../../../static/img2/k10.jpg',
            name: '梁湖槐角丸药品200丸痔疮',
            price: '20',
            origin_price: '18'
          },
          {
            id: 10,
            small_image: '../../../../static/img2/k11.png',
            name: '独圣大山楂颗粒15g10袋盒',
            price: '20',
            origin_price: '18'
          },
          {
            id: 11,
            small_image: '../../../../static/img2/k12.jpg',
            name: '太极小儿止咳糖浆100ml1瓶盒',
            price: '20',
            origin_price: '18'
          }
        ]
      }
    },
    created() {
      //增加了这个函数,其它没变
      this.axios.get('/api/get_pd').then(response => {
        var ddd = response.data
        this.flash_sale_product_list = ddd

        // console.log(response.data);
      })
    },
    mounted() {
      this.$nextTick(() => {
        let contentWrapperWidth = 0
        let el = this.$refs.productItem
        for (let i = 0; i < el.length; i++) {
          contentWrapperWidth += el[i].clientWidth
        }
        // 给ul设置值
        this.$refs.ulWrapper.style.width = contentWrapperWidth + 'px'
        if (!this.scroll) {
          // 名字一定要唯一 和父组件独立
          this.scroll = new BScroll('.flashItemwrapper', {
            probeType: 2,
            startX: 0,
            click: true,
            scrollX: true,
            scrollY: false,
            eventPassthrough: 'vertical'
          })
        } else {
          this.scroll.refresh()
        }
      })
    },
    components: {},
    methods: {
      addToCart2(goods) {
        alert(goods.id)
        PubSub.publish("homeAddToCart2",goods)
      },


      beforeEnter(el) {
        // 设置transform值
        el.style.transform = `translate3d(${this.elLeft - 30}px,${this.elTop -
          100}px , 0)`
        // 设置透明度
        el.style.opacity = 0
      }
    }
  }
</script>

<style scoped>
  #flashFood .flashItemwrapper {
    width: 100%;
    overflow: hidden;
    position: relative;
  }
  #flashFood .flashItemwrapper .move_dot {
    position: fixed;
    z-index: 100;
    top: 1rem;
    height: 2rem;
    width: 2rem;
    /*border-radius: 50%;*/
  }

  #flashFood .flashItemwrapper .move_dot img {
    animation: 0.88s mymove ease-in-out;
    width: 3rem;
    height: 3rem;
    /*border-radius: 50%;*/
  }
  #flashFood .flashItemwrapper .itemWrapper {
    display: flex;
    justify-content: flex-start;
  }

  #flashFood .flashItemwrapper .itemInCovers {
    flex: 0 0 6rem;
    align-items: center;
    padding-right: 0.5rem;
  }
  #flashFood .flashItemwrapper .itemInCovers .itemImage {
    width: 100%;
    /*border-radius: 50%;*/
    background-size: contain;
  }
  .itemInCovers{
    border: solid whitesmoke;
    background-color: white;
    padding: 2px;
  }

  @keyframes mymove {
    0% {
      transform: scale(1);
    }
    25% {
      transform: scale(0.8);
    }
    50% {
      transform: scale(0.6);
    }
    75% {
      transform: scale(0.4);
    }
    100% {
      transform: scale(0.2);
    }
  }
  @-moz-keyframes mymove {
    0% {
      transform: scale(1);
    }
    25% {
      transform: scale(0.8);
    }
    50% {
      transform: scale(0.6);
    }
    75% {
      transform: scale(0.4);
    }
    100% {
      transform: scale(0.2);
    }
  }
  @-webkit-keyframes mymove {
    0% {
      transform: scale(1);
    }
    25% {
      transform: scale(0.8);
    }
    50% {
      transform: scale(0.6);
    }
    75% {
      transform: scale(0.4);
    }
    100% {
      transform: scale(0.2);
    }
  }
  @-o-keyframes mymove {
    0% {
      transform: scale(1);
    }
    25% {
      transform: scale(0.8);
    }
    50% {
      transform: scale(0.6);
    }
    75% {
      transform: scale(0.4);
    }
    100% {
      transform: scale(0.2);
    }
  }

  #flashFood .flashItemwrapper .itemInCovers .price {
    position: relative;
    padding-left: 0.5rem;
    text-align: left;
  }
  #flashFood .flashItemwrapper .itemInCovers .price .nowPrice {
    color: #f37078;
    font-size: 0.928rem;
  }
  #flashFood .flashItemwrapper .itemInCovers .price .originPrice {
    font-size: 0.6875rem;
    color: #999999;
    text-decoration: line-through;
  }
  #flashFood .flashItemwrapper .itemInCovers .price .buyCar {
    position: absolute;
    right: 0.1rem;
    top: 0.1rem;
    width: 1.5rem;
    height: 1.5rem;
  }
  #flashFood {
    font-size: 13px;
    height: auto;
  }
</style>
