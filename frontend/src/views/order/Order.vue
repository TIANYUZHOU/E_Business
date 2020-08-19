<template>
  <div class="out">
    <van-nav-bar
      title="结算"
      left-text="返回"
      right-text="按钮"
      left-arrow
      @click-left="onClickLeft"
      @click-right="onClickRight"
    />
    <!-- 联系人卡片 -->
    <van-contact-card
      :type="address_type"
      add-text="选择收货地址"
      :name="address_name"
      :tel="address_phone"
      @click="chooseaddress"
      />
    <div class="goodsinfo" v-for="(goods,index) in goods" :key="index">
      <div class="image">
        <img :src="goods.small_image" alt />
      </div>
      <span class="span1">{{goods.name}}</span>
      <span class="span2">共{{goods.num}}件</span>
    </div>
    <div class="span">
      <span>您选择了{{selectedCount}}种商品</span>
    </div>
    <div class="pay">
      <span>支付方式</span>
      <van-cell-group>
        <van-cell title="微信支付" icon="wechat">
          <template #right-icon>
            <van-icon name="circle" class="circle" size="18px" />
            <van-icon name="passed" class="circle" size="18px" />
          </template>
        </van-cell>
        <van-cell title="支付宝支付" icon="alipay">
          <template #right-icon>
            <van-icon name="circle" class="circle" size="18px" />
            <van-icon name="passed" class="circle" size="18px" />
          </template>
        </van-cell>
      </van-cell-group>
      <van-cell title="备注" style="margin: 10px 0 10px 0;">
        <span>填写备注</span>
      </van-cell>
      <van-cell-group>
        <van-cell title="商品金额">
          <span>{{selectedTotalPrice | moneyFormat }}</span>
        </van-cell>
        <van-cell title="配送费">
          <span>包邮</span>
        </van-cell>
      </van-cell-group>
    </div>
    <div class="submit">
      <van-submit-bar :price="selectedTotalPrice*100" button-text="提交订单" @submit="onSubmit" />
    </div>
    <router-view />
  </div>
</template>

<script>
  import { Toast } from 'vant'
  import { mapState, mapGetters } from 'vuex'
  import pubsub from 'pubsub-js'

  export default {
    data() {
      return {
        chosenContactId: null,
        editingContact: {},
        showList: false,
        showEdit: false,
        isEdit: false,
        address_type:"add",
        address_name:"",
        address_phone:"",
        address_id:"",
        list: [
          {
            name: '张三',
            tel: '13000000000',
            id: 0,
          },
        ],
      }
    },
    mounted() {
      pubsub.subscribe('userAddress',(msg,address) => {
        if(msg === 'userAddress') {
          // console.log(address.name)
          //修改卡片类型
          // console.log(address.tel)
          this.address_type = "edit"
          this.address_name = address.name
          this.address_phone = address.tel
          this.address_id = address.id
          // console.log(this.address_name)
        }
      })
    },
    computed: {
      cardType() {
        return this.chosenContactId !== null ? 'edit' : 'add'
      },

      currentContact() {
        const id = this.chosenContactId
        return id !== null ? this.list.filter((item) => item.id === id)[0] : {}
      },
      ...mapGetters({
        selectedCount: 'SELECTED_GOODS_COUNT',
        goods: 'SELECTED_GOODS',
        selectedTotalPrice: 'SELECTED_GOODS_PRICE',
      }),
    },
    methods: {
      onClickLeft() {
        this.$router.back()
        Toast('返回')
      },
      onClickRight() {
        Toast('按钮')
      },
      chooseaddress() {
        this.$router.push('myAddress')
      },
      onSubmit() {
        let that = this
        console.log('...提交订单...')
        if (!this.address_name) {
          Toast({
            message:"请选择收货地址",
            duration:800
          })
        }else {
          let user = JSON.parse(window.localStorage.getItem('userInfo'))
          console.log(user.user_id)
          console.log(this.goods)
          this.goods.forEach(function (value,index,array) {
            console.log(array[index])
            // 数据库需要 user_id + product_id + address_id + product_num
            var Axios = that.axios
            let params = new URLSearchParams()
            // params.append("username",user.user_name)
            params.append("username","TIANYUZHOU")
            params.append("addressid",that.address_id)
            params.append("productid",array[index].id)
            params.append("pnum",array[index].num)
            params.append("myprice",array[index].price * array[index].num)
            Axios({
              url:"/api/order_add/",
              method:"post",
              data:params,
              responseType:"text"
            }).then(function () {
              console.log("订单提交成功！")
            })
          })
        }
      }
    },
  }
</script>

<style>
  .out {
    width: 100%;
    height: 100%;
  }
  .image {
    display: inline-block;
    width: 30%;
    text-align: left;
  }
  .image > img {
    width: 4rem;
  }
  .goodsinfo {
    margin-top: 2px;
    display: flex;
    align-items: center;
    background-color: white;
    position: relative;
  }
  .goodsinfo > span {
    color: gray;
  }
  .span {
    margin-top: 5px;
    color: gray;
  }
  .span1{
    position: absolute;
    left: 45%;
  }
  .span2{
    position: absolute;
    right: 10px;
  }
  .pay {
    text-align: left;
    margin-top: 5px;
    margin-bottom: 15%;
  }
  .pay > span {
    color: gray;
    margin-left: 5px;
  }
  .circle {
    margin: auto 0;
  }
</style>
