<template>
  <div>
    <div class="add-top"></div>
    <van-nav-bar
      title="新增收货地址"
      left-text="返回"
      right-text="按钮"
      left-arrow
      :fixed="true"
      :border="true"
      @click-left="onClickLeft"
      @click-right="onClickRight"
    />
    <van-address-edit
      class="addaddress"
      :area-list="areaList"
      show-postal
      show-delete
      show-set-default
      show-search-result
      :search-result="searchResult"
      :area-columns-placeholder="['请选择', '请选择', '请选择']"
      @save="onSave"
      @delete="onDelete"
      @change-detail="onChangeDetail"
    />
    <div></div>
  </div>
</template>

<script>
  import addressSelect from './addressSelect'
  import { Toast } from 'vant'

  export default {
    data() {
      return {
        areaList: addressSelect,
        searchResult: [],
        add_user_id: '',
      }
    },
    mounted() {
      if (this.$route.query.id) {
        this.getCurrentAddress(this.$route.query.id)
      }
      this.add_user_id = this.$route.query.id
    },
    methods: {
      onClickLeft() {
        this.$router.back()
        Toast('返回')
      },
      onClickRight() {
        Toast('按钮')
      },
      onSave(content) {
        let province = content.province
        let city = content.city
        let district = content.county //区
        let address = content.addressDetail
        let singer_name = content.name
        let singer_mobile = content.tel
        let user_id = this.add_user_id

        let address_js ={
          "city":city,
          "province":province,
          "district":district,
          "address":address,
          "singer_name":singer_name,
          "singer_mobile":singer_mobile,
          "user":user_id,
          // "user_id":Number(user_id)
        }
        let address_api = "/api/create_address/"
        this.axios.post(address_api,address_js).then(response =>{
          var address_data = response.data
          console.log(address_data)
        })
        Toast('保存成功！')
      },
      onDelete() {
        Toast('delete')
      },
      onChangeDetail(val) {
        if (val) {
          this.searchResult = [
            {
              name: '黄龙万科中心',
              address: '杭州市西湖区',
            },
          ]
        } else {
          this.searchResult = []
        }
      },
      getCurrentAddress(user_id, adderss_id) {},
    },
  }
</script>
<style scoped>
  /* .add-top {
          margin-top: -100%;
          width: 100%;
          height: 800px;
          position: fixed;
          background-color: #f8f8f8;
        } */
  .addaddress {
    margin-top: 10%;
  }
</style>