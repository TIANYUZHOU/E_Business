import Vue from "vue";

// 人民币过滤器   //只显示.后2位,以后可以改
Vue.filter("moneyFormat", value => {
  return "¥" + Number(value).toFixed(2);
});
