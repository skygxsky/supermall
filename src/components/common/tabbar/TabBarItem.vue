<template>
<!--  <div class="tab-bar-item">-->


<!--  </div>-->
  <div class="tab-bar-item" @click="itemClick">
<!--    <slot v-if="!isActive" name="item-icon"></slot>-->
<!--    <slot v-else name="item-icon-active"></slot>-->
    <div v-if="!isActive"><slot name="item-icon"></slot></div>
    <div v-else ><slot name="item-icon-active"></slot></div>
<!--    <slot :class="{active:isActive}" name="item-text"></slot>-->
    <div :style="activeStyle"><slot name="item-text"></slot></div>
<!--    <img src="../../assets/img/tabbar/home.svg" alt="">-->
<!--    <div>首页</div>-->
  </div>

<!--  <div class="tab-bar-item">-->
<!--    <img src="../../assets/img/tabbar/category.svg" alt="">-->
<!--    <div>分类</div>-->

<!--  </div>-->
<!--  <div class="tab-bar-item">-->
<!--    <img src="../../assets/img/tabbar/shopcart.svg" alt="">-->
<!--    <div>购物车</div>-->

<!--  </div>-->
<!--  <div class="tab-bar-item">-->
<!--    <img src="../../assets/img/tabbar/profile.svg" alt="">-->
<!--    <div>我的</div>-->
<!--  </div>-->
</template>

<script>
export default {
  name: "TabBarItem",
  props:{
    path:String,
    activeColor:{
      type:String,
      default:'red'
    }
  },
  data(){
    return{
      // isActive:true
    }
  },
  computed:{
    isActive(){
      return this.$route.path.indexOf(this.path) !== -1
    },
    activeStyle(){
      return this.isActive ? {color: this.activeColor} : {}
    }
  },
  methods:{
    itemClick(){
      // 返回无效
      this.$router.replace(this.path)
    }
  }
}
</script>

<style scoped>
.tab-bar-item{
  /*均等分*/
  flex: 1;
  /*  文本居中*/
  text-align: center;
  height: 49px;
  font-size: 14px;
}

.tab-bar-item img{
  width: 24px;
  height: 24px;
  margin-top: 3px;
/*  图片去掉下面的像素*/
  vertical-align: middle;
  margin-bottom: 2px;
}


</style>
