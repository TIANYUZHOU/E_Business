 <template>
  <div id="category">
    <!--头部-->
    <Header></Header>
    <!--内容-->
    <div class="listWrapper" v-if="!isShowLoading">
      <!--左边-->
      <div class="leftWrapper">
        <ul class="wrapper">
          <li
            class="categoryItem"
            v-for="(cate, index) in leftdata"
            :class="{selected: currentIndex === index}"
            @click="clickLeftLi(index,cate.id)"
            :key="cate.id"
            ref="menuList"
          >
            <span class="textWrapper">{{cate.title}}</span>
          </li>
        </ul>
      </div>
      <!--右边-->
      <ContentView :right_data="right_data" />
    </div>
    <!-- 加载动画 -->
    <Loading :show="isShowLoading" />
    <!-- 点击左边按钮加载数据时候显示动画 -->
    <LoadingGif v-show="isShowLoadingGif" />
  </div>
</template>

<script>
  import { mapMutations } from 'vuex'
  //监听
  import PubSub from 'pubsub-js'
  // 1. 引入组件
  import Header from './com/Header'
  import ContentView from './com/Conleftitem'
  // 2. 引入滚动组件
  import BScroll from 'better-scroll'
  // 3. 引入接口
  import { getCategoryData, getCategoryDetailData } from './../../serve/api/index'
  // 4.引入加载动画
  import Loading from '../../components/loading/LoadingGif'
  // 5.引入加载动画
  import LoadingGif from '../../components/loading/Loading'
  import { Toast } from 'vant'
  export default {
    name: 'Category',
    data() {
      return {
        // 是否显示加载图标
        isShowLoading: true,
        // 左边列表数据
        leftdata: [],
        // 右边列表数据
        right_data: [],
        // 左边item选中与否
        currentIndex: 0,
        isShowLoadingGif: false,
        myid: 1, //默认中药的id
      }
    },
    created() {
      this.getCategoryData()
      this.xyz()
    },
    mounted() {
      //监听添加到购物车的消息
      PubSub.subscribe('homeAddToCart3', (msg, goods) => {
        if (msg === 'homeAddToCart3') {
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
      // 初始化数据
      this._initData()
      // 处理首页点击显示对应的列表数据
      setTimeout(() => {
        if (this.$route.params.currentIndex > -1) {
          this.clickLeftLi(this.$route.params.currentIndex + 1)
        }
      }, 800)
    },
    components: {
      Header,
      ContentView,
      Loading,
      LoadingGif,
    },
    methods: {
      ...mapMutations(['ADD_GOODS']),
      //左侧分类栏提数据
      getCategoryData: function () {
        this.axios.get('/api/get_cg').then((response) => {
          this.leftdata = response.data
          // console.log(response.data);
        })
      },
      //右侧商品提数据_根据左侧分类id
      xyz: function () {
        //测试接口,取右侧数据
        let jj = '/api/assign_cg_pd/' + this.myid
        this.axios.get(jj).then((response) => {
          this.right_data = response.data
          // console.log("测试数据");
          // console.log(response.data);
        })
      },

      // 1. 初始化操作(数据和界面)
      async _initData() {
        // 1.1 获取左边的数据
        let leftRes = await getCategoryData()
        if (leftRes.success) {
          // this.categoriesData = leftRes.data.cate;
        }
        // 1.2 获取右边的数据
        let rightRes = getCategoryDetailData('/aaa')
        if (rightRes.success) {
          // this.categoriesDetailData = rightRes.data.cate;
        }
        // 1.3. 隐藏loading框
        this.isShowLoading = false

        // 1.4.初始化滚动视图
        this.$nextTick(() => {
          if (!this.leftScroll) {
            this.leftScroll = new BScroll('.leftWrapper', {
              probeType: 3,
              click: true,
              scrollY: true,
              tap: true,
              mouseWheel: true,
            })
          } else {
            this.leftScroll.refresh()
          }
        })
      },
      // 2. 处理左边的点击
      clickLeftLi(index, id) {
        //alert(index);//弹点击的分类在数组中的下标
        //alert(id);//弹出所点击的分类在数据库中的id
        this.myid = id
        this.xyz() //再次取数据,不然,虽然myid变了,但函数没有调用,不行
        this.isShowLoadingGif = true
        // 2.1 改变索引
        this.currentIndex = index
        // 2.2 滚动到对应的位置
        setTimeout(() => {
          let menuLists = this.$refs.menuList
          let el = menuLists[index]
          // 2.3 滚动到对应元素上
          this.leftScroll.scrollToElement(el, 300)
        }, 800)

        // 2.4 获取右边的数据
        let param
        if (index >= 9) {
          param = `/lk0${index + 1}`
        } else {
          param = `/lk00${index + 1}`
        }
        let rightRes = getCategoryDetailData(param)
        if (rightRes.success) {
          // this.categoriesDetailData = rightRes.data.cate;
        }
        this.isShowLoadingGif = false
      },
    },
  }
</script>

<style scoped>
  #category {
    width: 100%;
    height: 100%;
    background-color: #f5f5f5;
    overflow: hidden;
  }

  .listWrapper {
    display: flex;
    position: absolute;
    top: 2.75rem;
    bottom: 3rem;
    width: 100%;
    overflow: hidden;
  }

  .leftWrapper {
    background-color: #f4f4f4;
    width: 5.3125rem;
    flex: 0 0 5.3125rem;
  }

  .categoryItem {
    padding: 0.75rem 0;
    border-bottom: solid 0.01rem #e8e9e8;
    position: relative;
  }

  .categoryItem .textWrapper {
    line-height: 1.25rem;
    border-left: solid 0.1875rem transparent;
    padding: 0.3125rem 0.6875rem;
    font-size: 0.8125rem;
    color: #666666;
  }

  .categoryItem.selected {
    background: #fff;
  }

  .categoryItem.selected .textWrapper {
    border-left-color: #3cb963;
    font-weight: bold;
    font-size: 0.875rem;
    color: #333333;
  }

  @media (min-width: 960px) {
    .wrapper {
      border-right: 0.01rem solid #e8e9e8;
    }

    .wrapper .categoryItem {
      background: #fff;
    }
  }
</style>
