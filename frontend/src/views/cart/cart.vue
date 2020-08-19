<template>
  <div id="cart">
    <!--头部区域-->
    <header class="titleWrapper">
      <button id="mymycart">购物车</button>
      <button
        class="
        button-small
        button-caution
        button-pill
        button-box
"
        @click="clearCart()">清空购物车</button>
    </header>
    <div class="contentWrapper">
      <!--中间内容-->
      <main class="contentWrapperList">
        <section>
          <div
            class="shopCartListCon"
            v-for="(goods,index) in shopCart"
            :key="index"
          >
            <div class="left">
              <a href="javascript:;" class="cartCheckBox" @click.prevent="singerGoodsSelected(goods.id)" :checked="goods.checked"></a>
            </div>
            <div class="center">
              <img :src="goods.small_image" alt />
            </div>
            <div class="right">
              <a href="#">{{goods.name}}</a>
              <div class="bottomContent">
                <p class="shopPrice">&yen;{{goods.price}}</p>
                <div class="shopDeal">
                  <span @click="removeOutCart(goods.id,goods.num)">-</span>
                  <input disabled type="number" v-model="goods.num" />
                  <span @click="addToCart(goods.id,goods.name,goods.small_image,goods.price)">+</span>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
      <!--底部通栏-->
      <div class="tabBar">
        <div class="tabBarLeft">
          <a
            href="javascript:;"
            class="cartCheckBox"
            :checked="isSelectedAll"
            @click.prevent="selectedAll(isSelectedAll)"
          ></a>
          <span style="font-size: 16px;">全选</span>
          <div class="selectAll">
           <span style="font-size: 14px;">合计：</span>
            <span class="totalPrice">{{totalPrice | moneyFormat}}</span>
          </div>
        </div>
        <div class="tabBarRight">
          <a href="#" class="pay" @click.prevent="toPay">去结算({{goodsCount}})</a>
        </div>
      </div>
      <hr>
    </div>
  </div>
</template>

<script>
  import { Dialog, Toast } from 'vant'
  //监听
  import PubSub from 'pubsub-js'
  import { mapState, mapMutations } from 'vuex'
  export default {
    name: 'Cart',
    data() {
      return {
        isEmptyCart: false,
      }
    },
    computed: {
      ...mapState(['shopCart']),
      totalCount() {
        return Object.keys(this.shopCart).length
      },
      isShowEmptyCart() {
        let isshow = false
        if (this.totalCount > 0) {
          isshow = true
          this.isEmptyCart = isshow
          // console.log(isShowEmptyCart)
        }
        return isshow
      },
      isSelectedAll() {
        let goodsCount = Object.values(this.shopCart).length
        let tag = goodsCount > 0
        Object.values(this.shopCart).forEach((goods, index) => {
          if (!goods.checked) {
            tag = false
          }
        })
        return tag
      },
      totalPrice() {
        let totalPrice = 0
        Object.values(this.shopCart).forEach((goods, index) => {
          if (goods.checked) {
            totalPrice += goods.price * goods.num
          }
        })
        return totalPrice
      },
      goodsCount() {
        let selectedGoodsCount = 0
        Object.values(this.shopCart).forEach((goods, index) => {
          if (goods.checked) {
            selectedGoodsCount += 1
          }
        })
        return selectedGoodsCount
      },
    },
    methods: {
      ...mapMutations([
        'REDUCE_CART',
        'ADD_GOODS',
        'CLEAR_CART',
        'INIT_SHOP_CART',
        'SELECTED_SINGER_GOODS',
        'SELECTED_All_GOODS',
      ]),
      removeOutCart(goodsId, goodsNum) {
        if (goodsNum > 1) {
          this.REDUCE_CART({ goodsId })
        } else if (goodsNum === 1) {
          Dialog.confirm({
            title: '只剩最后一个了！',
            message: '确认删除吗?',
          })
            .then(() => {
              // on confirm
              this.REDUCE_CART({ goodsId })
            })
            .catch(() => {
              // on cancel
            })
        }
      },
      addToCart(goodsId, goodsName, smallImage, goodsPrice) {
        this.ADD_GOODS({ goodsId, goodsName, smallImage, goodsPrice })
      },
      clearCart() {
        Dialog.confirm({
          title: '清空购物车！',
          message: '确认清空购物车吗？',
        })
          .then(() => {
            // on confirm
            this.CLEAR_CART()
          })
          .catch(() => {
            // on cancel
          })
      },
      singerGoodsSelected(goodsId) {
        this.SELECTED_SINGER_GOODS({ goodsId })
      },
      selectedAll(isSelected) {
        this.SELECTED_All_GOODS({ isSelected })
      },
      toPay() {
        if (this.totalPrice > 0) {
          this.$router.push('/confirmOrder')
        } else {
          Toast({
            message: '请先选择商品再未结算~',
            duration: 1000,
          })
        }
      },
    },
    created() {
      this.INIT_SHOP_CART()
    },
  }
