// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.

//main.js注册全局
import Vue from 'vue'
import App from './App'
import router from './router'
import '../plugins/vant.js'
import './style/comment.css'
import './style/buttons.css'
import './filter/filter.js'
import store from './store/index'

//底部标签栏
import { Tabbar, TabbarItem } from 'vant';
Vue.use(Tabbar);
Vue.use(TabbarItem);

import { Tab, Tabs } from 'vant';
Vue.use(Tab);
Vue.use(Tabs);

// import { Lazyload } from 'vant';
// Vue.use(Lazyload)

import { Grid, GridItem } from "vant";

Vue.use(Grid);
Vue.use(GridItem);

import axios from 'axios'
Vue.prototype.axios = axios

Vue.config.productionTip = false

import VueLazyload from 'vue-lazyload'
Vue.use(VueLazyload, {
     loading: require('@/assets/loading.png'),//加载中图片，一定要有，不然会一直重复加载占位图
     error: require('@/assets/error.png')  //加载失败图片
})

import { SubmitBar } from 'vant'

Vue.use(SubmitBar)

import { Cell, CellGroup } from 'vant'

Vue.use(Cell)
Vue.use(CellGroup)

import { Tag } from "vant";

Vue.use(Tag);

import { NavBar } from "vant";

Vue.use(NavBar);

import { Divider } from "vant";

Vue.use(Divider);

import { Icon } from "vant";

Vue.use(Icon);

import { Button } from "vant";

Vue.use(Button);

import { Field } from "vant";

Vue.use(Field);

import { Toast } from "vant";

Vue.use(Toast);

import { CountDown } from "vant";

Vue.use(CountDown);

import { Dialog } from 'vant';


Vue.use(Dialog);

import { AddressEdit } from 'vant';

Vue.use(AddressEdit);

import { AddressList } from 'vant';

Vue.use(AddressList);

import { Area } from 'vant';

Vue.use(Area);

import { ContactCard, ContactList, ContactEdit } from 'vant';

Vue.use(ContactCard);
Vue.use(ContactList);
Vue.use(ContactEdit);

import { CouponCell, CouponList } from 'vant';

Vue.use(CouponCell);
Vue.use(CouponList);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
