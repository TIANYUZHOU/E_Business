<template>
  <div class="wrapper">
    <div class="itemWrapper" v-for="(nav, index) in nav_list" :key="index">
      <div class="imageWrapper">
        <img class="image" :src="nav.icon_url" :alt="nav.name" />
      </div>
      <div class="titleWrapper">
        <div class="title">{{ nav.name }}</div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return {
        nav_list: [
          {
            cid: 0,
            icon_url:
              '../../../../static/camera/相机.png',
            name: '相机'
          },
          {
            cid: 1,
            icon_url:
              '../../../../static/camera/镜头.png',
            name: '镜头'
          },
          {
            cid: 2,
            icon_url:
              '../../../../static/camera/闪光灯.png',
            name: '闪光灯'
          },
          {
            cid: 3,
            icon_url:
              '../../../../static/camera/话筒.png',
            name: '话筒'
          },
          {
            cid: 4,
            icon_url:
              '../../../../static/camera/数据线.png',
            name: '数据线'
          },
          {
            cid: 5,
            icon_url:
              '../../../../static/camera/包包.png',
            name: '相机包'
          },
          {
            cid: 6,
            icon_url:
              '../../../../static/camera/三脚架.png',
            name: '三脚架'
          },
          {
            cid: 7,
            icon_url:
              '../../../../static/camera/数码-快门线.png',
            name: '快门线'
          },
          {
            cid: 8,
            icon_url:
              '../../../../static/camera/稳定器.png',
            name: '稳定器'
          },
          {
            cid: 9,
            icon_url:
              '../../../../static/camera/无人机.png',
            name: '无人机'
          }
        ]
      }
    }
  }
</script>

<style scoped>
  .wrapper {
    padding-top: 0.9375rem;
    background: #fff;
    padding-bottom: 0.9375rem;
    margin-top: -6px;
  }

  .itemWrapper {
    display: inline-block;
    padding-top: 0.3125rem;
    width: 20%;
  }

  .imageWrapper {
    padding-bottom: 58.823%;
    height: 0;
    overflow: hidden;
    text-align: center;
  }

  .image {
    width: 58.823%;
    height: auto;
    display: inline-block;
  }

  .titleWrapper {
    padding: 0.4375rem 0.3125rem 0.375rem 0.3125rem;
  }

  .title {
    font-size: 0.7rem;
    color: #555555;
    text-align: center;
    overflow: hidden;
    white-space: nowrap;
    text-overflow: ellipsis;
  }
</style>