</script>

<style scoped>
.button-box{
  width:70px;
  margin-left: 20%
}
  #cart {
    width: 100%;
    height: 100%;
    background-color: #f5f5f5;
  }
  #mymycart {
    background-color: white;
    color: #000000;
    font-size: 18px;
    align-content: center;
    margin-left: 45%;
  }

  .titleWrapper {
    width: 100%;
    height: 2.6rem;
    background: #fff;
    -webkit-background-size: 0.1rem 4.4rem;
    background-size: 0.1rem 4.4rem;
    position: fixed;
    left: 0;
    top: 0;
    z-index: 999;
    display: flex;
    justify-content: center;
    align-items: center;
    border-bottom: 0.01rem solid #e0e0e0;
  }

  .contentWrapper {
    padding-top: 2.5rem;
  }

  /*列表内容*/
  .contentWrapperList {
    padding-bottom: 6rem;
  }
  .contentWrapperList section {
    background-color: #fff;
  }

  .cartCheckBox {
    background: url("./img/未选中.png") no-repeat;
    background-size: 1rem 1rem;
    width: 1rem;
    height: 1rem;
  }

  .cartCheckBox[checked] {
    background: url("./img/选中.png") no-repeat;
    background-size: 1rem 1rem;
  }

  .shopCartListCon {
    display: flex;
    height: 6rem;
    border-bottom: 0.01rem solid #e0e0e0;
    margin-bottom: 0.7rem;
    padding: 0.5rem 0;
  }

  .shopCartListCon .left {
    /*background: purple;*/
    flex: 1;
    display: flex;
    /*justify-content: center;*/
  }

  .shopCartListCon .left a {
    display: inline-block;
    margin-top: 0.8rem;
    margin-left: 0.5rem;
    width: 1.2rem;
    height: 1.2rem;
  }

  .shopCartListCon .center {
    /*background: blue;*/
    flex: 3;
  }

  .shopCartListCon .center{
    width: 100%;
    height: 100%;
    overflow: hidden;
  }

/*.center{*/
/*  border: solid #96C2F1;*/
/*  background-color:#EFF7FF;*/
/*  border-width:2px 2px 6px 2px;*/
/*  box-shadow:1px 1px 5px grey;*/
/*}*/
img{
  width: 75px;
  border: solid #96C2F1;
  border-width:2px 2px 6px 2px;
  box-shadow:1px 1px 5px #83a4d7;
}

  .shopCartListCon .right {
    /*background: orangered;*/
    flex: 6;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    margin-left: 0.5rem;
    margin-right: 0.5rem;

    position: relative;
  }

  .shopCartListCon .right a {
    height: 2.2rem;
    line-height: 1.2rem;
    overflow: hidden;
    margin-bottom: 0.3rem;
    font-size: 0.8rem;
    color: #000;
  }

  .shopCartListCon .bottomContent {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }

  .shopCartListCon .bottomContent .shopPrice {
    font-size: 0.8rem;
  }

  .shopCartListCon .right .shopDeal span {
    /* display: inline-block; */
    font-size: 28px;
    width: 1rem;
    height: 1.2rem;
    line-height: 1.2rem;
    text-align: center;
    float: left;
  }

  .shopCartListCon .right .shopDeal input {
    float: left;
    width: 2rem;
    height: 1.2rem;
    text-align: center;
    margin: 0 0.2rem;
    font-size: 0.8rem;
  }

  /*底部通栏*/
  .tabBar {
    position: fixed;
    left: 0;
    bottom: 3.2rem;
    height: 2.8rem;
    width: 100%;
    background-color: #fff;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top: 0.01rem solid #e0e0e0;
  }

  .tabBarLeft {
    display: flex;
    align-items: center;
    margin-left: 0.5rem;
  }
  .tabBarLeft>a{
    width: 1.2rem;
    height: 1.2rem;
  }

  .tabBarLeft .selectAll {
    margin-left: 1rem;
    font-size: 0.8rem;
  }

  .totalPrice {
    color: #e9232c;
  }

  .tabBarRight .pay {
    width: 5rem;
    height: 1.5rem;
    background-color: #e9232c;
    border-radius: 1rem;
    margin-right: 0.5rem;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 0.9rem;
    color: #fff;
  }
</style>
