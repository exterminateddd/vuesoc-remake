<template>
  <div class="container app-container">
    <header>
      
      <sidebar-menu :localeChangeHandler="setLocale">
      </sidebar-menu>
    </header>
    
    <router-view/>
  </div>
</template>

<script>
import SidebarMenu from '@/components/SidebarMenu.vue';
export default {
  components: {
    // MenuRouteLink: import('./components/MenuRouteLink.vue'),
    SidebarMenu
  },
  methods: {
    setLocale(newLocale) {
      this.$store.dispatch('setLocale', newLocale);
    }
  },
  inject: ['l'],
  mounted() {
    this.$store.dispatch('auth/updateUserData');
  }
}
</script>

<style>
@import "./styles/App.css";
</style>
