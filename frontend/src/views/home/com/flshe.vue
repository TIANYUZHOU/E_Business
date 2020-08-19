<template>
  <div id="wrapper">
    <div class="titleWrapper" id="ttpx">
      <div class="title">限时抢购</div>
      <count-down
        v-on:start_callback="countDownS_cb(1)"
        v-on:end_callback="countDownE_cb(1)"
        :currentTime="68400000"
        :startTime="72000000"
        :endTime="75600000"
        :tipText="'距离开始文字1'"
        :tipTextEnd="'距离结束文字1'"
        :endText="'结束自定义文字2'"
        :dayTxt="'天'"
        :hourTxt="'小时'"
        :minutesTxt="'分钟'"
        :secondsTxt="'秒'"
      ></count-down>
      <!-- 更多按钮 -->
      <div class="more">更多</div>
    </div>
  </div>
</template>

<script>
  import CountDown from 'vue2-countdown'
  export default {
    data() {
      return {
        // 倒计时时间设置
        time: 1 * 60 * 1000 * 100
      }
    },
    components: { CountDown },
    methods: {
      countDownS_cb: function(x) {
        console.log(x)
      },
      countDownE_cb: function(x) {
        console.log(x)
      }
    }
  }
</script>

<style scoped>
  #ttpx {
    display: flex;
    font-size: 16px;
    align-items: center;
    justify-content: space-between;
    color: rgb(221, 94, 94);
  }
  #wrapper {
    margin-top: 0px;
    padding: 1.25rem 0 0.9375rem 0;
    background-color: white;
  }

  .titleWrapper {
    margin: 0 0.625rem 0.625rem 0.625rem;
    height: 1.5625rem;
  }

  .title {
    display: inline-block;
    border-left: 4px #907cc8 solid;
    padding-left: 0.3125rem;
    height: 1.3125rem;
    line-height: 1.3125rem;
    vertical-align: middle;
    font-size: 16px;
    color: black;
  }

  .item {
    display: inline-block;
    width: 22px;
    margin-right: 5px;
    color: #fff;
    font-size: 12px;
    text-align: center;
    background-color: #1989fa;
  }

  .countStyle {
    float: left;
    margin-left: 0.7rem;
  }

  .more {
    color: #907cc8;
    float: right;
    font-size: 0.8rem;
  }
</style>
