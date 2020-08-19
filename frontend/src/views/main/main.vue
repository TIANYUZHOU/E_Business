<template>
  <div id="mine">
    <van-nav-bar id="mybar" title="我的" :fixed="true" :border="false" style="height:2.5rem;" />

    <van-cell-group style="margin-top:2.4rem">
      <van-cell
        style="background-color: #fac674;color:#FFF;"
        label-class="labelClass"
        is-link
        center
      >
        <template slot="title">
          <!-- 已登录状态     用token来控制到底显示登陆还是没登陆 -->
          <div class="personMsg" v-if="userInfo.token" @click="goToUserCenter">
            <img class="iconImage" src="./../../../static/myimg/ddd3-03.png" alt />
            <div class="sex" v-if="true">
              <img src alt />
            </div>
            <div class="personInfo" v-if="true">
              <span id="myspanlsd">myname</span>
              <span>手机号：15362355654</span>
            </div>
          </div>
          <!-- 未登录状态 用token来控制到底显示登陆还是没登陆 和上面相反 -->
          <div class="personMsg" v-if="!userInfo.token">
            <img class="iconImage" src="./../../../static/myimg/ddd3-03.png" alt />
            <div class="personInfo" v-if="true">
              <div @click="login">立即登录</div>
            </div>
          </div>
        </template>
      </van-cell>
    </van-cell-group>

    <!-- 订单相关-->
    <van-cell-group>
      <van-cell
        id="mytitlex"
        title="我的订单"
        icon="label"
        value="查看全部订单"
        is-link
        @click="goTomyOrder(-1)"
      ></van-cell>
      <van-grid :border="false">
        <van-grid-item
          v-for="(order, index) in orderData"
          :key="index"
          :icon="order.icon"
          :text="order.title"
          @click="goTomyOrder(index)"
        />
      </van-grid>
    </van-cell-group>

    <van-cell-group style="margin-top:0.4rem">
      <van-cell
        title="我的优惠券"
        icon="gold-coin"
        :value="true ? '2张' : ''"
        @click="goToMyCouponList"
        is-link
      />
      <van-cell title="我的收货地址" icon="todo-list" is-link @click="goToMyAddredd" />
    </van-cell-group>

    <van-cell-group style="margin-top:0.4rem">
      <van-cell is-link icon="vip-card" @click="goToMyVip">
        <template slot="title">
          <span class="custom-title">我的绿卡</span>
          <van-tag type="danger" :round="true">NEW</van-tag>
        </template>
      </van-cell>
    </van-cell-group>

    <van-cell-group style="margin-top:0.4rem">
      <van-cell title="联系客服" icon="phone" value="客服时间 07:00-22:00" is-link />
      <van-cell title="意见反馈" icon="comment-circle" is-link @click="onFeedBack" />
    </van-cell-group>

    <div class="version">当前版本3.0</div>
    <!--路由的出口-->

    <router-view />
  </div>
</template>

<script type="text/javascript">
  // 引入vuex
  import { mapState } from 'vuex'
  import { Dialog } from 'vant'
  import { _VERSION_ } from './../../configs/global'

  export default {
    data() {
      return {
        // 头像
        user_image: {
          login_icon: null, // require('./../../../myimg/ddd3-03.png'),
          noLogin_icon: null, //require('./../../images/login/grey.jpg'),
          female: null, //require('./../../images/mine/female.png'),
          male: null, // require('./../../images/mine/male.png')
          token: true,
        },
        // 订单状态
        orderData: [
          { icon: 'cart-circle-o', title: '待支付' },
          { icon: 'gift-o', title: '待收货' },
          { icon: 'smile-comment-o', title: '待评价' },
          { icon: 'cash-back-record', title: '售后/退款' },
        ],
        version: _VERSION_, // 版本信息
      }
    },
    computed: {
      ...mapState(['userInfo']),
      phoneNumber() {
        // 设置隐藏手机号中间四位
        var mobile = String(this.userInfo.phone)
        var reg = /^(\d{3})\d{4}(\d{4})$/
        return mobile.replace(reg, '$1****$2')
      },
      userInfoSex() {
        if (this.userInfo.sex == '1') {
          return this.user_image.female
        } else if (this.userInfoSex.sex == '2') {
          return this.user_image.male
        } else {
          return ''
        }
      },
    },
    components: {},
    methods: {
      // 跳转到登录界面
      login() {
        this.$router.push('/login')
      },
      // 跳转到用户中心
      goToUserCenter() {
        // alert(123);
        this.$router.push({ name: 'userCenter' })
      },
      // 跳转到我的订单
      goTomyOrder(index) {
        if (this.userInfo.token) {
          if (index == 3) {
            // 跳转到售后退款界面
          } else {
            this.$router.push({ name: 'myOrder', params: { active: index + 1 } })
          }
        } else {
          this.login()
        }
      },
      // 跳转到我的优惠券
      goToMyCouponList() {
        // 判断是否登录
        if (this.userInfo.token) {
          this.$router.push({ name: 'couponList' })
        } else {
          this.login()
        }
      },
      // 跳转到我的收货地址
      goToMyAddredd() {
        // 判断是否登录
        if (this.userInfo.token) {
          this.$router.push({ name: 'myAddress' })
        } else {
          this.login()
        }
      },
      // 跳转到绿卡会员
      goToMyVip() {
        if (this.userInfo.token) {
          this.$router.push('/dashboard/Mine/myVip')
        } else {
          this.login()
        }
      },
      // 意见反馈
      onFeedBack() {
        Dialog.alert({
          confirmButtonText: '记得点个小星❤️哦~',
          title: '💘感谢您的关注💘',
          message: 'GitHub上搜索 \nGeek-James/ddBuy \n🦉欢迎提出优化建议🙉',
        }).then(() => {
          // on close
        })
      },
    },
  }
</script>

<style lang="less" scoped>
  #mine {
    width: 100%;
    background-color: #f5f5f5;
    margin-bottom: 3rem;
    .version {
      margin: 0 auto;
      text-align: center;
      font-size: 0.6rem;
      background-color: #ffffff;
      height: 2rem;
      color: grey;
      line-height: 2rem;
    }
    .van-nav-bar {
      background-color: #fac674;
      font-size: 0.6rem;
      color: #fdfbfb;
    }
    .van-nav-bar__title {
      color: white;
    }
    .personMsg {
      display: flex;
      align-items: center;
      .sex {
        position: absolute;
        top: 3.5rem;
        left: 3.8rem;
        width: 0.1rem;
        height: 0.1rem;
        img {
          width: 1rem;
          height: 1rem;
        }
      }
      img {
        width: 4rem;
        height: 4rem;
        border-radius: 50%;
      }

      .personInfo {
        display: flex;
        flex-direction: column;
        //align-items: left;
        margin-left: 0.8rem;
      }
    }

    .van-cell__left-icon {
      color: #ef6e49;
      font-size: 1.2rem;
    }
    /*转场动画*/
    .router-slider-enter-active,
    .router-slider-leave-active {
      transition: all 0.3s;
    }

    .router-slider-enter,
    .router-slider-leave-active {
      transform: translate3d(2rem, 0, 0);
      opacity: 0;
    }
  }
  #myspanlsd {
    margin-left: -78px;
  }
  #mybar {
    color: white;
  }
  #mytext {
    color: white;
  }

  /* 加了这一句,所有左边的字,靠边整齐排列,ok*/
  .van-cell__title span {
    float: left;
  }
</style>
