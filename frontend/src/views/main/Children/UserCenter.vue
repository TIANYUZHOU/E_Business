<template>
  <div id="userCenter">
    <!--个人资料------>
    <van-nav-bar
      title="个人资料"
      :fixed="true"
      :border="false"
      @click-left="onClickLeft"
      left-arrow
      style="height:2.5rem"
    />

    <!--头 像------>
    <div
      class="icon"
      style="margin-top: 60px;background-color: white;font-size: 16px;
display: flex;align-items: center;"
    >
      <span class="title">头像</span>
      <img id="myimgddd" src="./../../../../static/myimg/ddd3-03.png" alt />
    </div>

    <!--个人信息------>
    <van-cell-group id="groupxx">
      <van-cell title="昵称" is-link :value="xyz" @click="goToChangeNickName" />
      <van-cell title="性别" is-link :value="xyz" @click="onChangeSex" />
      <van-cell title="生日" is-link @click="selectBrithday" :value="xyz" />
      <van-cell title="手机号" :value="12345678945" />
    </van-cell-group>

    <!--退出登陆------>
    <van-button size="large" style="margin-top:1rem" @click="logOut">退出登录</van-button>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
import { Toast } from 'vant'
  export default {
    data() {
      return {
        xyz: '暂不填写',
      }
    },
    created() {},
    mounted() {
      
    },
    methods: {
      onClickLeft() {
        this.$router.back()
      },
      ...mapMutations(["CLEAR_CART","RESET_USER_INFO"]),
      logOut() {
        this.RESET_USER_INFO()
        this.CLEAR_CART()
        alert("退出登陆成功！")
        Toast({
          message:"退出登陆成功",
          duration: 500
        })
        this.$router.push("/dashboard/main")
      }
    },
  }
</script>

<style lang="less" scoped>
  #ppp {
    width: 450px;
  }
  #myimgddd {
    width: 50px;
    height: 50px;
  }
  #userCenter {
    position: fixed;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    background-color: #f5f5f5;
    z-index: 999;
    .icon {
      display: flex;
      height: 3rem;
      width: 100%;
      margin-top: 3rem;
      padding: 0 16px;
      background-color: #ffffff;
      align-items: center;
      .title {
        height: 3rem;
        line-height: 3rem;
        color: #323233;
        font-size: 14px;
      }
      img {
        position: absolute;
        right: 1.6rem;
        height: 2.5rem;
        width: 2.5rem;
      }
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
    #groupxx {
      width: 500px;
    }
    .van-cell {
      margin-left: -95px;
    }
    .van-cell_title {
      color: red;
    }
  }
</style>
