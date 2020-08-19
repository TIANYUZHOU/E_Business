<template>
  <div class="Edit">
    <van-nav-bar
      title="编辑收货地址"
      left-text="返回"
      right-text="按钮"
      left-arrow
      :fixed="true"
      :border="true"
      @click-left="onClickLeft"
      @click-right="onClickRight"
    />
    <van-address-edit
      :area-list="areaList"
      :address-info="AddressInfo"
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
        adderss_id:"",
        AddressInfo: {},
        
      }
    },
    mounted() {
      // 接收父组件传的地址表id
      console.log(this.$route)
      if (this.$route.query.id) {
        this.getCurrentAddress(this.$route.query.id)
      }
      this.adderss_id = this.$route.query.id
      let address = '/api/address/' + this.adderss_id
      this.axios.get(address).then((response) => {
        var address_data = response.data
        console.log(address_data)

        this.AddressInfo = {
          id: address_data.id,
          name: address_data.singer_name,
          tel: address_data.singer_mobile,
          province: address_data.province,
          city: address_data.city,
          county: address_data.district,
          addressDetail: address_data.address,
          areaCode: '00000',
          postalCode: '11111',
          isDefault: true,
        }
        console.log(this.AddressInfo)
      })
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
        let address_api = "/api/address/" + this.adderss_id
        this.axios.patch(address_api,address_js).then(response =>{
          var address_data = response.data
          console.log(address_data)
        })
        Toast('保存成功')
      },
      onDelete() {
        let address_delete = "/api/address/"+ this.adderss_id
        this.axios.delete(address_delete).then(
          console.log("删除成功！")
        )
        Toast('delete')
      },
      getCurrentAddress(user_id, adderss_id) {},
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
    },
  }
</script>

<style scoped>
  /* .edit-top {
          margin-top: -100%;
          width: 100%;
          height: 800px;
          position: fixed;
          background-color: #f8f8f8;
        }
        .edit-bottom1 {
          margin-bottom: 50px;
          position: fixed;
          background-color: red;
          height: 50px;
        }
        .edit {
          margin-top: -350px;
        } */
  .Edit {
    margin-top: 10%;
  }
</style>