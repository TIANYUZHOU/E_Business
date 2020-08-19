<template>
  <div id="address">
    <div class="address-top"></div>
    <van-nav-bar
      title="我的收货地址"
      left-text="返回"
      right-text="按钮"
      left-arrow
      :fixed="true"
      :border="true"
      @click-left="onClickLeft"
      @click-right="onClickRight"
    />
    <van-address-list
      class="address"
      v-model="chosenAddressId"
      :list="list"
      :disabled-list="disabledList"
      disabled-text="以下地址超出配送范围"
      default-tag-text="默认"
      @add="onAdd"
      @edit="onEdit"
      @select="onBackAddress"
    />
    <router-view />
  </div>
</template>

<script>
  import { Toast } from 'vant'
  import { mapState } from 'vuex'
  import pubsub from 'pubsub-js'

  export default {
    data() {
      return {
        user_id: "",
        chosenAddressId: '1',
        list: [],
        disabledList: [
          {
            id: '3',
            name: '王五',
            tel: '1320000000',
            address: '浙江省杭州市滨江区江南大道 15 号',
          },
        ],
      }
    },
    created() {
      this.getAddress()
    },
    mounted() {},
    computed: {
      ...mapState(['userInfo']),
    },
    methods: {
      onClickLeft() {
        this.$router.back()
        Toast('返回')
      },
      onClickRight() {
        Toast('按钮')
      },
      onAdd() {
        this.$router.push({
          path: 'addAddress?id=' + this.user_id,
        })
        Toast('新增地址')
      },
      onEdit(item, index) {
        this.$router.push({
          path: 'editAddress?id=' + item.id,
        })
        Toast('编辑第' + (index + 1) + '个地址')
      },
      // 发布信号，带地址
      onBackAddress(item,index) {
        // console.log(item,index)
        if(item) {
          // 发布地址数据userAddress 暗号
          pubsub.publish('userAddress',item)
          // 返回上一级
          this.$router.back()
        }
      },
      getAddress() {
        let userdata = window.localStorage.getItem('userInfo')
        console.log(userdata)
        console.log(typeof userdata)
        console.log(JSON.parse(userdata).user_id)
        // this.user_id = JSON.parse(userdata).user_id
        let user_name = JSON.parse(userdata).user_name
        console.log(user_name)
        //
        let add_api = '/api/get_address/' + 'TIANYUZHOU'

        this.axios.get(add_api).then((response) => {
          var address = response.data
          // var msg = JSON.parse(address)
          // address = JSON.parse(address)
          console.log(address)
          console.log(typeof address)
          this.user_id = address[0].user.id
          console.log(this.user_id)

          var address_list = []
          for (let one of address) {
            let add_dict = {}
            add_dict['id'] = one.id
            add_dict['name'] = one.singer_name
            add_dict['tel'] = one.singer_mobile
            add_dict['address'] =
              one.province + one.city + one.district + one.address
            address_list.push(add_dict)
          }
          this.list = address_list
        })
      },
    },
  }
</script>

<style scoped>
  /* .address-top {
              background-color: #f8f8f8;
              position: fixed;
              margin-top: -50%;
              width: 100%;
              height: 720px;
            } */
  .address {
    margin-top: 10%;
  }
</style>
