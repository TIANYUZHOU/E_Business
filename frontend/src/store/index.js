import Vue from "vue";
import Vuex from "vuex";
import actions from "./actions";
import getters from "./getters";
import mutations from "./mutations"
Vue.use(Vuex);

import { getStore, setStore, removeStore } from "../../config/global";
import {
  INIT_SHOP_CART,
  REDUCE_CART,
  SELECTED_All_GOODS,
  SELECTED_SINGER_GOODS
} from "./mutations-type";
Vue.config.devtools = true;

export default new Vuex.Store({
  state: {
    // count: 210,

    // mytoken: {
    //   phone: "15323441764",
    //   token: "df12e8b98bcb48fa83d44c4eb025474d",
    //   user_id: "83",
    //   username: "15323441764"
    // },
    // Userinfo: {},
    // shopCart: {}

    userInfo: {
      token: ""
    },
    shopCart: {}
  },
  

  // mutations: {
  //   add(state, sep) {
  //     //放参
  //     state.mytoken = sep;
  //     // alert("vuex中mytoken写入完毕")
  //   },

  //   // 1. 往购物车中添加数据
  //   ADD_GOODS(state, { goodsId, goodsName, smallImage, goodsPrice }) {
  //     //商品ID,name,小图,价格
  //     let shopCart = state.shopCart;
  //     // 1.1 判断商品是否存在
  //     if (shopCart[goodsId]) {
  //       // 存在
  //       shopCart[goodsId]["num"]++;
  //     } else {
  //       // 不存在
  //       shopCart[goodsId] = {
  //         num: 1,
  //         id: goodsId,
  //         name: goodsName,
  //         small_image: smallImage,
  //         price: goodsPrice,
  //         checked: true
  //       };
  //     }
  //     // 1.2  产生新对象
  //     state.shopCart = { ...shopCart };
  //     // state.shopCart =shopCart
  //     // 1.3 存入本地
  //     setStore("shopCart", state.shopCart);
  //   },

  //   // // 1. 往购物车中添加数据
  //   // myADD_GOODS(state, { goodsId, goodsName, smallImage, goodsPrice }) {
  //   //   //商品ID,name,小图,价格
  //   //   let shopCart = state.shopCart;
  //   //   // 1.1 判断商品是否存在
  //   //   if (shopCart[goodsId]) {
  //   //     // 存在
  //   //     shopCart[goodsId]["num"]++;
  //   //   } else {
  //   //     // 不存在
  //   //     shopCart[goodsId] = {
  //   //       num: 1,
  //   //       id: goodsId,
  //   //       name: goodsName,
  //   //       small_image: smallImage,
  //   //       price: goodsPrice,
  //   //       checked: true
  //   //     };
  //   //   }
  //   //   // 1.2  产生新对象
  //   //   state.shopCart = { ...shopCart };
  //   //   // 1.3 存入本地
  //   //   setStore("shopCart", state.shopCart);
  //   // },

  //   // 添加商品进购物车
  //   ADD_TO_CART(state, goods) {},
  //   // 清空购物车(本地和vuex同时)----------mapmutations内

  //   //清空用户信息(本地和vuex同时)----------mapmutations内

    // CLEAR_USER_DATA(state) {
    //   state.mytoken = {};
    //   removeStore("userdata");
    // },
  //   //函数

  //   // 3. 购物车---减
  //   REDUCE_CART(state, { goodsId }) {
  //     let shopCart = state.shopCart;
  //     let goods = shopCart[goodsId];
  //     if (goods) {
  //       // 找到该商品
  //       if (goods["num"] > 0) {
  //         goods["num"]--;
  //         // 3.1 判断是否只有0个
  //         if (goods["num"] === 0) {
  //           delete shopCart[goodsId];
  //         }
  //       } else {
  //         goods = null;
  //       }
  //       // 3.2 同时数据
  //       state.shopCart = { ...shopCart };
  //       setStore("shopCart", state.shopCart);
  //     }
  //   },

    // 6. 清空购物车
    // CLEAR_CART(state) {
    //   state.shopCart = null;
    //   state.shopCart = {
    //     ...state.shopCart
    //   };
    //   setStore("shopCart", state.shopCart);
    // },

  //   // 2. 页面初始化，获取购物车的数据(本地)
  //   Initialization(state) {
  //     let initCart = getStore("shopCart");
  //     if (initCart) {
  //       state.shopCart = JSON.parse(initCart);
  //     }
  //   },

  //   SELECT_ONE(state, { goodsId }) {
  //     let shopCart = state.shopCart;
  //     let goods = shopCart[goodsId];
  //     if (goods) {
  //       if (goods.checked) {
  //         // 存在该属性
  //         goods.checked = !goods.checked;
  //       } else {
  //         Vue.set(goods, "checked", true);
  //         // goods.checked = true;
  //       }
  //       // 4.1 同时数据
  //       state.shopCart = { ...shopCart };
  //       setStore("shopCart", state.shopCart);
  //     }
  //   },

  //   //所有商品选中和取消选中
  //   SELECTED_All(state, { isSelected }) {
  //     let shopCart = state.shopCart;
  //     Object.values(shopCart).forEach((goods, index) => {
  //       if (goods.checked) {
  //         // 存在该属性
  //         goods.checked = !isSelected;
  //       } else {
  //         Vue.set(goods, "checked", !isSelected);
  //       }
  //     });
  //     state.shopCart = { ...shopCart };
  //   }
  // },
  mutations,
  actions,
  getters
}); //最后的括号
