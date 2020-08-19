import Vue from "vue";
import VueRouter from "vue-router";

//引入一级组件//首页
import DashBoard from "./../views/dashboard/dashboard.vue";
//懒加载其它二级组件//首页下面的导航,点击才出来
const Home = () => import("./../views/home/home.vue");
const Category = () => import("./../views/category/category.vue");
const Cart = () => import("./../views/cart/cart.vue");
const Main = () => import("./../views/main/main.vue");
const Login = () => import('../views/login/Login.vue');
const UserCenter = () => import('../views/main/Children/UserCenter.vue');
const Order = () => import('../../src/views/order/Order.vue')
const MyAddress = () => import('../../src/views/order/children/MyAddress.vue')
const AddAddress = () => import('../../src/views/order/children/children/AddAddress.vue')
const EditAddress = () => import('../../src/views/order/children/children/EditAddress.vue')

Vue.use(VueRouter);

const originalPush = VueRouter.prototype.push;
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err);
};

export default new VueRouter({
  routes: [
    { path: "/", redirect: "/dashboard" },  //根路由 / 重定向到 /dashboard
    {
      path: "/confirmOrder", name: 'order', component: Order,
      // children: [{
      //   // path: "myAddress", name: 'myAddress', component: MyAddress,
      //   // children: [
      //   //   {path: "addAddress", name: 'addAddress', component: AddAddress},
      //   //   {path: "editAddress", name: 'editAddress', component: EditAddress},
      //   // ]
      // }]
    },
    {path: "/myAddress", name: 'myAddress', component: MyAddress},
    {path: "/addAddress", name: 'addAddress', component: AddAddress},
    {path: "/editAddress", name: 'editAddress', component: EditAddress},
    {
      path: "/dashboard",
      name: "dashboard",
      component: DashBoard,  //加载DashBoard组件

      children: [           //子路由
        { path: "/dashboard", redirect: "/dashboard/home" },
        { path: "home", name: "home", component: Home },
        { path: "main", name: "main", component: Main },
        { path: "category", name: "category", component: Category },
        { path: "cart", name: "cart", component: Cart },
        { path: 'userCenter', name: 'userCenter', component: UserCenter },
      ]
    },
    { path: '/login', name: 'login', component: Login }
  ]
});
